import docker
import psutil

class DockerMonitor:
    def __init__(self):
        try:
            # Verbindet sich mit dem lokalen Docker-Socket (unter Linux/ZimaOS /var/run/docker.sock)
            self.client = docker.from_env()
        except Exception as e:
            self.client = None
            print(f"Fehler bei der Docker-Verbindung: {e}")

    def get_system_stats(self):
        try:
            cpu_total = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory()
            
            total_gb = mem.total / (1024**3)
            used_gb = mem.used / (1024**3)
            
            return {
                'cpu_total': f"{cpu_total:.1f}%",
                'ram_total': f"{used_gb:.1f} GB / {total_gb:.1f} GB",
                'ram_percent': mem.percent
            }
        except Exception as e:
            print(f"Fehler beim Abrufen der System-Stats: {e}")
            return {
                'cpu_total': "0.0%",
                'ram_total': "0.0 GB / 0.0 GB",
                'ram_percent': 0
            }

    def get_container_stats(self):
        if not self.client:
            return []

        containers_data = []
        try:
            for container in self.client.containers.list(all=True):
                # Standardwerte
                cpu_percent = 0.0
                memory_usage = "0 MB"
                memory_limit = "0 MB"
                
                # Wenn der Container läuft, holen wir uns die Echtzeit-Stats
                if container.status == 'running':
                    try:
                        # stream=False liefert einen einmaligen JSON-Snapshot der Stats
                        stats = container.stats(stream=False)
                        
                        # CPU-Berechnung (Docker liefert rohe CPU- und System-Delta-Werte)
                        cpu_stats = stats.get('cpu_stats', {})
                        precpu_stats = stats.get('precpu_stats', {})
                        
                        cpu_delta = cpu_stats.get('cpu_usage', {}).get('total_usage', 0) - precpu_stats.get('cpu_usage', {}).get('total_usage', 0)
                        system_delta = cpu_stats.get('system_cpu_usage', 0) - precpu_stats.get('system_cpu_usage', 0)
                        
                        online_cpus = cpu_stats.get('online_cpus', len(cpu_stats.get('cpu_usage', {}).get('percpu_usage', [1])))
                        
                        if system_delta > 0 and cpu_delta > 0:
                            cpu_percent = (cpu_delta / system_delta) * online_cpus * 100.0

                        # RAM-Berechnung
                        memory_stats = stats.get('memory_stats', {})
                        used_memory = memory_stats.get('usage', 0)
                        limit_memory = memory_stats.get('limit', 0)
                        
                        # Umrechnung in Megabyte (MB)
                        memory_usage = f"{used_memory / (1024 * 1024):.1f} MB"
                        memory_limit = f"{limit_memory / (1024 * 1024):.1f} MB"

                    except Exception:
                        pass # Falls beim Abrufen der Stats ein Fehler auftritt, ignorieren wir es temporär

                containers_data.append({
                    'id': container.id,
                    'name': container.name,
                    'image': container.image.tags[0] if container.image.tags else 'Unbekannt',
                    'status': container.status,
                    'cpu': f"{cpu_percent:.1f}%",
                    'memory': f"{memory_usage} / {memory_limit}"
                })
        except Exception as e:
            print(f"Fehler beim Abrufen der Container: {e}")

        return containers_data
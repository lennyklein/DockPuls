import os
import docker
from datetime import datetime

class DockerMonitor:
    def __init__(self):
        try:
            # Verbindet sich über den Docker-Socket des Hosts
            self.client = docker.from_env()
        except Exception as e:
            print(f"Fehler bei der Docker-Verbindung: {e}")
            self.client = None

    def get_container_stats(self):
        if not self.client:
            return [{"name": "Fehler", "status": "Keine Verbindung zu Docker", "created": "-"}]
        
        container_list = []
        try:
            for container in self.client.containers.list(all=True):
                container_list.append({
                    "name": container.name,
                    "status": container.status, # z.B. running, exited
                    "image": container.image.tags[0] if container.image.tags else "Lokales Image",
                    "id": container.short_id
                })
        except Exception as e:
            print(f"Fehler beim Abrufen der Container: {e}")
        
        return container_list
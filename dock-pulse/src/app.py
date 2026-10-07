import os
from flask import Flask, render_template, jsonify, redirect, url_for
from monitor import DockerMonitor

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

monitor = DockerMonitor()

@app.route('/')
def index():
    containers = monitor.get_container_stats()
    system = monitor.get_system_stats()  # <--- HIER: System-Stats abrufen
    return render_template('index.html', containers=containers, system=system)  # <--- HIER: system übergeben

@app.route('/container/<action>/<container_id>', methods=['POST'])
def control_container(action, container_id):
    try:
        import docker
        client = docker.from_env()
        container = client.containers.get(container_id)
        
        if action == 'stop':
            container.stop()
        elif action == 'start':
            container.start()
        elif action == 'restart':
            container.restart()
            
        return jsonify({'status': 'success', 'message': f'Container {container_id} {action}ed.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

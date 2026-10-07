import os
from flask import Flask, render_template, jsonify, redirect, url_for
from monitor import DockerMonitor

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

monitor = DockerMonitor()

@app.route('/')
def index():
    containers = monitor.get_container_stats()
    return render_template('index.html', containers=containers)

@app.route('/container/<action>/<container_id>', methods=['POST'])
def control_container(action, container_id):
    try:
        if action == 'stop':
            monitor.stop_container(container_id)
        elif action == 'start':
            monitor.start_container(container_id)
        elif action == 'restart':
            monitor.restart_container(container_id)
        return jsonify({'status': 'success', 'message': f'Container {container_id} {action}ed successfully.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

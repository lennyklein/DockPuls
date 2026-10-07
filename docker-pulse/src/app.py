import os
from flask import Flask, render_template
from monitor import DockerMonitor

# Wir sagen Flask genau, wo der 'templates'-Ordner liegt (ein Verzeichnis höher, im Hauptordner)
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

monitor = DockerMonitor()

@app.route('/')
def index():
    containers = monitor.get_container_stats()
    return render_template('index.html', containers=containers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
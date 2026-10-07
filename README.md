<div align="center">

# ⚡ DocPuls
### Der ultra-schlanke, elegante Realtime-Container-Monitor für Homelabs & ZimaOS.

<div align="center">

<p align="center">
  <img src="https://raw.githubusercontent.com/lennyklein/lennyklein/refs/heads/main/assets/dockpuls-banner.svg" alt="DocPuls Banner" width="100%">
</p>

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-UI-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 🚀 Über das Projekt
Vergiss überladene Enterprise-Monitoringsysteme. **DocPuls** wurde für Self-Holster und Homelab-Enthusiasten entwickelt, die eine blitzschnelle, minimalistische und wunderschöne Übersicht über ihre aktiven Docker-Container haben wollen – ohne Bloatware.

---

## 🚀 Schnellstart & lokale Installation

### 1. Repository klonen oder herunterladen
Lade das Projekt als ZIP-Datei herunter oder klone es direkt per Git:
`git clone https://github.com/lennyklein/docpuls.git`

### 2. Abhängigkeiten installieren
Stelle sicher, dass Python auf deinem System installiert ist. Installiere die benötigten Pakete mit diesem Befehl im Projektordner:
`pip install -r requirements.txt`

### 3. Anwendung starten
Starte den lokalen Flask-Entwicklungsserver mit folgendem Befehl:
`python src/app.py`

### 4. Im Browser öffnen
Öffne deinen Webbrowser und rufe diese Adresse auf:
`http://127.0.0.1:5000`

---

## 🐳 Docker & ZimaOS Deployment (Empfohlen)
Wenn du das Tool dauerhaft und isoliert auf deinem Server laufen lassen möchtest, nutze Docker Compose:
`docker compose up -d --build`

---

## 🗺️ Roadmap
- [x] Basis-Container-Status (Running / Stopped)
- [x] CPU- und RAM-Auslastung in Echtzeit (inkl. Host-Gesamtübersicht)
- [x] Live-Auto-Refresh und Steuerungs-Aktionen (Start / Stop / Neustart)
- [ ] Discord-Webhook Benachrichtigungen bei Container-Ausfällen

---

## 📝 Lizenz
Dieses Projekt steht unter der [MIT License](LICENSE).


<p align="center">
  <img src="https://raw.githubusercontent.com/lennyklein/lennyklein/refs/heads/main/assets/banner.svg" alt="Lenny Klein Banner" width="100%">
</p>

FROM python:3.11-slim

WORKDIR /app

# System-Abhängigkeiten installieren, falls nötig
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Python-Pakete installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Quellcode kopieren
COPY . .

EXPOSE 5000

CMD ["python", "src/app.py"]
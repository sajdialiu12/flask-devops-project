# Flask DevOps Project

A Dockerized Flask app.

## Run locally
python app.py

## Run via Docker
docker build -t simple-devops-app .
docker run -p 5000:5000 simple-devops-app

## Optional: Expose with ngrok
./ngrok http 5000

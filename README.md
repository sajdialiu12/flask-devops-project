# Flask DevOps Project

A simple Dockerized Flask app.

## Run locally
python app.py

## Run with Docker
docker build -t simple-devops-app .
docker run -p 5000:5000 simple-devops-app

## Optional: Expose with ngrok
./ngrok http 5000

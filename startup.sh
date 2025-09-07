#!/bin/bash
# Startup script for Azure App Service

echo "Starting FastAPI application..."

# Install dependencies if not already installed
pip install -r requirements.txt

# Start the application with Gunicorn and Uvicorn workers
exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 --timeout 120

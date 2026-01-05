#!/bin/bash
# Ensure we are in the script's directory (VibeSnip)
cd "$(dirname "$0")"

source .venv/bin/activate
# Log to server.log in the current directory (VibeSnip/)
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &
echo "VibeSnip started with PID $!"
echo "Logs are being written to $(pwd)/server.log"

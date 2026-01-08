#!/bin/bash

# Ensure we are in the script's directory (VibeSnip)
cd "$(dirname "$0")"

PID_FILE="server.pid"
LOG_FILE="server.log"

case "$1" in
  start)
    if [ -f "$PID_FILE" ]; then
      PID=$(cat "$PID_FILE")
      if ps -p "$PID" > /dev/null 2>&1; then
        echo "VibeSnip is already running with PID $PID."
        exit 1
      else
        echo "Found stale PID file. Removing..."
        rm "$PID_FILE"
      fi
    fi

    echo "Starting VibeSnip..."
    source .venv/bin/activate
    nohup .venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 > "$LOG_FILE" 2>&1 &
    PID=$!
    echo "$PID" > "$PID_FILE"
    echo "VibeSnip started with PID $PID"
    echo "Logs are being written to $(pwd)/$LOG_FILE"
    ;;

  stop)
    if [ ! -f "$PID_FILE" ]; then
      echo "VibeSnip is not running (PID file not found)."
      exit 1
    fi

    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
      echo "Stopping VibeSnip (PID $PID)..."
      kill "$PID"
      rm "$PID_FILE"
      echo "VibeSnip stopped."
    else
      echo "Process $PID not found. Removing stale PID file..."
      rm "$PID_FILE"
    fi
    ;;

  restart)
    $0 stop
    $0 start
    ;;

  *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
    ;;
esac
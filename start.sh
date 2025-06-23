#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/app
exec adk web --static-dir /app/frontend_dist --port 8080

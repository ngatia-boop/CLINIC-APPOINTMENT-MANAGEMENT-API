#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting app with Gunicorn..."
exec gunicorn main:app --bind 0.0.0.0:$PORT

#!/usr/bin/bash

echo "Bắt đầu khởi động..."
gunicorn -b 0.0.0.0:8080 --log-level critical main:app
#!/bin/bash

set -e 

sudo apt update 

sudo apt install -y python-is-python3 python3-venv python3-pip

python -m venv .my_venv

source .my_venv/bin/activate

pip install flask

echo "Setup complete."

echo "Run: source .my_venv/bin/activate"

echo "Then: flask --app hello run --host=0.0.0.0"

#!/bin/bash

echo "Starting import process..."

python3 get-nyc.py

python3 load-csvs.py

echo "Imports complete."s
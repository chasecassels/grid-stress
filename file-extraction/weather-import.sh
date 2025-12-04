#!/bin/bash

echo "Starting import process..."

python3 get-nyc.py

python3 load-weather-csvs.py

echo "Imports complete."s
#!/bin/bash

python3 -m venv chores-venv
source chores-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py
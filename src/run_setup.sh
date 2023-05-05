#!/bin/bash

# This bash script sets up the requirements for the application to run and links to the ./run.sh script

python3 --version

python3 -m venv chores-venv
source chores-venv/bin/activate
pip3 install -r requirements.txt

./run.sh
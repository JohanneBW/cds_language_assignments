#!/usr/bin/env bash

VENVNAME=Assignment_4

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

# run script
python3 network.py

deactivate
echo "build $VENVNAME"

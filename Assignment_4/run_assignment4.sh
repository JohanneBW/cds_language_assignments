#!/usr/bin/env bash

VENVNAME=Assignment_4

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

python -m spacy download en_core_web_sm

# run script
cd src
python3 network.py

deactivate
echo "build $VENVNAME"

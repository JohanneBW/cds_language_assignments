#!/usr/bin/env bash

VENVNAME=LA_Assignment3_venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

#echo "build $VENVNAME"

#download
python3 -m spacy download en_core_web_sm

#run script
python3 sentiment.py

#deactivate environment
deactivate

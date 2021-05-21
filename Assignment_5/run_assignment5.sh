#!/usr/bin/env bash

VENVNAME=LA_Assignment5_venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

#download spacy model
python -m spacy download en_core_web_sm

#run script
cd src
python3 GameStop_LDA.py

#deactivate environment
deactivate
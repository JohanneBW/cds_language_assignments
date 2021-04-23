#!/usr/bin/env bash

VENVNAME=Assignment_W6_env

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install -r requirements.txt

deactivate
echo "build $VENVNAME"

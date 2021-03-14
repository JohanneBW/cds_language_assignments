#!/usr/bin/env bash

#Environment name
VENVNAME=Assignment_W6_env

#Activate environment
source $VENVNAME/bin/activate

#Upgrade pip
pip install --upgrade pip

# test and install from requirements.txt
test -f requirements.txt && pip install requirements.txt

# download NLP model 
python -m spacy download en_core_web_sm

#run script
python3 assignment_W6.py --file $file

#deactivate environment
deactivate

#Print to terminal
echo "Done, the visualization is located in the 'viz' folder and the data frame in the 'output' folder'"

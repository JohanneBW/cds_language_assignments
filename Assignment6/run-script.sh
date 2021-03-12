#!/usr/bin/env bash

#Environment name
VENVNAME=assignment_w6

#Activate environment
source $VENVNAME/bin/activate

#Upgrade pip
pip install --upgrade pip

# problems when installing from requirements.txt
test -f requirements.txt && pip install requirements.txt

#parameters
#filepath=${1:-"data/king_james_bible.csv"}
#edgeweight=${2:->500}

#run script
python3 assignment_w6.py --file $file

#deactivate environment
deactivate

#Print to terminal
echo "Done, the visualization is located in the 'viz' folder and the data frame in the 'output' folder'"

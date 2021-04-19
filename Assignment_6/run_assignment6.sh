#!/usr/bin/env bash

VENVNAME=LA_Assignment6_venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install requirements.txt

echo "build $VENVNAME"

#download and unzip pretraind embeddings
cd data
wget http://nlp.stanford.edu/data/glove.6B.zip
unzip -q glove.6B.zip

#run scripts
cd ..
python3 LRModel.py $@
python3 DLModel.py $@

#deactivate environment
deactivate

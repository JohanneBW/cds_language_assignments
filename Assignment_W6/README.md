## Assignment 6 - Creating reusable network analysis pipeline
**Johanne BW**

The purpose with this assignment is to make a command-line tool which will take a given dataset and perform simple network analysis. 
In particular, it will build networks based on entities appearing together in the same documents.

For any given CSV file, with a column called 'text', create a weighed edgelist of named entities, based on document co-ocurrence. This will be used to create a network visualization, which will be saved in a folder called viz. It will also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It will save this as a CSV in a folder called output."

## How to run
**Step 1: Clone repo**
- open terminal
- Navigate to destination you want the repo
- type the following command
 ```console
 git clone https://github.com/JohanneBW/cds_language_assignments.git
 ```
**step 2: Set up enviroment:**
- Navigate to the folder "Assignment_W6".
```console
cd cds_language_assignments
cd Assignment_W6
```  
- Use the bash script _create_venv.sh_ to set up environment:  
```console
bash create_venv.sh
```  
**step 3: Run the program:**
- Navigate to the folder "Assignment_W6" if you are not already there
- Run the program with a csv as input:
```console
python3 assignment_W6.py -i "data/king_james_bible.csv"
```  
**step 4: Output:**
- Check the 'viz' and 'output' folder to see vizualization and edgelist

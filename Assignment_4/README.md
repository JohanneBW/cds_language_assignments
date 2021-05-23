## Assignment 4 - Creating reusable network analysis pipeline
**Johanne BW**

__Contribution__

I didn’t work with others on this assignment.

__Assignment description__

The purpose with this assignment is to make a command-line tool which will take a given dataset and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents. For any given CSV file, with a column called 'text', create a weighed edge list of named entities based on document co-occurrence. This will be used to create a network visualization and also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. 


__Methods__

I primarily used SpaCy and NetworkX in this task. I used SpaCy to create text entities based on the input file and NetworkX was used to plot the visualization as well as calculate betweenness- and eigenvector centrality. 

__Usage__

_Structure:_
The repository contains the folders data, src, viz and output. The data folder contains the csv file king_james_bible.csv. This file will be used as a default if another path isn’t defined when running the script from the command-line. The src folder contains the script network.py which create the text enti-ties and creates a network. The viz folder contains the visualization output, and the output folder con-tains the csv file with information about betweenness- and eigenvector centrality.  

_Arguments:_
It is possible to select the text on which you want to create a network. This is done by specifying the path that leads to the csv file you want. This is done by "-i" or "--path" when running the script. The script has a default text, king_james_bible.csv located in the data folder, so it is easier to test.

I have created a bash script that creates and activates a virtual environment, retrieves necessary libraries from the requirements.txt file and runs the script for the assignment.

## How to run
The following shows how to set up the virtual environment and run the script step by step.
**Step 1: Clone repo**
- open terminal
- Navigate to destination you want the repo
- type the following command
 ```console
 git clone https://github.com/JohanneBW/cds_language_assignments.git
 ```
**step 2: Set up enviroment and run script:**
- Navigate to the folder "Assignment_4".
```console
cd cds_language_assignments
cd Assignment_4
```  
- Use the bash script _run_assignment4.sh_ to set up environment and run the script:  
```console
bash create_venv.sh
```  
**Else:**
- Navigate to the folder "Assignment_4" if you are not already there
- Run the program with a csv as input:
```console
python3 assignment_4.py -i "data/king_james_bible.csv"
```  
**step 3: Output:**
- Check the 'viz' and 'output' folder to see vizualization and edgelist

__Discussion of results__

To make the script more reusable I have chosen that the input should consist of a csv file with a column called text rather than a csv file with a weighted edgelist. This means that both the edgelist and the network are created in the same script. However, it should be mentioned that not all csv files you want to create a network for have a column called text. That the input file should have a column called text makes it easier to make an edgelist on the right column. This could possibly be made more universal by also having to define the desired column for calculating an edgelist through an argument when running the script. Otherwise, minimal data wrangling is required to change the name of a column in the data if you want to use the script. Therefore, I argue that the script is still reusable.

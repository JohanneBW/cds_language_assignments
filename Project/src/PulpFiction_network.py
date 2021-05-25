'''
---------------- Libraries ----------------------
'''

import os
import pandas as pd
import matplotlib.pyplot as plt

#NLP
import spacy
nlp = spacy.load("en_core_web_sm")

#Edgelist
from itertools import combinations
from collections import Counter

#Network
import networkx as nx
plt.rcParams["figure.figsize"] = (20,20)

def main():
    '''
    ----------------- Read data ----------------------
    '''

    '''
    The first thing we do is read in the csv file with our data. 
    The files is located in the data folder.
    '''

    #Define data path
    input_file = os.path.join("..", "data", "pulp_fiction_dialogue.csv")

    #Read data as a csv using Pandas
    data = pd.read_csv(input_file)


    '''
    ----------------- Data wrangling ----------------------
    '''

    '''
    The next thing we do is some simple data wrangling. 
    We rename the column with the character name to avoid spaces in the name.
    Then we join the two columns with character and line. 
    We do this because we want to use network analysis based on node pairs/characters appearing together .
    Therefore we need to have both the person speaking and the person being spoken to in our text.
    '''

    #We rename the column to avoid spaces in the name
    data = data.rename(columns = {"Character (actual)" : "Character"}, inplace = False)

    #Join the columns with the character and the line
    data = data.assign(United = data.Character.astype(str) + ": " + data.Line.astype(str))
    
    '''
    ----------------- Post entities -------------
    '''

    '''
    The next step is to transform the text into a doc object using SpaCy.
    We are only interested in the entities with the label PERSON because we want to focus on the characters.
    Then we store the entities in a list.
    '''

    #Create empty list where the entities will be storred 
    post_entities = []

    print("Create post entities...")

    #For every line in the column United
    for line in data["United"]:
        # create a temporary list
        tmp_list = []
        # create spacy doc object
        doc = nlp(line)
        # for every named entity in the doc
        for entity in doc.ents:
            # if the entity label is equal to Person(SpaCy)
            if entity.label_ == "PERSON":
                # append the entity to the temporary list
                tmp_list.append(entity.text)
        # add tmp_list to post_entities list
        post_entities.append(set(sorted(tmp_list)))

    print("Post entities are created!")


    '''
    ------------------- Edgelist --------------------
    '''  

    '''
    The next thing we do is make an edgelist. 
    The edge list contains the node pairs that appear together in the text. 
    We use Itertools combinations function with 2 as our combination number. 
    This means that we look for characters/nodes who perform/appear together in pairs.
    '''
    #Create empty list where the nodes will be storred 
    edgelist = []

    print("Create edgelist...")

    # iterate over every document in our post_entities list
    for doc in post_entities:
        # use combinations to create edgelist. We look at combinations of two nodes
        edges = list(combinations(doc,2))
        #for each combination - i.e. each pair of 'nodes'
        for edge in edges:
            # append this to edgelist
            edgelist.append(tuple(sorted(edge)))

    print("Edgelist is created!")

    #Create empty list where the counted nodes will be storred         
    counted_edges = []

    print("Count node pairs...")

    #Count every node pair in the edgelist
    for pair, weight in Counter(edgelist).items():
        #nodeA is the value on index 0
        nodeA = pair[0]
        #nodeB is the value on index 1
        nodeB = pair[1]
        #Append the nodes and their weight to the counted_edges list
        counted_edges.append((nodeA, nodeB, weight))

    #Print the counted edges
    print(f"There is: {len(counted_edges)} node pairs in the counted edges")


    #Create data frame with the colomns: nodeA, nodeB and weight
    edges_df = pd.DataFrame(counted_edges, columns=["nodeA", "nodeB", "weight"])

    #Create data frame with the node pairs with a weight of more than one
    filtered_df = edges_df[edges_df["weight"]>1]

    print(f"{len(filtered_df)} of the node pairs have a weight of more than one")
    
    '''
    ------------------ Network -------------------
    '''
    '''
    The next step is to create and plot our network model using NetworkX.
    '''

    print("Create network based on node pair weight...")

    #Create network based on the filtered edges
    network = nx.from_pandas_edgelist(filtered_df, "nodeA", "nodeB", ["weight"])

    #Define outpath for the vizualization
    outpath_viz = os.path.join("..","output", "network_viz.png")

    #Create and draw the vizualization 
    viz = nx.nx_agraph.graphviz_layout(network, prog="neato")
    nx.draw(network, viz, with_labels=True, node_size=20, font_size=10)

    #Save the vizualization 
    plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")

    print("The network is created and can be found in the output folder!")
    
    '''
    ------------------ Centrality measures ---------------
    '''

    print("Find centrality measures...")

    #Find the eigenvector centrality                            
    ev = nx.eigenvector_centrality(network)                            
    #Make df with the eigenvector centrality                              
    ev_df = pd.DataFrame(ev.items(), columns=["nodeA", "eigenvector"])

    #Find betweenness centrality
    bc = nx.betweenness_centrality(network)                                                           
    #Make df with the betweenness centrality
    bc_df = pd.DataFrame(bc.items(), columns=["nodeA", "betweenness"])   

    #Merge the three data frames into one
    Centrality_measure_df = pd.merge(bc_df, ev_df, how="inner", on=["nodeA"])
    Centrality_measure_df = pd.merge(Centrality_measure_df, filtered_df, how="inner", on=["nodeA"])

    #Define outpath for the centrality measure data frame                             
    outpath_df = os.path.join("..", "output", "Centrality_measure.csv") 
    #Save the merged data frame as a csv in the output folder 
    Centrality_measure_df.to_csv(outpath_df)
    
    #Create data frame for the number of spoken lines per character
    spoken_lines = pd.DataFrame(data["Character"].value_counts())
    #Define outpath for the data frame
    lines_out = os.path.join("..", "output", "Spoken_lines.csv")
    #Save the data frame
    spoken_lines.to_csv(lines_out)
    
    print("The centrality measures are located in the output folder!")
    
                                 
#Define behaviour when called from command line
if __name__ == "__main__":
    main()
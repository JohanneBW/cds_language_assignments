"""
---------- Import libraries ----------
"""
# System tools
import os, glob
import sys
import argparse

# Data analysis
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm

# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# drawing
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)

"""
---------- Main function ----------
"""
def main():
    
    """
    ---------- Parameters ----------
    """
    # Create an argument parser from argparse
    ap = argparse.ArgumentParser(description = "[INFO] Create a weighed edgelist of named entities, based on document co-ocurrence"
                                 
    # File 
    ap.add_argument("-f", "--filepath", required = False,
                    type = str, help = "file from path e.g. 'data/file.csv'")
    # Edge weight
    ap.add_argument("-e", "--edgeweight", required = False, type = int, help = "define a cut-off point to filter data")    
        
    args = vars(ap.parse_args())
    
    """
    ------ Read data to dataframe ------
    """
    
    # Only make a df if the file is a csv file and have a column called 'text'
    filepath = args["filepath"]
                                 
    if filepath.endswith(".csv"): 
        data = pd.read_csv(filepath)
        if 'text' in data.columns:
            # Make a df with the data
            text_df = pd.DataFrame(data)
    else:
        print("The file needs to be a csv file and have a column called 'text'")                                                                                                        
    
    """
    ----- Extract all named entities ------
    """
    
    # Create empty list were the entities will be stored
    text_entities = []

    # Loop over the text in the text column of the df
    for text in tqdm(text_df["text"]):
        # create temporary list 
        tmp_entities = []
        # create doc object
        doc = nlp(text)
        # for every named entity
        for entity in doc.ents:
            # append to temp list
            tmp_entities.append(entity.text)
        # append temp list to main list
        text_entities.append(tmp_entities)
                                 
    
    """
    ---------- Create edgelist ------------
    """
    # Create empty list were the edgelist will be stored
    edgelist = []
                                 
    # Iterate over every document
    for text in text_entities:
        # Use itertools.combinations() to create edgelist
        edges = list(combinations(text, 2))
        # For each combination - i.e. each pair of 'nodes'
        for edge in edges:
            # Append this to final edgelist
            edgelist.append(tuple(sorted(edge)))
    

    """
    ----------- Count occurrences -----------
    """
    # Create empty list were the counted edges will be stored
    counted_edges = []
                                 
    # Iterate over every key in edgelist
    for key, value in Counter(edgelist).items():
        source = key[0]
        target = key[1]
        weight = value
        counted_edges.append((source, target, weight))
     
    # Create data frame containing the occurrences                             
    edges_df = pd.DataFrame(counted_edges, columns=["nodeA", "nodeB", "weight"])
                                 
                                 
    """
    ----------- Filter based on edgeweight -----------
    """                                 
    
    edgeweight = args["edgeweight"]
                                 
    filtered = edges_df[edges_df["weight"]edgeweight]                             
                                 
                                 
    """
    ----------- Create network -----------
    """                                
    # Create a graph object called G
    G=nx.from_pandas_edgelist(filtered, 'nodeA', 'nodeB', ["weight"])
                               
    # Plot it
    pos = nx.nx_agraph.graphviz_layout(G, prog="neato")                             
                                 
    nx.draw(G, pos, with_labels=True, node_size=20, font_size=10)
    
    # Save the vizualization in the viz folder                             
    plt.savefig("viz/network.png", dpi=300, bbox_inches="tight")  
                                 

    """
    ----------- Centrality measures -----------
    """                              
    
    # Find the eigenvector centrality                            
    ev = nx.eigenvector_centrality(G)                             
    
    # Make df with the eigenvector centrality                              
    ev_df = pd.DataFrame(ev.items())
                                 
    # Find betweenness centrality
    bc = nx.betweenness_centrality(G)                             
                                 
    # Make df with the betweenness centrality
    bc_df = pd.DataFrame(bc.items())                             
                                 
    # Merge the three data frames into one
                                 
                                 
                                 
#Define behaviour when called from command line
if __name__ == "__main__":
    main()

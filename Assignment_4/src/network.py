#!/usr/bin/env python
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
    ap.add_argument("-i", "--path", default = "../data/king_james_bible.csv", help="Path to data folder")  
        
    args = vars(ap.parse_args())
    
    """
    ------ Read data to dataframe ------
    """
    
    # Only make a df if the file is a csv file and have a column called 'text'
    filepath = args["path"]
                                 
    if filepath.endswith(".csv"): 
        data = pd.read_csv(filepath)
        if 'text' in data.columns:
            # Make a df with the data
            data_df = pd.DataFrame(data)
    else:
        print("The file needs to be a csv file and have a column called 'text'")                                                                                                        
    
    """
    ----- Extract all named entities ------
    """
    
    # Create empty list were the entities will be stored
   text_entities = []

    for text in tqdm(data_df["text"]):
        # create temporary list 
        tmp_entities = []
        # create doc object
        doc = nlp(text)
        # for every named entity
        for entity in doc.ents:
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
    
                                 
    filtered = edges_df[edges_df["weight"]>500]                            
                                 
                                 
    """
    ----------- Create network -----------
    """                                
    # Create a graph object called G
    G = nx.from_pandas_edgelist(filtered, "nodeA", "nodeB", ["weight"])
                               
    # Plot it                                                      
    fig = nx.draw_random(G, with_labels=False, node_size=20, font_size=10)
    
    # Save the vizualization in the viz folder   
    viz_output = os.path.join("..", "viz", "network.png")                             
    plt.savefig(viz_output, dpi=300, bbox_inches="tight")  
                                 

    """
    ----------- Centrality measures -----------
    """                              
    
    # Find the eigenvector centrality                            
    ev = nx.eigenvector_centrality(G)                            
    
    # Make df with the eigenvector centrality                              
    ev_df = pd.DataFrame(ev.items(), columns=["nodeA", "eigenvector"])
                                 
    # Find betweenness centrality
    bc = nx.betweenness_centrality(G)                             
                                 
    # Make df with the betweenness centrality
    bc_df = pd.DataFrame(bc.items(), columns=["nodeA", "betweenness"])   
                                                                                                         
    # Merge the three data frames into one
    measure_df = pd.merge(bc_df, ev_df, how="inner", on=["nodeA"])
    measure_df = pd.merge(measure_df, filtered, how="inner", on=["nodeA"])
    
    # Save the merged df as a csv in the output folder                             
    df_output = os.path.join("..", "output", "measure.csv") 
    measure_df.to_csv(df_output)
                                 
    print("DONE, the vizualization is located in the 'viz' folder and the csv is located in the 'output' folder")                           
                                 
#Define behaviour when called from command line
if __name__ == "__main__":
    main()

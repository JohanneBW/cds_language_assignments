#!/usr/bin/env python

"""
---------- Import libraries ----------
"""

# system tools
import os
import sys
sys.path.append(os.path.join(".."))

# pandas, numpy, gensim
import pandas as pd
import numpy as np
import gensim.downloader

# import classifier utility functions
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit
from sklearn import metrics
from sklearn.metrics import classification_report

# tools from tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, Embedding, 
                                     Flatten, GlobalMaxPool1D, Conv1D)
from tensorflow.keras.optimizers import SGD, Adam
#from tensorflow.keras import backend as K
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.regularizers import L2

# matplotlib
import matplotlib.pyplot as plt


"""
---------- Functions ----------
"""    
def plot_history(H, epochs):
    """
    Utility function for plotting model history using matplotlib
    H: model history 
    epochs: number of epochs for which the model was trained
    """
    plt.style.use("fivethirtyeight")
    plt.figure()
    plt.plot(np.arange(0, epochs), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, epochs), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, epochs), H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.show()
    fig.savefig("../output/LR_performance.png")
    
def create_embedding_matrix(filepath, word_index, embedding_dim):
    """ 
    A helper function to read in saved GloVe embeddings and create an embedding matrix

    filepath: path to GloVe embedding
    word_index: indices from keras Tokenizer
    embedding_dim: dimensions of keras embedding layer
    """
    vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
    embedding_matrix = np.zeros((vocab_size, embedding_dim))

    with open(filepath) as f:
        for line in f:
            word, *vector = line.split()
            if word in word_index:
                idx = word_index[word] 
                embedding_matrix[idx] = np.array(
                vector, dtype=np.float32)[:embedding_dim]
    return embedding_matrix

"""
---------- Main function ----------
"""

def main():
  
    """
    ---------- Read data ----------
    """
    # Read the data into a pandas data frame
    filepath = os.path.join("..", "data", "Game_of_Thrones_Script.csv")
    df = pd.read_csv(filepath)
    # Make a df with the two columns: season and sentence from the original data set
    df = df[["Season", "Sentence"]]
    sentence = df['Sentence'].values
    season = df['Season'].values
    
    """
    ---------- Train, split and vectorize data ----------
    """
    # Train and test split using sklearn
    X_train, X_test, y_train, y_test = train_test_split(sentence, 
                                                    season, 
                                                    test_size=0.25, 
                                                    random_state=42)
    # Vectorize using sklearn
    vectorizer = CountVectorizer()
    
    # First we do it for our training data...
    X_train_feats = vectorizer.fit_transform(X_train)
    #... then we do it for our test data
    X_test_feats = vectorizer.transform(X_test)
    # We can also create a list of the feature names. 
    feature_names = vectorizer.get_feature_names()
    
    """
    ---------- Logistic regression classifier ----------
    """
    # Logistic regression classifier
    classifier = LogisticRegression(random_state=42).fit(X_train_feats, y_train)
    # Define the y_predict
    y_pred = classifier.predict(X_test_feats)
    # Evaluate
    classifier_metrics = metrics.classification_report(y_test, y_pred)
    print(classifier_metrics)
    # Plot the data 
    clf.plot_cm(y_test, y_pred, normalized=True)

    # Vectorize full dataset
    X_vect = vectorizer.fit_transform(sentence)

    # Initialise cross-validation method
    title = "Learning Curves (Logistic Regression)"
    cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

    # Run on data
    model = LogisticRegression(random_state=42)
    # Plot the learning curve
    clf.plot_learning_curve(model, title, X_vect, season, cv=cv, n_jobs=4)
    # Save image in output folder
    plt.savefig("../output/LR_CrossValidation.png")
    
#Define behaviour when called from command line
if __name__ == "__main__":
    main() 

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
  fig = plt.figure()
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
  fig.savefig("../output/DL_performance.png")
  
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
        embedding_matrix[idx] = np.array(vector, dtype=np.float32)[:embedding_dim]
     
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
    # Train and test split using sklearn. X is the data, so in this case the scentences and y is the labels which is the season.
    X_train, X_test, y_train, y_test = train_test_split(sentence, 
                                                    season, 
                                                    test_size=0.25, # We split the data in 75% training and 25% test
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
    ---------- Deep learning model ----------
    """
    # Factorize the labels from a string to a number 
    y_train = pd.factorize(y_train)[0]
    y_test = pd.factorize(y_test)[0]
    
    # Word embeddings

    # Initialize tokenizer
    tokenizer = Tokenizer(num_words=5000) #we use this to get all the full scentences 
    # Fit to training data
    tokenizer.fit_on_texts(X_train)

    # Tokenized training and test data
    X_train_toks = tokenizer.texts_to_sequences(X_train)
    X_test_toks = tokenizer.texts_to_sequences(X_test)

    # Overall vocabulary size
    vocab_size = len(tokenizer.word_index) + 1  # Adding 1 because of reserved 0 index

    # Inspect it
    print(X_train[2])
    print(X_train_toks[2])
    
    # Padding
    # Max length for a doc
    maxlen = 100

    # Pad training data to maxlen
    X_train_pad = pad_sequences(X_train_toks, 
                                padding='post', # sequences can be padded "pre" or "post"
                                maxlen=maxlen)
    # Pad testing data to maxlen
    X_test_pad = pad_sequences(X_test_toks, 
                               padding='post', 
                               maxlen=maxlen)
    # Use the Regularization model
    l2 = L2(0.0001)

    # Set the embedding dimension to 50
    embedding_dim = 50
    # Create embedding_matrix
    embedding_matrix = create_embedding_matrix('data/glove.6B.50d.txt',
                                               tokenizer.word_index, 
                                               embedding_dim)
    # New model
    model = Sequential()

    # Embedding -> CONV+ReLU -> MaxPool -> FC+ReLU -> Out
    model.add(Embedding(vocab_size,                  # Vocab size from Tokenizer()
                        embedding_dim,               # Embedding input layer size
                        weights=[embedding_matrix],  # Pretrained embeddings
                        input_length=maxlen,         # Maxlen of padded doc
                        trainable=True))             # Trainable embeddings
    model.add(Conv1D(128, 5, 
                    activation='relu',
                    kernel_regularizer=l2))          # L2 regularization 
    model.add(GlobalMaxPool1D())
    model.add(Dense(10, activation='relu', kernel_regularizer=l2))
    model.add(Dense(1, activation='softmax'))        # We use the softmax activations because we have multiple labels

    # Compile the model
    model.compile(loss='categorical_crossentropy',   # We use the categorical_crossentropy because we have multiple labels
                  optimizer="adam",
                  metrics=['accuracy'])

    # Print the summary
    model.summary()
    
    # Create history of the model
    history = model.fit(X_train_pad, y_train,
                    epochs=20,
                    verbose=False,
                    validation_data=(X_test_pad, y_test),
                    batch_size=10)

    # Evaluate the model 
    loss, accuracy = model.evaluate(X_train_pad, y_train, verbose=False)
    print("Training Accuracy: {:.4f}".format(accuracy))
    loss, accuracy = model.evaluate(X_test_pad, y_test, verbose=False)
    print("Testing Accuracy:  {:.4f}".format(accuracy))

    # Plot the history
    plot_history(history, epochs = 20)
    
    # Create predictions an print the classification report
    predictions = model.predict(X_test_pad, batch_size = 10)
    print(classification_report(y_test, predictions.argmax(axis=1)))

#Define behaviour when called from command line
if __name__ == "__main__":
    main() 

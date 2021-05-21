#!/usr/bin/env python

"""
---------- Import libraries ----------
"""
import os
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import datetime

from spacytextblob.spacytextblob import SpacyTextBlob

# initialise spacy
nlp = spacy.load("en_core_web_sm")
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

"""
---------- Main function ----------
"""
def main():    
    
    """
    ---------- Filepaths ----------
    """
    # Defining the filepath where the data file is located
    filepath = os.path.join("..","data","abcnews-date-text.csv")
    # Defining the filepath were the data is going to be stored
    df_path = os.path.join("..", "output", "sentiment_df.csv")
    # Defining the filepath were the 1 week average plot is going to be stored
    week_path = os.path.join("..", "output", "week_plot.png")
    # Defining the filepath were the 1 month average plot is going to be stored
    month_path = os.path.join("..", "output", "month_plot.png")
    
    # I use a pandas data frame to get an overview of the data
    data_df = pd.read_csv(filepath)
    # I use head() to take a look at the data in the data frame  
    data_df.head(5)
    

    """
    ---------- Sentiment Score ----------
    """
    # Create empty list where the sentiment scores will be saved
    polarity = []
    
    # Create for loop that loops over all the headlines and calculates the sentiment
    for doc in nlp.pipe(data_df["headline_text"]):
        # For every sentence calculate sentiment by adding polarity and subjectivity
        for sentence in doc.sents:
            polarity_score = sentence._.sentiment.polarity
            # Ad the scores to the lists
            polarity.append(polarity_score)

    # Adding the polarity to a coloumn in the data frame
    # I could not add the list directly, but when I convert it to series it works
    polarity_values = pd.Series(polarity) 
    #I use pandas insert feature where loc is set to 0 as it is at this position where I want the values to start
    data_df.insert(loc=0, column="polarity", value=polarity_values)
    
    # Save the updated data_df as a csv file
    data_df.to_csv(df_path)
    
    """
    ---------- Updated data frame ----------
    """   
    # Read the csv file containing the data frame
    sentiment_df = pd.read_csv(df_path)
    # Overwrite the data frame so it only contains the columns publish_date and polarity
    sentiment_df = sentiment_df[["publish_date","polarity"]]
    # Convert the publish_date into date time format (year, month, day)
    sentiment_df["publish_date"] = pd.to_datetime(sentiment_df["publish_date"],format = "%Y%m%d")
    
    """
    ---------- 1 week average plot ----------
    """       
    # I group all the dates so there is one mean value for each date.
    day_by_day = sentiment_df.groupby("publish_date")["polarity"].mean()
    # I now plot the rolling mean at weekly intervals. I do this by making the windowsize 7 (because there is 7 days in a week)
    plt.plot(day_by_day.rolling(7).mean())
    # add title
    plt.title("Sentiment over time with a 1 week rolling average")
    # add label to x-axis
    plt.xlabel("Publishing date")
    # add label to y-axis
    plt.ylabel("Sentiment score")
    # save the plot(output folder)
    plt.savefig(week_path)
    # show the plot 
    plt.show()
    
    
    """
    ---------- 1 month average plot ----------
    """     
    # I now plot the rolling mean at weekly intervals. I do this by making the windowsize 30. 30 days = 1 month-ish
    plt.plot(day_by_day.rolling(30).mean())
    # add title
    plt.title("Sentiment over time with a 1 month rolling average")
    # add label to x-axis
    plt.xlabel("Publishing date")
    # add label to y-axis
    plt.ylabel("Sentiment score")
    # save the plot(output folder)
    plt.savefig(month_path)
    # show the plot
    plt.show()

    
#Define behaviour when called from command line
if __name__ == "__main__":
    main()

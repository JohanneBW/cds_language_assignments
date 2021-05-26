## Assignment 3 - Sentiment Analysis 
**Johanne Brandhøj Würtz**

__Contribution__

I didn’t work with others on this assignment.

__Assignment description__

In this assignment we will calculate the sentiment score for every headline in the data using a diction-ary-based sentiment analysis. We will create and plot sentiment over time with a 1-week and 1-month rolling average. The data is news headlines published over a period of eighteen years from the Austral-ian news source ABC. The data has about two hundred articles per day. 

__Methods__ 

For this Assignment I made a sentiment analysis based on polarity using SpaCy and SpaCy Text Blob.  Polarity is calculated based on a range between -1 and 1. It is this scale that determines whether the text is polarized or not, where -1 corresponds to a negative statement and 1 corresponds to a posi-tive statement. A polarity close to 0 will is neutral on the polarity scale. I used Datetime along with Matplotlib for creating the weekly and the monthly rolling average plots.  

__Usage__

_Structure:_
The repository contains the folders data, src and output. Before you run the script you have to download the data to the data folder in order for the paths in the script to work. The data can be found here: https://www.kaggle.com/therohk/million-headlines. The src folder contains the script sentiment.py and the output folder contains the two plots, one with a weekly rolling average and one with a monthly lolling average. 

I have created a bash script that creates and activates a virtual environment, retrieves necessary librar-ies from the requirements.txt file and runs the script for the assignment.


## How to run
**Step 1: Clone repo**
- Open terminal
- Navigate to destination you want the repo
- type the following command
 ```console
 git clone https://github.com/JohanneBW/cds_language_assignments.git
 ```
**step 2: Set up enviroment and run program:**
- Navigate to the folder "Assignment_3".
```console
cd cds_language_assignments
cd Assignment_3
```  
- Use the bash script _run_assignment3.sh_ to run the programs and set up environment:  
```console
bash run_assignment3.sh
```  
__Discussion of results__

As mentioned before, the polarity is calculated based on a range between -1 and 1. It is this scale that determines whether the text is polarized or not. The reason why the polarity values are so close to zero may be due to some different parameters. First and foremost, it may be because we work with averag-es through the calculation. First, we calculated the average for a day based on all the headlines pub-lished on the same date. Then we calculated the average for a whole week. Seen in connection with the fact that the data itself originates from newspaper headlines, there may be a connection between the polarity values being close to 0 and the content. The headlines come from the Australian news source ABC. ABC is owned and funded by the Australian Government, and one is therefore inclined to be-lieve that objectivity is weighted higher than clickbait. This means that the headings should be just around 0, which is neutral on the polarity scale, rather than high variation in positive and negative po-larization. Had the data, on the other hand, originated from a more sensation-based source, the results would most likely have looked different. 


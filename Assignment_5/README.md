## Assignment 5 - (Un)supervised machine learning
**Johanne Brandhøj Würtz**

__Contribution__

I work with Emil Buus Thomsen, Christoffer Mondrup Kramer and Rasmus Vesti Hansen in this assignment. All contributed equally to every stage of this project. Subsequently, I have modified and corrected the code myself in relation to in-depth comments and further corrections in the code. In the coding process itself, everyone has contributed equally (25%/25%/25%/25%).

__Assignment description__

In this assignment, we have chosen to investigate whether we can find some general content trends in a dataset with information about the GameStop stock. When we went into this task, we had an expectation that it would be difficult for our LDA model to discern any human-interpretable trends. Some of the elements that cloud make it difficult for our model are the fact that the comments regarding the stock are formulated in a way that requires some pre-understanding of the context. I have no experience with stocks and therefore I was first confused by the jargon that the comments are characterized by. Some examples are “going to the moon”, “diamondhands” and “retard”. In addition, the comments are largely the same, so in terms of content there is not much variation. The goal is, to find out if the LDA model can find some various topic groups that are human-interpretable. 
 
__Methods__

We have primarily used gensim and spaCy to make our text object as well as make our LDA model. The data we have chosen for this assignment is a csv file with different comments doing the GameStop stock “explosion” in February. The text itself are comments from Reddit WallStreetBets posts. The comments are not very long, so we do not have to do a lot of data wrangling and make decisions about what should be defined as a paragraph etc. we simply use each comment as a “text”. One of the elements that has been most challenging is choosing the most optimal number of topics for our model. Although the coherence value may be high at the high number of topics, it is not significant that it is the most optimal. One of the reasons for this is that there will be more repetitions of words the more topics there are. So, if one wants to avoid this, it may be an advantage with fewer topics. When we first ran the part to find the most optimal topic number, we got the number of 7 topics to be the most optimal. But when we later in the script saw the visualization of how the topics are distributed, it became clear that they formed 3 main clusters, where the topics overlapped. For this reason, we have chosen to include three topics in the model.

__Usage__

_Structure:_
The repository contains the folders data, src, utils and output. Before running the script, you must download the csv file to the data folder for the path in the script to work optimal. The data can be found by the following link: https://www.kaggle.com/unanimad/reddit-rwallstreetbets/metadata. The data contains the csv file with the GameStop stock comments. There is a sample of the data in the folder. The utils folder contain a utility function we have used in the lessons for our CDS/Language Analytics class. We use the process_words function from our utils folder. This function takes text, nlp, bigram_mod, trigram_mod, stop_words and allowed_postags as arguments. It uses gensim to preprocess the words and uses spaCy to lemmatize and POS tag.
The src folder contain our script (GameStop_LDA.py) and our output folder contains a csv with our document-topic matrix as well as a visualization of our line plot. 

I have created a bash script that creates and activates a virtual environment, retrieves necessary libraries from the requirements.txt file and runs the script for the assignment.

__How to run:__

The following shows how to set up the virtual environment and run the script step by step.
**Step 1: Clone repo**
- Open terminal
- Navigate to destination you want the repo
- Type the following command:
```console
git clone https://github.com/JohanneBW/cds_language_assignments.git
```  
**Step 2: Set up environment and run script**
- Type the following command to navigate to the folder "Assignment_5":
```console
cd cds_language_assignments
cd Assignment_5
```
- Use the bash script run_assignment5.sh to set up environment and run the script
- Type the following command:
```console
bash run_assignment5.sh
```
__Discussion of results__

As we had expected, our model failed to group the topics in a clear human-interpretable way. The only trends captured by the model are one of the topics containing the words "money", "investment" and "stock", which relates to the same. As well as another topic that had the words "month", "day" and "hour" with which relates to time. besides these individual cases, the rest of the words in the categories are not clear in their topic. Looking at our visualization, it is also clear that there are no clear separations between our subjects. I would just like to point out again that we did not expect to achieve a successful model in relation to the data we have. This may relate to the fact that the comments are all about the same thing. If, on the other hand we had data from different stocks, our model might have succeeded better in differentiating them. But again, the lingo that characterizes the comments is probably general for the entire stock market, so the model would probably have a greater advantage in categorizing on the basis of proper names, as these largely refer to the companies and stocks involved. 


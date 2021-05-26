## Assignment 6 - Text classification using Deep Learning
**Johanne BW**

__Contribution__

I work with Emil Buus Thomsen, Christoffer Mondrup Kramer and Rasmus Vesti Hansen in this assignment. All contributed equally to every stage of this project. Subsequently, I have modified and corrected the code myself in relation to in-depth comments and further corrections in the code. In the coding process itself, everyone has contributed equally (25%/25%/25%/25%).

__Assignment description__

In this assignment we will see how successfully we can use a Logistic Regression model and Deep learning Convolutional Neural Network model to classify a specific kind of cultural data - scripts from the TV series Game of Thrones. We are going to see how accurately we can model the relationship between each season and the lines spoken. We want to find out if dialogue is a good predictor of sea-son. 

__Methods__

We primarily used Sklearn and Tensorflow in this task for our LogisticRegression model and our Convolutional Neural Network model. The challenge in this assignment was to build a CNN model for text classification as well as use pre-trained word embeddings in the form of embeddings from GloVe. In addition, it has also been a challenge to balance between research questions, approach and results. I will address this in the discussion of the results.

__Usage__

_Structure:_
The repository contains the folders data, src, utils and output. The data folder contains the csv file Game_of_Thrones_Script.csv which content is a complete set of Game of Thrones script for all sea-sons. The data can be found by the following link: https://www.kaggle.com/albenft/game-of-thrones-script-all-seasons. The src folder contains the two scripts LRModel.py and DLModel.py. The LRModel.py script uses a Logistic Regression model and the DLModel.py uses a Convolutional Neu-ral Network model. The utils folder contains utility functions we have used in the lessons for our CDS/Language Analytics class. The output folder contains the visualization of the LR and DL models performances. 

I have created a bash script that creates and activates a virtual environment, retrieves necessary librar-ies from the requirements.txt file and runs the script for the assignment. We use pretrained GloVe embedding for the assignment and these will be downloaded through the bash script


## How to run
**Step 1: Clone repo**
- Open terminal
- Navigate to destination you want the repo
- type the following command
 ```console
 git clone https://github.com/JohanneBW/cds_language_assignments.git
 ```
**step 2: Set up enviroment, download pretrained embeddigs and run program:**
- Navigate to the folder "Assignment_6".
```console
cd cds_language_assignments
cd Assignment_6
```  
- Use the bash script _run_assignment6.sh_ to run the programs, download pretrained embeddigs and set up environment:  
```console
bash run_assignment6.sh
```  
__Discussion of results__

We wanted to answer whether dialogue is a good indicator of the seasons. To this we must answer no, it can certainly not be said that it is. When we discussed this, we came up with several things that could influence this. First of all, the data contains all the lines said in the whole series and that's quite a lot. if we instead chose to focus on some key figures, there might be more characteristics for each season to trace in the lines. Another aspect that could affect the result is the size of the text bits we define. Here, instead of looking at the individual lines or the individual sentences, one could look at larger pieces of text, as this can have an influence on how the models find characteristics. One of the best possible ways to distinguish the seasons must be to look at the characters, as there is great variation in which characters are in the different seasons. Here, however, we end up quite far from what we wanted to answer in the first place. Although some elements can be modified, the question arises again about how much one can afford to modify to get the desired result. This must be seen in relation to the data we work with and the question or questions we want answered. If we instead wanted to answer how best to distinguish the seasons, it is a completely different task we are interested in. It is worth bearing in mind that it is all about compromises between data, research questions, approaches and results.

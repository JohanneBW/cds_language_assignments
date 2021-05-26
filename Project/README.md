## Project - Character network in Pulp Fiction
**Johanne Brandhøj Würtz**

__Contribution__

I didn’t work with others on this assignment.

__Assignment description__

For this assignment I was inspired by the text “Social network analysis in a movie using character-net” by S. Park et al. from 2011 who has done a character-net analysis of films. The article deals with how they, with the help of network analysis on the basis of both script, subtitles and image reading, manage to create a new form of network analysis called character-net. The article can be found by the following link: https://link-springer-com.ez.statsbiblioteket.dk:12048/article/10.1007/s11042-011-0725-1. In my project, I intend to use the elements from their analysis where they use the film script to track the network between the characters in the film. My research question is therefore: is it possible to trace the character network in the 1994 film Pulp Fiction based on the dialogue in the film script?

__Methods__

To answer my research question, I do a network analysis based on the characters appearing together in pairs throughout the film. The characters and thus the nodes I use in the analysis I find using SpaCy and the network is made with NetworkX. One of the things I have had to do to be able to connect the dialogues is to tie the line itself together with the character. This would not be necessary if it was a book or similar, where one knows who says what because it is implemented in the text itself, but since I am dealing with a manuscript there is no other indication of who says the line as it is not explicitly expressed in the line itself. 
When looking at the text, the lines in the script, it is worth bearing in mind that dialects are 'written out'. An example of this is the fifth line in the script where the words forgittin' and remem-berin' appears. This also affects the node pairs along with the swearwords. Examples of this is "ta fuck", "Motherfucker" and "dont' ya" which are defined as persons by the SpaCy labels. These does not appear in the pairs often enough to conflict with the network analysis, but it is a clear example of an issue using a SpaCy library on a film script known for its slang and rough language. 
If you look at the two centrality measures, betweenness and eigenvector, there is a dif-ference in how these looks in relation to the network. Betweenness is the measure that shows which nodes are bridges between the nodes in the network. It identifies all the shortest paths and the counts how many times each node falls on one. Eigenvector measures a node’s influence based on the num-ber of links it has to other nodes in the network but is also taking into account how well connected a node is. Said in other words, eigenvector can identify nodes with influence over the whole network, not just those directly connected to it. These results seen in the light of the network I will elaborate on later. 

__Usage__

_Structure:_
The repository contains the folders data, src and output. The data folder contains the csv file with the film script. The data containing the film manuscript can be found by the following: https://www.kaggle.com/matiaswargelin/pulp-fiction-script-dialogue.  The src folder contains the script PulpFiction_network.py where the network and the centrality measures are created. The output folder contains a visualization of the network along with two csv files. One with centrality measures based on betweenness and eigenvector and one with the number of lines per character. 

I have created a bash script that creates and activates a virtual environment, retrieves necessary librar-ies from the requirements.txt file and runs the script for the assignment.

## How to run
**Step 1: Clone repo**
- Open terminal
- Navigate to destination you want the repo
- type the following command
 ```console
 git clone https://github.com/JohanneBW/cds_language_assignments.git
 ```
**Step 2: Set up enviroment and run program:**
- Navigate to the folder "Project".
```console
cd cds_language_assignments
cd Project
```  
- Use the bash script _run_project.sh_ to run the programs, download pretrained embeddigs and set up environment:  
```console
bash run_project.sh
```
__Discussion of results__

In relation to my research question: is it possible to trace the character network in the 1994 film Pulp Fiction based on the dialogue in the film script? To answer this, I will discuss the various results that the network as well as the centrality measures showed. In the betweenness score it is Wolf, Jules and Vincent who score the highest. So, these are the ones that act as bridges between the characters in the film. If we look at eigenvector instead, we get a different result. In the eigenvector score it is instead Wolf, Jimmie and Uncle Conrad who score the highest. If one looks at the visualization of the network, one can see roughly the same trends. Here are three main groups, where it is Jules, Vincent, Mia, Jimmie and Wolf who connect the groups with each other. It is also clear to see that each bridge plays different roles. If we look at Jules and Vincent, they are the characters that connect the groups with each other. Mia, Jimmie and Wolf, on the other hand, are the ones who have the most connec-tions to other characters.
	It is interesting that the main characters scores high on the betweenness centrality, but not on the eigenvector score. The characters with most lines are not necessarily the most important in the network. A good example of this is the character Butch played by Bruce Willis. He has 135 lines in the film (third most), but his history is like a side story to the main story. Therefore, he does not communicate a lot with the other main characters and scores low on the centrality measures. Jimmie on the other hand does only have 26 lines but scores highest on the eigenvector centrality score. One as-pect that has an impact on the network are nicknames, as they do not match the names that the characters have. Here are two examples of this with the characters Jules and Vincent, who sometimes throughout the film are called Julie and Vince. The network considers Julie and Vince as other charac-ters. Since the nicknames are only used for the recipient, that is, a character can talk to one and use the nickname, but the nickname does not respond back. I have chosen not to change them to the charac-ter's real name, as I can see who uses the nicknames and whether it has an impact on the network. Here one sees that it is Mia who calls Vincent Vince, as she is the only character associated with the nickname. Similarly, we can see that it is Jimmie who calls Jules Julie. It is worth bearing in mind that the places where nicknames are used affect the network a bit. Jimmie and Mia have got an extra connec-tion even though in reality it should also be Jules and Vincent who got their scores strengthened. 
I would conclude that one can well trace a network between film characters based on dialogue. The most interesting thing I have found out is that it is not necessarily the characters with the most lines that bind the film together in relation to the characters. One of the elements that is worth including is that in this analysis I only focused on dialogue, where both sender and receiver are mentioned in the lines. It might be interesting to examine the text in a different way, where one might focus on an entire scene instead of the individual lines, as this would give some other interesting results.


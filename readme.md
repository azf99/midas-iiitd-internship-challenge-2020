# Reddit Flair Detection
(Task by MIDAS Lab@IIITD for Summer Internship 2020)


A project to scrape, analyze, perform modeling and deploying the ML model online on heroku.

### Contents and Intallation:

1. data/ : folder containing the raw and preprocessed data files in CSV

2. models/ : folder with the classifier model and the label encoder as pickle files

3. templates/ : folder containing the HTML templates for the webapp

4. Jupyter Notebooks: Three notebooks with the code for Data Collection, Analysis and Modeling

5. app.py : The main file with the Flask app architecture

6. utils.py : The file containing all the dependency methods for app.py, for fetching, processing and predicting the data

7. Procfile : For Heroku to define the app as a webapp

8. nltk.txt : Again for Heroku to download all the nltk dependencies

9. requirements.txt : contains all the necessary python packages and versions for installation

Prequisites:- Python 3 and pip should be installed

To install:
1. Clone the repository

2. Go into the cloned repo path and run:
	pip3 install -r requirements.txt
 
3. Go ahead and start the server with:
	python3 app.py


## PART 1: Data Collection
By, primarily the use of the PRAW API in python.

Reference: https://www.storybench.org/how-to-scrape-reddit-with-python/


## PART 2:  Exploratory Data Analysis
Detailed analysis can be found in the notebook [here](https://github.com/azf99/midas-iiitd-internship-challenge-2020/blob/master/Part%202-%20Exploratory%20Data%20Analysis.ipynb)

## PART 3: Modeling for predicting flair of a post

Approach

The final corpus that we are going to be using for modelling will be a combination of the title, body and top 20 comments of each post.

I decided use all of this data because, I saw, during the EDA, that for some flairs, there was inconsistency in the lenth of title body of the posts. For eg.: Most of the posts in the flairs "Photography" and "Sports" didn't have much text in the body, so using only body as a feature would result in less features being extracted.

Finally I moved forward with the corpus. I tried 5 ML Classification Algorithms on different combinations of data by using the following:

    Term Frequency-Inverse Document Frequency(TF-IDF)
    Count Vectorization

The algorithms I will use:

    Logistic Regression
    Random Forest
    Support Vector Classifier
    Naive Bayes
    A Multi-Layer Perceptron

For different types of data, I'll train all the 5 Algorithms on them, just to assess which one will work better

I also thought if I used other text features, like the length of both the title and body, maybe it will improve accuray, because in the original data also, there were dicrepancies over posts of different flairs. But that didn't give any better results, so I scrapped the idea.

Finally selected: Support Vector Classifier with TF-IDF scores.

Best parameters = {'gamma': 'scale', 'kernel': 'linear'}
Results:

              precision    recall  f1-score   support

           0       0.97      0.98      0.97        58
           1       0.52      0.32      0.39        95
           2       0.53      0.56      0.54        55
           3       0.63      0.69      0.66        58
           4       0.25      0.23      0.24        78
           5       0.74      0.78      0.76        51
           6       0.46      0.42      0.44        62
           7       0.50      0.51      0.50        51
           8       0.92      0.91      0.92        67
           9       0.49      0.46      0.48        74
          10       0.66      0.93      0.77        40
          11       0.33      0.59      0.42        32

    accuracy                           0.58       721
    macro avg      0.58      0.62      0.59       721
    weighted avg   0.58      0.58      0.57       721

Label Meanings:
0 : AMA
1 : AskIndia
2 : Business/Finance
3 : Food
4 : Non-Political
5 : Photography
6 : Policy/Economy
7 : Politics
8 : Scheduled
9 : Science/Technology
10 : Sports
11 : [R]eddiquette


#### Pros:
1. The model works pretty accurately in predicting Politics, Sports and Science/Tech, maybe because the contents are very different from each other.
2. Its fast at the same time, no being a deep learning model
3. It acheived a satisfactory amount of accuracy, even with such less amount of data, around 200 posts per flair

#### Cons:
1. The model often gets confused between AskIndia and AMA because posts in both the flairs have the same motive
2. It also predicts wrong for some particular flairs only, beacuse of not having sufficient amount of text in each of the posts. 

### Future Scope:
One idea, I got very late was that, if we preprocessed the text based on the stopwords and trends of different flairs separately, we would have been able to filter out more noise, which would in return help in increasing the accuracy.


## PART 4: Deployment

App succesfully deployed on heroku: https://reddit-flair-azf99.herokuapp.com/

Link for the sending a text file with post links: https://reddit-flair-azf99.herokuapp.com/automated_testing

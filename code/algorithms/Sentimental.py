import pandas as pd
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# Import the dataset training of imdb
reviews = pd.read_csv("../../datasets/imdb-reviews-pt-br.csv")

#Pre processing
#Replace neg and pos to 0 and 1
classification = reviews["sentiment"].replace(["neg","pos"], [0,1])
reviews["classification"] = classification

def sentimentalAnalyses(text, text_column, classification_column):
    #Creating a bag of words
    #Limit of 50 features by bag.
    vectorizer = CountVectorizer(max_features=150)
    bag_of_words = vectorizer.fit_transform(text[text_column])

    # Split the dataset in training and test dataset
    training, test, class_training, class_test = train_test_split(bag_of_words, text[classification_column], random_state=60)
    exampler = vectorizer.fit_transform(example)

    teste2 = sklearn.model_selection.train_test_split(exampler)
    #Vector size of bag
    #print(bag_of_words.shape)

    # Make the training
    lr = LogisticRegression()
    lr.fit(training, class_training)
    print(teste2)

    prediction = lr.predict(np.array(teste2).reshape(-1, 1))
    print(classification_report(class_test,prediction))

    return  lr.score(test,class_test)


print(sentimentalAnalyses(reviews, "text_pt", "classification"))
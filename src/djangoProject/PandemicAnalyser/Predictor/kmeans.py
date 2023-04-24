from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from PandemicAnalyser.Predictor.modeldata import *

train = get_train()
test = get_test()


##### K-Means Clustering ####

vectorizer = CountVectorizer() # initialize vectorizer to transform training and test sets to matrices

train_text = []
for data in train: # iterate over training data and add it to list to be transformed to matrix
    train_text.append(data[0]) # just use the text part of the tuple, which is first value, hence data[0]

X_train = vectorizer.fit_transform(train_text) # convert the training data to a matrix

kmeans = KMeans(n_clusters=2) # 2 clusters has the best performance
kmeans.fit(X_train) # train K-means model

test_text = []
for data in test: # iterate over test data to add to list which will be transformed to matrix
    test_text.append(data[0]) # add all text values without the pos or neg values to an array

X_test = vectorizer.transform(test_text) # transform intro matrix
predicted_labels = kmeans.predict(X_test) # predict clusters from test data

scores = []
for data in test: # iterate over data in test and add scores to list
    if data[1] == "pos":
        scores.append(1)
    else:
        scores.append(0)

correct = 0
i = 0
while i < len(predicted_labels):
        #print(str(predicted_labels[i]) + " " + str(scores[i]))
        if predicted_labels[i] == scores[i]: # if value correctly predicted ( the values are equal)
                correct += 1 # if correct prediction add 1 to counter
        i += 1

accuracy = (correct / len(predicted_labels))
#print("\nOVERALL K-means ACCURACY: " + str(accuracy))

def get_km_accuracy():
        vectorizer = CountVectorizer()  # initialize vectorizer to transform training and test sets to matrices

        train_text = []
        for data in train:  # iterate over training data and add it to list to be transformed to matrix
                train_text.append(data[0])  # just use the text part of the tuple, which is first value, hence data[0]

        X_train = vectorizer.fit_transform(train_text)  # convert the training data to a matrix

        kmeans = KMeans(n_clusters=2)  # 2 clusters has best performance
        kmeans.fit(X_train)  # train K-means model

        test_text = []
        for data in test:  # iterate over test data to add to list which will be transformed to matrix
                test_text.append(data[0])  # add all text values without the pos or neg values to an array

        X_test = vectorizer.transform(test_text)  # transform intro matrix
        predicted_labels = kmeans.predict(X_test)  # predict clusters from test data

        scores = []
        for data in test:  # iterate over data in test and add scores to list
                if data[1] == "pos":
                        scores.append(1)
                else:
                        scores.append(0)

        correct = 0
        i = 0
        while i < len(predicted_labels):
                if predicted_labels[i] == scores[i]:  # if value correctly predicted ( the values are equal)
                        correct += 1  # if correct prediction add 1 to counter
                i += 1

        accuracy = (correct / len(predicted_labels))

        return accuracy

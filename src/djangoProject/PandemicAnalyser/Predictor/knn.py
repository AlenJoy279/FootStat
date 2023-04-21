from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from PandemicAnalyser.Predictor.modeldata import *

train = get_train()
test = get_test()

##### K-Nearest Neighbour Clustering ###
vectorizer = CountVectorizer()

trainx_text = []
train_y = []
for data in train: # iterate over training data and add it to list to be transformed to matrix
    train_y.append(data[1]) # score is data[1] which is either 'neg' or 'pos'
    trainx_text.append(data[0]) # tweet text data is [0]

train_x = vectorizer.fit_transform(trainx_text) # transform train data into matrix for clustering

test_text = []
for data in test: # iterate over test data to add to list which will be transformed to matrix
    test_text.append(data[0]) # add all text values without the pos or neg values to an array

test_x = vectorizer.transform(test_text) # transform test data into matrix for clustering

model = KNeighborsClassifier(n_neighbors=2)
model.fit(train_x, train_y) # train KNN

# Use the model to predict the sentiment of the test data
test_y = model.predict(test_x)

correct = 0
i = 0
while i < len(test):
        #print(str(test_y[i]) + " " + str(test[i][1]))
        if test_y[i] == test[i][1]:
                correct += 1 # if correct add counter to total correctly predicted values
        i += 1

knnaccuracy = correct / len(test) # total accuracy = correctly predicted values / total values

#print("\nOVERALL KNN ACCURACY:" + str(knnaccuracy))

def get_knn_accuracy():
        vectorizer = CountVectorizer()

        trainx_text = []
        train_y = []
        for data in train:  # iterate over training data and add it to list to be transformed to matrix
                train_y.append(data[1])  # score is data[1] which is either 'neg' or 'pos'
                trainx_text.append(data[0])  # tweet text data is [0]

        train_x = vectorizer.fit_transform(trainx_text)  # transform train data into matrix for clustering

        test_text = []
        for data in test:  # iterate over test data to add to list which will be transformed to matrix
                test_text.append(data[0])  # add all text values without the pos or neg values to an array

        test_x = vectorizer.transform(test_text)  # transform test data into matrix for clustering

        model = KNeighborsClassifier(n_neighbors=2)
        model.fit(train_x, train_y)  # train KNN

        # Use the model to predict the sentiment of the test data
        test_y = model.predict(test_x)

        correct = 0
        i = 0
        while i < len(test):
                if test_y[i] == test[i][1]:
                        correct += 1  # if correct add counter to total correctly predicted values
                i += 1

        knnaccuracy = correct / len(test)  # total accuracy = correctly predicted values / total values

        return knnaccuracy
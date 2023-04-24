from textblob import TextBlob
from textblob.classifiers import DecisionTreeClassifier
from PandemicAnalyser.Predictor.modeldata import *

train = get_train()
test = get_test()

#### DECISION TREE CLASSIFIER #####
dtc = DecisionTreeClassifier(train) # train decision tree algorithm using training data

# print("\nOVERALL Decision Tree Predictor ACCURACY: " + str(dtc.accuracy(test)) + "\n") # print accuracy using test set

for s in test:
      blob = TextBlob(s[0])
      # print("BUILT-IN SENTIMENT: " + str(blob.sentiment.polarity))
      # print("DECISION TREE CLASSIFIER: " + str(dtc.classify(blob)) + "\n")

def get_dt_accuracy():
        dtc = DecisionTreeClassifier(train)  # train decision tree algorithm using training data
        print("DT ACCURACY: " + str(dtc.accuracy(test)))
        return dtc.accuracy(test)
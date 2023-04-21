import pickle
import re
import nltk
import pandas as pd
import numpy as np
import string
import json
import seaborn as sns
from matplotlib import pyplot as plt
from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from wordcloud import WordCloud




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def create_df(path):
    df = pd.read_json(path, lines=True, orient='records')
    df = df[['id', 'full_text']]
    return df


def get_sentiment_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def cleaning_stopwords(text):
    stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
                    'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before',
                    'being', 'below', 'between', 'both', 'by', 'can', 'd', 'did', 'do',
                    'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from',
                    'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
                    'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
                    'into', 'is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
                    'me', 'more', 'most', 'my', 'myself', 'now', 'o', 'of', 'on', 'once',
                    'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'own', 're', 's', 'same', 'she', "shes",
                    'should', "shouldve", 'so', 'some', 'such',
                    't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
                    'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
                    'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
                    'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
                    'why', 'will', 'with', 'won', 'y', 'you', "youd", "youll", "youre",
                    "youve", 'your', 'yours', 'yourself', 'yourselves']

    STOPWORDS = set(stopwordlist)
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

def cleaning_punctuations(text):
    english_punctuations = string.punctuation
    punctuations_list = english_punctuations
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)

def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)

def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)

def stemming_on_text(data):
    st = nltk.PorterStemmer()
    text = [st.stem(word) for word in data]
    return data

def lemmatizer_on_text(data):
    lm = nltk.WordNetLemmatizer()
    text = [lm.lemmatize(word) for word in data]
    return data


def pos_neg(polarity):
    if polarity > 0:
        return 2
    elif polarity < 0:
        return 1
    elif polarity == 0:
        return 0


def convert_to_json(file, name):
    with open(file, 'r') as f:
        data = eval(f.read())

    # Convert the data to a list of dictionaries
    data_list = []
    for d in data:
        data_list.append({"text": d[0], "label": d[1]})

    # Serialize the data to JSON
    json_data = json.dumps(data_list)

    # Write the JSON data to a file
    with open(name, 'w') as f:
        f.write(json_data)


def dataset_distro(df, title):
    # Plotting the distribution for dataset.
    ax = df.groupby('label').count().plot(kind='bar', title=f'Distribution of {title} data', legend=False)
    ax.set_xticklabels(['Positive', 'Negative'], rotation=0)

    # Storing data in lists.
    sns.countplot(x='label', data=df)
    text, label = list(train_tweet['text']), list(train_tweet['label'])

    return plt.show()

# def prep_dataset():
#


def model_evaluate(model):
    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    # Print the evaluation metrics for the dataset.
    print(unprocessed_test['label'])
    print(y_pred)
    print(classification_report(y_test, y_pred))
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    categories = ['Negative', 'Positive']
    group_names = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
    group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]
    labels = [f'{v1}n{v2}' for v1, v2 in zip(group_names, group_percentages)]
    labels = np.asarray(labels).reshape(2, 2)
    sns.heatmap(cf_matrix, annot=labels, cmap='Blues', fmt='',
                xticklabels=categories, yticklabels=categories)
    plt.xlabel("Predicted values", fontdict={'size': 14}, labelpad=10)
    plt.ylabel("Actual values", fontdict={'size': 14}, labelpad=10)
    plt.title("Confusion Matrix", fontdict={'size': 18}, pad=20)

    return plt.show()


def model_accuracy(model):
    y_pred = model.predict(X_test)

    return classification_report(y_test, y_pred, output_dict=True)['accuracy']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # convert_to_json("train.txt", "train.json")
    # convert_to_json("test.txt", "test.json")

    # Read in the train and test data as pandas frames
    train_tweet = pd.read_json("train.json")
    test_tweet = pd.read_json("test.json")

    # Map pos labels to the integer 1 and neg labels to 0
    train_tweet['label'] = train_tweet['label'].map({'pos': 1, 'neg': 0})
    test_tweet['label'] = test_tweet['label'].map({'pos': 1, 'neg': 0})

    # Data pre-processing steps (only required for graphs, word cloud etc.)
    # 1. Convert to lower case
    train_tweet['text'] = train_tweet['text'].str.lower()
    test_tweet['text'] = test_tweet['text'].str.lower()

    unprocessed_train = train_tweet[['text', 'label']]
    unprocessed_test = test_tweet[['text', 'label']]

    # 2. Remove stopwords, urls, numbers, punctuations and repeating chars
    train_tweet['text'] = train_tweet['text'].apply(lambda text: cleaning_stopwords(text))
    train_tweet['text'] = train_tweet['text'].apply(lambda x: cleaning_punctuations(x))
    train_tweet['text'] = train_tweet['text'].apply(lambda x: cleaning_repeating_char(x))
    train_tweet['text'] = train_tweet['text'].apply(lambda x: cleaning_URLs(x))
    train_tweet['text'] = train_tweet['text'].apply(lambda x: cleaning_numbers(x))

    test_tweet['text'] = test_tweet['text'].apply(lambda text: cleaning_stopwords(text))
    test_tweet['text'] = test_tweet['text'].apply(lambda x: cleaning_punctuations(x))
    test_tweet['text'] = test_tweet['text'].apply(lambda x: cleaning_repeating_char(x))
    test_tweet['text'] = test_tweet['text'].apply(lambda x: cleaning_URLs(x))
    test_tweet['text'] = test_tweet['text'].apply(lambda x: cleaning_numbers(x))

    # 3. Tokenization, stemming and lemmatization
    tokenizer = RegexpTokenizer(r'\w+')

    train_tweet['text'] = train_tweet['text'].apply(tokenizer.tokenize)
    train_tweet['text'] = train_tweet['text'].apply(lambda x: stemming_on_text(x))
    train_tweet['text'] = train_tweet['text'].apply(lambda x: lemmatizer_on_text(x))

    test_tweet['text'] = test_tweet['text'].apply(tokenizer.tokenize)
    test_tweet['text'] = test_tweet['text'].apply(lambda x: stemming_on_text(x))
    test_tweet['text'] = test_tweet['text'].apply(lambda x: lemmatizer_on_text(x))
    print(train_tweet)



    # Train a TF-IDF vectorizer on the training data
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(unprocessed_train['text'])
    y_train = unprocessed_train['label']

    # Print the shape of the feature matrix and the label vector
    print('Shape of feature matrix:', X_train.shape)
    print('Shape of label vector:', y_train.shape)

    # Transform the test data into feature vectors using the trained vectorizer
    X_test = vectorizer.transform(unprocessed_test['text'])
    y_test = unprocessed_test['label']

    print('No. of feature_words: ', len(vectorizer.get_feature_names_out()))

    # Train an LR model using the training data
    LRmodel = LogisticRegression()
    LRmodel.fit(X_train, y_train)

    pickle.dump(LRmodel, open('LRmodel.sav', 'wb'))
    dataset_distro(train_tweet, "training")
    dataset_distro(test_tweet, "test")

    # Evaluate precision, recall and F-1 scores. Display confusion matrix.
    model_evaluate(LRmodel)

    # Calculate the accuracy of the model on the test data
    print(model_accuracy(LRmodel))

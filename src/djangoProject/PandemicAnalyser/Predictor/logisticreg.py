import pickle
import re

import mpld3
import nltk
import pandas as pd
import numpy as np
import string
import json
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from wordcloud import WordCloud


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
                    'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'im', 'if', 'in',
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


def create_dfs_matrices(*args):
    # Read in the train and test data as pandas frames
    if not args:
        train_tweet = pd.read_json('PandemicAnalyser/Predictor/train.json')
        test_tweet = pd.read_json('PandemicAnalyser/Predictor/test.json')
    else:
        train_tweet = pd.read_json(args[0])
        test_tweet = pd.read_json(args[1])

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

    processed_train = train_tweet[['text', 'label']]
    processed_test = test_tweet[['text', 'label']]

    # 3. Tokenization, stemming and lemmatization
    tokenizer = RegexpTokenizer(r'\w+')

    train_tweet['text'] = train_tweet['text'].apply(tokenizer.tokenize)
    train_tweet['text'] = train_tweet['text'].apply(lambda x: stemming_on_text(x))
    train_tweet['text'] = train_tweet['text'].apply(lambda x: lemmatizer_on_text(x))

    test_tweet['text'] = test_tweet['text'].apply(tokenizer.tokenize)
    test_tweet['text'] = test_tweet['text'].apply(lambda x: stemming_on_text(x))
    test_tweet['text'] = test_tweet['text'].apply(lambda x: lemmatizer_on_text(x))

    # Train a TF-IDF vectorizer on the training data
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(unprocessed_train['text'])
    y_train = unprocessed_train['label']

    # Transform the test data into feature vectors using the trained vectorizer
    X_test = vectorizer.transform(unprocessed_test['text'])
    y_test = unprocessed_test['label']

    # Can probably train all models with these matrices in the future (if dev time allows)

    xy_train_xy_test = [X_train, y_train, X_test, y_test]

    return [train_tweet, test_tweet, processed_train, processed_test, xy_train_xy_test]


def get_wordmap():
    test_data = create_dfs_matrices()[3]

    data_pos = test_data[test_data['label'] == 1]
    data_neg = test_data[test_data['label'] == 0]

    neg_text = ' '.join(data_neg['text'].tolist())
    pos_text = ' '.join(data_pos['text'].tolist())

    # Negative wordcloud
    plt.imshow(
        WordCloud(width=800, height=800, background_color='white', max_words=100, colormap='Reds').generate(neg_text),
        interpolation='bilinear')
    plt.axis('off')
    plt.show()
    # Positive wordcloud
    plt.imshow(
        WordCloud(width=800, height=800, background_color='white', max_words=100, colormap='Reds').generate(pos_text),
        interpolation='bilinear')
    plt.axis('off')
    plt.show()


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


def get_dataset_distro():
    df = create_dfs_matrices()[0]
    # Plotting the distribution for dataset.
    ax = df.groupby('label').count().plot(kind='bar', title=f'Distribution of training data', legend=False)
    ax.set_xticklabels(['Positive', 'Negative'], rotation=0)

    # Storing data in lists.
    sns.countplot(x='label', data=df)
    text, label = list(df['text']), list(df['label'])

    return plt.show()


def get_lr_cm():
    model = pickle.load(open('PandemicAnalyser/Predictor/LRmodel.sav', 'rb'))
    train_test_matrices = create_dfs_matrices()[-1]
    X_test = train_test_matrices[2]
    y_test = train_test_matrices[3]

    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    # Print the evaluation metrics for the dataset.
    # print(y_pred)
    # print(classification_report(y_test, y_pred))
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

    html = mpld3.fig_to_html(plt.gcf())
    centered_html = f'<div style="text-align: center;">{html}</div>'

    return centered_html


def get_lr_accuracy():
    model = pickle.load(open('PandemicAnalyser/Predictor/LRmodel.sav', 'rb'))

    train_test_matrices = create_dfs_matrices()[-1]
    X_test = train_test_matrices[2]
    y_test = train_test_matrices[3]

    y_pred = model.predict(X_test)

    return classification_report(y_test, y_pred, output_dict=True)['accuracy']


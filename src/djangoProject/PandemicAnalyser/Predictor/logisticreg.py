import re

import nltk
import pandas as pd
import numpy as np
import string
import seaborn as sns
from matplotlib import pyplot as plt
from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from wordcloud import WordCloud

english_punctuations = string.punctuation
punctuations_list = english_punctuations


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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


def create_df(path):
    df = pd.read_json(path, lines=True, orient='records')
    df = df[['id', 'full_text']]
    return df


def get_sentiment_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


STOPWORDS = set(stopwordlist)


def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])


def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)


def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)


def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)


def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)


st = nltk.PorterStemmer()


def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data


lm = nltk.WordNetLemmatizer()


def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data


def pos_neg(polarity):
    if polarity > 0:
        return 2
    elif polarity < 0:
        return 1
    elif polarity == 0:
        return 0


def model_Evaluate(model):
    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    # Print the evaluation metrics for the dataset.
    print(classification_report(y_test, y_pred))
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    categories = ['Negative','Positive']
    group_names = ['True Neg','False Pos', 'False Neg','True Pos']
    group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]
    labels = [f'{v1}n{v2}' for v1, v2 in zip(group_names,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    sns.heatmap(cf_matrix, annot = labels, cmap = 'Blues',fmt = '',
    xticklabels = categories, yticklabels = categories)
    plt.xlabel("Predicted values", fontdict = {'size':14}, labelpad = 10)
    plt.ylabel("Actual values" , fontdict = {'size':14}, labelpad = 10)
    plt.title ("Confusion Matrix", fontdict = {'size':18}, pad = 20)


tokenizer = RegexpTokenizer(r'\w+')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df_path = r"F:\ca400\hydrated\no_tag2020_april1_april2.csv.jsonl"
    basename = df_path.split("\\")[-1]
    tweet = create_df(df_path)


    tweet['polarity'] = tweet['full_text'].apply(get_sentiment_score)
    tweet['sentiment'] = tweet['polarity'].apply(pos_neg)
    data = tweet[['full_text', 'sentiment']]
    data_pos = data[tweet['sentiment'] == 2]
    data_neg = data[tweet['sentiment'] == 1]
    dataset = pd.concat([data_pos, data_neg])
    dataset['full_text'] = dataset['full_text'].str.lower()
    # Data preprocessing steps
    dataset['full_text'] = dataset['full_text'].apply(lambda text: cleaning_stopwords(text))
    dataset['full_text'] = dataset['full_text'].apply(lambda x: cleaning_punctuations(x))
    dataset['full_text'] = dataset['full_text'].apply(lambda x: cleaning_repeating_char(x))
    dataset['full_text'] = dataset['full_text'].apply(lambda x: cleaning_URLs(x))
    dataset['full_text'] = dataset['full_text'].apply(lambda x: cleaning_numbers(x))
    dataset['full_text'] = dataset['full_text'].apply(tokenizer.tokenize)
    dataset['full_text'] = dataset['full_text'].apply(lambda x: stemming_on_text(x))
    dataset['full_text'] = dataset['full_text'].apply(lambda x: lemmatizer_on_text(x))
    dataset['full_text'].tail()

    # Plotting the distribution for dataset.
    ax = dataset.groupby('sentiment').count().plot(kind='bar', title='Distribution of data', legend=False)
    ax.set_xticklabels(['Positive', 'Negative'], rotation=0)
    # Storing data in lists.
    sns.countplot(x='sentiment', data=dataset)

    text, sentiment = list(dataset['full_text']), list(dataset['sentiment'])
    print(dataset.dtypes)

    X = data.full_text
    y = data.sentiment

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=26105111)
    vectoriser = TfidfVectorizer(ngram_range=(1, 2), max_features=500000)
    vectoriser.fit(X_train)
    X_train = vectoriser.transform(X_train)
    X_test = vectoriser.transform(X_test)
    print('No. of feature_words: ', len(vectoriser.get_feature_names_out()))

    LRmodel = LogisticRegression(C=2, max_iter=1000, n_jobs=-1)
    LRmodel.fit(X_train, y_train)
    model_Evaluate(LRmodel)
    y_pred3 = LRmodel.predict(X_test)

    dataset.to_csv("result.csv", sep='\t')


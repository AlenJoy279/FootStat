from PandemicAnalyser.models import Tweet
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

def select_by_date(month, year): # select tweets given a list of tweets, a month and a year
    selected_tweets = []

    for tweet in Tweet.objects.all():
        t_month = tweet.created_at[4:7]
        t_year = tweet.created_at[26:30]
        if (t_month == month) and (t_year == year):
            selected_tweets.append(tweet)
    return selected_tweets

def get_count_by_date():
    countDate = {"Feb 2020": 0, "Mar 2020":0,"Apr 2020": 0, "May 2020":0, "Jun 2020":0, "Jul 2020":0, "Aug 2020":0,
                 "Sep 2020":0, "Oct 2020": 0, "Nov 2020":0, "Dec 2020":0, "Jan 2021":0, "Feb 2021" : 0,"Mar 2021":0,
                 "Apr 2021": 0, "May 2021":0, "Jun 2021":0, "Jul 2021":0, "Aug 2021":0,"Sep 2021":0, "Oct 2021": 0,
                 "Nov 2021":0, "Dec 2021":0, "Jan 2022":0, "Feb 2022" : 0,"Mar 2022":0,"Apr 2022": 0, "May 2022":0,
                 "Jun 2022":0, "Jul 2022":0, "Aug 2022":0,"Sep 2022":0, "Oct 2022": 0, "Nov 2022":0, "Dec 2022":0}



    # for month between feb 2020 to dec 2022
    # get count
    # return count dictionary
    for key in countDate.keys():
        selected_tweets = []
        for tweet in Tweet.objects.all():
            t_month = tweet.created_at[4:7]
            t_year = tweet.created_at[26:30]
            if (t_month == key[0:3]) and (t_year == key[4:8]):
                selected_tweets.append(tweet)
        if len(selected_tweets) > 0:
            countDate[key] = len(selected_tweets)

    return countDate

def get_polarity_by_month():
    countDate = {"Feb 2020": 0, "Mar 2020":0,"Apr 2020": 0, "May 2020":0, "Jun 2020":0, "Jul 2020":0, "Aug 2020":0,
                 "Sep 2020":0, "Oct 2020": 0, "Nov 2020":0, "Dec 2020":0, "Jan 2021":0, "Feb 2021" : 0,"Mar 2021":0,
                 "Apr 2021": 0, "May 2021":0, "Jun 2021":0, "Jul 2021":0, "Aug 2021":0,"Sep 2021":0, "Oct 2021": 0,
                 "Nov 2021":0, "Dec 2021":0, "Jan 2022":0, "Feb 2022" : 0,"Mar 2022":0,"Apr 2022": 0, "May 2022":0,
                 "Jun 2022":0, "Jul 2022":0, "Aug 2022":0,"Sep 2022":0, "Oct 2022": 0, "Nov 2022":0, "Dec 2022":0}

    # for month between feb 2020 to dec 2022
    # get polarity of all tweets
    # let each month in dict = avg of all polarity for each month
    # return dict containing all avg polarities

    for key in countDate.keys():
        selected_tweets = []
        for tweet in Tweet.objects.all():
            t_month = tweet.created_at[4:7]
            t_year = tweet.created_at[26:30]

            blob = TextBlob(tweet.full_text)
            t_polarity = blob.sentiment.polarity

            if (t_month == key[0:3]) and (t_year == key[4:8]):
                selected_tweets.append(t_polarity)

        total = 0
        for value in selected_tweets:
            total += value

        if len(selected_tweets) > 0:
            avg = total / len(selected_tweets)
            countDate[key] = avg

    return countDate

from PandemicAnalyser.models import Tweet, TweetPolarity
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
            t_month = tweet.created_at[4:7] # in created_at string select substring from position 4 tp 7, which is the month
            t_year = tweet.created_at[26:30] # select substring which is the year

            blob = TextBlob(tweet.full_text)
            t_polarity = blob.sentiment.polarity # use polarity function to get sentiment

            if (t_month == key[0:3]) and (t_year == key[4:8]):
                selected_tweets.append(t_polarity) # if month with polarity info is same as key, add value to dictionary

        total = 0
        for value in selected_tweets:
            total += value # add all sentiment values

        if len(selected_tweets) > 0: # if more than 1 tweet added to selected_tweets list for each month
            avg = total / len(selected_tweets) # average sum of all polarities by total amount of tweets
            countDate[key] = avg # add avg polarity to dictionary of months

    return countDate


    #     for day in month:
    #         get polarity of day
    #         add it to a dictionary
    # return dictionary

    # 31 day months = January, March, May, July, August, October, and December
    # 30 day months = April, June, September, and November
    # 28 day month (except leap year = 29) = February
    # Feb 2020 was a leap year
    # for every day in a month
    # add sentiment of every day to a dictionary
    # then you can make line plots of daily sentiment by month and use slider to visualize change
def get_daily_polarity(month, year):
    # It would take too long to calculate the daily polarity of all tweets every time the website gets loaded
    # It's better to calculate it once, add it to the DB and then just make a function to get values from DB
    long_months = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
    mid_months = ["Apr", "Jun", "Sep", "Nov"]
    short_months = ["Feb"]


    if month in long_months: # 31 days
        dailySentiment = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0,
                          "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                          "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0,
                          "26": 0, "27": 0, "28": 0,"29": 0, "30": 0, "31": 0}
    elif month in mid_months: #30 days
        dailySentiment = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0,
                          "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                          "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0,
                          "26": 0, "27": 0, "28": 0,"29": 0, "30": 0}
    elif ((month in short_months) and (year == "2020")): # February 2020 was leap - 29 days
        dailySentiment = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0,
                          "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                          "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0,
                          "26": 0, "27": 0, "28": 0,"29": 0}
    else: # 28 days
        dailySentiment = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0,
                          "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                          "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0,
                          "26": 0, "27": 0, "28": 0}

    for tweet in TweetPolarity.objects.all():
        t_day = tweet.created_at[8:10]
        t_month = tweet.created_at[4:7] # in created_at string select substring from position 4 tp 7, which is the month
        t_year = tweet.created_at[26:30] # select substring which is the year

        t_polarity = tweet.polarity
        if (t_day in dailySentiment and t_month == month and t_year == year):
             dailySentiment[t_day] = t_polarity

    return dailySentiment

def get_all_daily_polarity():

    sentimentDate = {"Feb 2020": {}, "Mar 2020": {}, "Apr 2020": {}, "May 2020": {}, "Jun 2020": {}, "Jul 2020": {},
                     "Aug 2020": {}, "Sep 2020": {}, "Oct 2020": {}, "Nov 2020": {}, "Dec 2020": {}, "Jan 2021": {},
                     "Feb 2021": {}, "Mar 2021": {}, "Apr 2021": {}, "May 2021": {}, "Jun 2021": {}, "Jul 2021": {},
                     "Aug 2021": {}, "Sep 2021": {}, "Oct 2021": {}, "Nov 2021": {}, "Dec 2021": {}, "Jan 2022": {},
                     "Feb 2022": {}, "Mar 2022": {}, "Apr 2022": {}, "May 2022": {}, "Jun 2022": {}, "Jul 2022": {},
                     "Aug 2022": {}, "Sep 2022": {}, "Oct 2022": {}, "Nov 2022": {}, "Dec 2022": {}}

    for key in sentimentDate.keys():
            sentimentDate[key] = get_daily_polarity(key[0:3], key[4:8])

    return sentimentDate

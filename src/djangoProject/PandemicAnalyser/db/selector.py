from PandemicAnalyser.models import Tweet

def select_by_date(tweets, month, year): # select tweets given a list of tweets, a month and a year
    selected_tweets = []
    for tweet_dict in tweets:
        t_month = tweet_dict["created_at"][4:7] # index the substring containing month - e.g."Aug" or "Nov"
        t_year = tweet_dict["created_at"][26:30] # index the substring containing the year - e.g. 2020 or 2021
        if (t_month == month) and (t_year == year):
            selected_tweets.append(tweet_dict)
    return selected_tweets # return the list of tweets from given date



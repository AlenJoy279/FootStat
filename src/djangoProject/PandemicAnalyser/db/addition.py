from textblob import TextBlob
from unittest.mock import patch
from .decoder import *
import os
from PandemicAnalyser.models import Tweet, TweetPolarity

seen = []
seen1 = []
#abs_path = "C:/Users/Jaime/Documents/hydrated/" # Path containing the tweets - this path points to tweets in the month of april of 2020

def get_files(path):
    # r = root, d = directories , f = files
    for r, d, f in os.walk(path):
        for file in f: # iterate over every file
            full_path = os.path.join(r, file)
            add_to_db(full_path) # add tweets from each file into the DB
            add_tweet_polarity(full_path)


def add_to_db(path): # function to add tweets from given path to DB
    if path not in seen:
        json_data = jsonl_to_json(path)
        for tweet_dict in json_data: # tweet_dict is just the dictionary of all items
            xcreated_at = ""
            xid = ""
            xid_str = ""
            xfull_text = ""
            xdisplay_text_range = ""
            xentities = ""
            xsource = ""
            xin_reply_to_status_id = ""
            xin_reply_to_status_id_str = ""
            xin_reply_to_user_id = ""
            xin_reply_to_user_id_str = ""
            xin_reply_to_screen_name = ""
            xuser = ""
            xgeo = ""
            xcoordinates = ""
            xplace = ""
            xcontributors = ""
            xis_quote_status = ""
            xretweet_count = ""
            xfavorite_count = ""
            xfavorited = ""
            xretweeted = ""
            xlang = ""

            for k,v in tweet_dict.items():
                    if k == "created_at":
                        xcreated_at = v
                    elif k == "id":
                        xid = v
                    elif k == "id_str":
                        xid_str = v
                    elif k == "full_text":
                        xfull_text = v
                    elif k == "display_text_range":
                        xdisplay_text_range = v
                    elif k == "entities":
                        xentities = v
                    elif k == "source":
                        xsource = v
                    elif k == "in_reply_to_status_id":
                        xin_reply_to_status_id = v
                    elif k == "in_reply_to_status_id_str":
                        xin_reply_to_status_id_str = v
                    elif k == "in_reply_to_user_id":
                        xin_reply_to_user_id = v
                    elif k == "in_reply_to_user_id_str":
                        xin_reply_to_user_id_str = v
                    elif k == "in_reply_to_screen_name":
                        xin_reply_to_screen_name = v
                    elif k == "user":
                        xuser = v
                    elif k == "geo":
                        xentities = v
                    elif k == "coordinates":
                        xsource = v
                    elif k == "place":
                        xplace = v
                    elif k == "contributors":
                        xcontributors = v
                    elif k == "is_quote_status":
                        xis_quote_status = v
                    elif k == "retweet_count":
                        xretweet_count = v
                    elif k == "favorite_count":
                        xfavorite_count = v
                    elif k == "favorited":
                        xfavorited = v
                    elif k == "retweeted":
                        xretweeted = v
                    elif k == "lang":
                        xlang = v

            tweet_instance = Tweet(created_at = xcreated_at, id=xid, id_str = xid_str, full_text = xfull_text, display_text_range=xdisplay_text_range, entities=xentities,source=xsource,in_reply_to_status_id=xin_reply_to_status_id,in_reply_to_user_id_str=xin_reply_to_user_id_str, in_reply_to_screen_name = xin_reply_to_screen_name, user = xuser, geo = xgeo, coordinates = xcoordinates, place = xplace, contributors = xcontributors, is_quote_status = xis_quote_status, retweet_count = xretweet_count, favorite_count = xfavorite_count, favorited = xfavorited, retweeted = xretweeted, lang = xlang)
            tweet_instance.save() # save the tweet into the DB

        seen.append(path)


def get_data(path): # return list of tweets from given path
    return jsonl_to_json(path)

def add_tweet_polarity(path):
    if path not in seen1:
        json_data = jsonl_to_json(path)
        for tweet_dict in json_data: # tweet_dict is just the dictionary of all items
            xcreated_at = ""
            xid = ""
            xid_str = ""
            xfull_text = ""
            xentities = ""
            xsource = ""
            xuser = ""
            xgeo = ""
            xretweet_count = ""
            xfavorite_count = ""
            xfavorited = ""
            xretweeted = ""
            xpolarity = ""

            for k,v in tweet_dict.items():
                    if k == "created_at":
                        xcreated_at = v
                    elif k == "id":
                        xid = v
                    elif k == "id_str":
                        xid_str = v
                    elif k == "full_text":
                        xfull_text = v
                        blob = TextBlob(xfull_text)
                        xpolarity = str(blob.sentiment.polarity)
                    elif k == "entities":
                        xentities = v
                    elif k == "source":
                        xsource = v
                    elif k == "user":
                        xuser = v
                    elif k == "geo":
                        xentities = v
                    elif k == "favorited":
                        xfavorited = v
                    elif k == "retweeted":
                        xretweeted = v

            tweet_instance = TweetPolarity(created_at = xcreated_at, id=xid, id_str = xid_str, full_text = xfull_text, entities=xentities,source=xsource, user = xuser, geo = xgeo, retweet_count = xretweet_count, favorite_count = xfavorite_count, favorited = xfavorited, retweeted = xretweeted, polarity = xpolarity)
            tweet_instance.save() # save the tweet into the DB

        seen.append(path)
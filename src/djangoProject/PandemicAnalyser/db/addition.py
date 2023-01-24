from .decoder import *
import os
from PandemicAnalyser.models import Tweet

seen = []
abs_path = "C:/Users/Jaime/Documents/hydrated/April 2020" # Path containing the tweets - this path points to tweets in the month of april of 2020

def get_files():
    # r = root, d = directories , f = files
    for r, d, f in os.walk(abs_path):
        for file in f: # iterate over every file
            full_path = os.path.join(abs_path, file)
            add_to_db(full_path) # add tweets from each file into the DB


def add_to_db(path): # function to add tweets from given path to DB
    if path not in seen:
        json_data = jsonl_to_json(path)
        for tweet_dict in json_data:
            tweet_instance = Tweet(tweet_dict)
            tweet_instance.save() # save the tweet into the DB

        seen.append(path)

def get_data(path): # return list of tweets from given path
    return jsonl_to_json(path)
import os
import json

import pandas as pd
import re

from twill.commands import *
from twarc.client2 import Twarc2


def convert_to_json():
    # Reading in a hydrated tweet file as a panads dataframe
    json_obj = pd.read_json(path_or_buf="hydrated/no_tag2020_april1_april2.csv.jsonl", lines=True)

    return json_obj


def retrieve_dataset_links():
    # As our dataset source site does not have any other way to retrieve the data, we are using twill to do so
    browser.go("https://ieee-dataport.org/")
    browser.go("https://ieee-dataport.org/saml_login?destination=/")
    browser.show_links()
    browser.show_forms()
    browser.submit()
    browser.show_forms()
    form_value("1", "pf.username", "redacted")
    form_value("1", "pf.pass", "redacted")
    browser.show_forms()
    browser.submit()
    browser.submit()
    browser.show_forms()
    browser.go("https://ieee-dataport.org/open-access/coronavirus-covid-19-geo-tagged-tweets-dataset")
    all_links = browser.links

    correct_links = []
    for link in all_links:
        regex = re.search("\d{4}_\d{2}\.zip", link.text)
        if regex:
            correct_links.append(link)

    print(correct_links[0:10])

    with open("links.txt", "r") as f:
        for link in correct_links:
            f.write(link.url + "\n")
        print("Links written")


def drop_tags():
    # Drop the included sentiment tags
    for file in os.listdir("dehydrated"):
        print(file)
        dataframe = pd.read_csv("dehydrated\\" + file, header=None)
        dataframe = dataframe[0]
        dataframe.to_csv("untagged\\" + "no_tag" + file, index=False, header=None)


infile = "untagged\\no_tag2020_april1_april2.csv"


def hydrate_tweets():
    # Hydrate tweets using twarc library
    t = Twarc2(consumer_key="redacted",
               consumer_secret="redacted",
               access_token="redacted",
               access_token_secret="redacted",
               bearer_token="redacted",
               )

    with open(infile) as f:
        str_f = f.read()
        tweet_list = str_f.split()

    print(tweet_list)


def jsonl_to_json(jsonl):
    with open(jsonl) as f:
        list_jsonl = list(f)

    return [json.loads(jline) for jline in list_jsonl]


if __name__ == '__main__':
    drop_tags()
    hydrate_tweets()
    result = convert_to_json()
    print(result)
    json_list = jsonl_to_json("hydrated/no_tag2020_april1_april2.csv.jsonl")
    print(len(json_list))
    print(json_list[0])

    all_jsons_list = []
    count = len(os.listdir("hydrated"))
    for file in os.listdir("hydrated"):
        count -= 1
        json_list = jsonl_to_json(f"hydrated/{file}")
        all_jsons_list.append(json_list)
        print(f"Remaining: {count}")

    print(all_jsons_list[-1][0])

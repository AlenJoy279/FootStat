from django.http import HttpResponse
from django.shortcuts import render
from PandemicAnalyser.db.selector import *
from PandemicAnalyser.db.addition import *
from PandemicAnalyser.Graphs.test import *

seen = []

def index(request):
  # check if new path added
  # if new path - call function
  tweets = []
  #entries.delete()

  #jsonl_path = "C:/Users/Jaime/Documents/hydrated/no_tag2020_august18_august19.csv.jsonl"

  #add_to_db(jsonl_path) # the function contains checker - if path already been checked then do not add

  #selected_tweets = select_by_date(jsonl_to_json("C:/Users/Jaime/Documents/hydrated/test"), "Apr", "2022")

  get_files() # add all tweets from hydrated path to db

  selected_tweets = select_by_date("Apr", "2022")

  dict_count = get_count_by_date()
  dict_polarity = get_polarity_by_month()

  fig_plot = testplot(dict_polarity)
  fig_piechart = testpiechart(dict_count)
  fig_barchart = testbarchart(dict_polarity)

  return render(request, 'index.html', {'plot': fig_plot, 'piechart':fig_piechart, 'barchart': fig_barchart, 'tweets' : selected_tweets})

def register(request):
 return HttpResponse("Hello from registration page")

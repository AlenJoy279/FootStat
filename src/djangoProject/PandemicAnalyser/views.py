from django.http import HttpResponse
from django.shortcuts import render
from PandemicAnalyser.db.selector import *
from PandemicAnalyser.db.addition import *

seen = []

def index(request):
  # check if new path added
  # if new path - call function
  tweets = []
  #entries.delete()

  #jsonl_path = "C:/Users/Jaime/Documents/hydrated/no_tag2020_august18_august19.csv.jsonl"

  #add_to_db(jsonl_path) # the function contains checker - if path already been checked then do not add

  #selected_tweets = select_by_date(get_data(jsonl_path), "Aug", "2020")

  get_files() # add all tweets from hydrated path to db

  return render(request, 'index.html', {'tweets' : tweets})

def register(request):
 return HttpResponse("Hello from registration page")

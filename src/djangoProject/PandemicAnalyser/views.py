from django.http import HttpResponse
from django.shortcuts import render
from PandemicAnalyser.db.selector import *
from PandemicAnalyser.db.addition import *
from PandemicAnalyser.Graphs.barchart import *
from PandemicAnalyser.Graphs.lineplot import *
from PandemicAnalyser.Graphs.piechart import *

seen = []
pol_calc = False
def index(request):
  # check if new path added
  # if new path - call function
  tweets = []
  #entries.delete()

  #jsonl_path = "C:/Users/Jaime/Documents/hydrated/no_tag2020_august18_august19.csv.jsonl"

  #add_to_db(jsonl_path) # the function contains checker - if path already been checked then do not add

  #selected_tweets = select_by_date(jsonl_to_json("C:/Users/Jaime/Documents/hydrated/test"), "Apr", "2022")

  get_files() # add all tweets from hydrated path to db
  if pol_calc == False:
    # calcualte the polarity and add to Tweet_polarity table in DB
    # Use this table in functions to select values for website to improve speed of processes
    pass

  # selected_tweets = select_by_date("Apr", "2022")

  dict_count = get_count_by_date()
  dict_polarity = get_polarity_by_month()

  fig_plot = lineplot_by_month(dict_polarity)
  fig_piechart = piechart_by_month(dict_count)
  fig_barchart = barchart_by_month(dict_polarity)
  fig_lineplot = lineplot_by_month(dict_polarity)

  plots = []
  all_pol = get_all_daily_polarity()
  for date, daily_sentiment in all_pol.items():
        plots.append(lineplot_by_day(date, daily_sentiment))


  return render(request, 'index.html', {'plot': fig_plot, 'piechart':fig_piechart,
                                        'barchart': fig_barchart, 'lineplot': fig_lineplot,
                                        # 'tweets' : selected_tweets,
                                        'Feb2020': plots[0], 'Mar2020': plots[1], 'Apr2020': plots[2], 'May2020': plots[3], "Jun2020": plots[4],
                                        "Jul2020": plots[5],
                                        "Aug2020": plots[6], "Sep2020": plots[7], "Oct2020": plots[8], "Nov2020": plots[9], "Dec2020": plots[10],
                                        "Jan2021": plots[11],
                                        "Feb2021": plots[12], "Mar2021": plots[13], "Apr2021": plots[14], "May2021": plots[15], "Jun2021": plots[16],
                                        "Jul2021": plots[17],
                                        "Aug2021": plots[18], "Sep2021": plots[19], "Oct2021": plots[20], "Nov2021": plots[21], "Dec2021": plots[22],
                                        "Jan2022": plots[23],
                                        "Feb2022": plots[24], "Mar2022": plots[25], "Apr2022": plots[26], "May2022": plots[27], "Jun2022": plots[28],
                                        "Jul2022": plots[29],
                                        "Aug2022": plots[30], "Sep2022": plots[31], "Oct2022": plots[32], "Nov2022": plots[33], "Dec2022": plots[34]
                                        })

def register(request):
 return HttpResponse("Hello from registration page")

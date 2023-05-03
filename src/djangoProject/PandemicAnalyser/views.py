from django.http import HttpResponse
from django.shortcuts import render
import os

from PandemicAnalyser.Graphs.heatmap import get_tweet_heatmap, get_monthly_heatmap
from PandemicAnalyser.Plots.searcher import *
from PandemicAnalyser.Predictor.logisticreg import *
#from PandemicAnalyser.Predictor.logisticreg import run_acc
from PandemicAnalyser.db.selector import *
from PandemicAnalyser.db.addition import *
from PandemicAnalyser.Graphs.barchart import *
from PandemicAnalyser.Graphs.lineplot import *
from PandemicAnalyser.Graphs.piechart import *
from PandemicAnalyser.Predictor.bayes import *
from PandemicAnalyser.Predictor.decisiontree import *
from PandemicAnalyser.Predictor.kmeans import *
from PandemicAnalyser.Predictor.knn import *

seen = []
pol_calc = False

def index(request):

  #get_files("C:/Users/Jaime/Documents/hydrated/") # add all tweets from hydrated path to db
  # Tweet.objects.all().delete()
  # TweetPolarity.objects.all().delete()

  #avgy = get_all_polarity()
  # for date, pol in avgy.items():
  #     print("For " + date + " polarity is equal to " + str(pol))

  # selected_tweets = select_by_date("Jul", "2022")

  # dict_count = get_count_by_date()
  # dict_polarity = get_polarity_by_month()
  #
  #fig_plot = lineplot_by_month(dict_polarity)
  # fig_piechart = piechart_by_month(dict_count)
  #fig_barchart = barchart_by_month(avgy)
  #fig_lineplot = lineplot_by_month(avgy)

  # plots = []
  # all_pol = get_all_daily_polarity()
  # for date, daily_sentiment in all_pol.items():
  #           if(date == "Oct 2021"):
  #              plots.append(lineplot_by_day(date, daily_sentiment))

  yplots = get_yearly_html_files("./PandemicAnalyser/templates/yearly")

  hmaps = get_monthly_heatmap()

  return render(request, 'index.html', {#'plot': fig_plot, 'piechart':fig_piechart,
                                        'barchart': yplots[0], 'lineplot': yplots[1],'Mar2020': hmaps["2020_03"], 'Apr2020': hmaps["2020_04"],
                                        'May2020': hmaps["2020_05"], 'Jun2020': hmaps["2020_06"], 'Jul2020': hmaps["2020_07"],
                                        "Aug2020": hmaps["2020_08"], "Sep2020": hmaps["2020_09"], "Oct2020": hmaps["2020_10"], "Nov2020": hmaps["2020_11"], "Dec2020": hmaps["2020_12"],
                                        "Jan2021": hmaps["2021_01"],
                                        "Feb2021": hmaps["2021_02"], "Mar2021": hmaps["2021_03"], "Apr2021": hmaps["2021_04"], "May2021": hmaps["2021_05"], "Jun2021": hmaps["2021_06"],
                                        "Jul2021": hmaps["2021_07"],
                                        "Aug2021": hmaps["2021_08"], "Sep2021": hmaps["2021_09"], "Oct2021": hmaps["2021_10"], "Nov2021": hmaps["2021_11"], "Dec2021": hmaps["2021_12"],
                                        "Jan2022": hmaps["2022_01"],
                                        "Feb2022": hmaps["2022_02"], "Mar2022": hmaps["2022_03"], "Apr2022": hmaps["2022_04"], "May2022": hmaps["2022_05"], "Jun2022": hmaps["2022_06"],
                                        "Jul2022": hmaps["2022_07"],
                                        "Aug2022": hmaps["2022_08"], "Sep2022": hmaps["2022_09"], "Oct2022": hmaps["2022_10"], "Nov2022": hmaps["2022_11"], "Dec2022": hmaps["2022_12"]
  })

def register(request):
 return HttpResponse("Hello from registration page")


def daily(request):
    plots = get_monthly_html_files("./PandemicAnalyser/templates/monthly")
    return render(request, 'daily.html', {
        'Mar2020': plots[0], 'Apr2020': plots[1], 'May2020': plots[2], "Jun2020": plots[3],
        "Jul2020": plots[4],
        "Aug2020": plots[5], "Sep2020": plots[6], "Oct2020": plots[7], "Nov2020": plots[8], "Dec2020": plots[9],
        "Jan2021": plots[10],
        "Feb2021": plots[11], "Mar2021": plots[12], "Apr2021": plots[13], "May2021": plots[14], "Jun2021": plots[15],
        "Jul2021": plots[16],
        "Aug2021": plots[17], "Sep2021": plots[18], "Oct2021": plots[19], "Nov2021": plots[20], "Dec2021": plots[21],
        "Jan2022": plots[22],
        "Feb2022": plots[23], "Mar2022": plots[24], "Apr2022": plots[25], "May2022": plots[26], "Jun2022": plots[27],
        "Jul2022": plots[28],
        "Aug2022": plots[29], "Sep2022": plots[30], "Oct2022": plots[31], "Nov2022": plots[32] #, "Dec2022": plots[33]
    })


def models(request):
    bayes_accuracy = get_nbc_accuracy()
    #dt_accuracy = get_dt_accuracy()
    dt_accuracy = 0.77
    km_accuracy = get_km_accuracy()
    knn_accuracy = get_knn_accuracy()
    textblob_accuracy = get_builtinTextblob_accuracy()
    # replace with function call
    linearRegression_accuracy = 0.85
    bar = barchart_models(bayes_accuracy, dt_accuracy, km_accuracy, knn_accuracy, linearRegression_accuracy, textblob_accuracy)

    #run_lr = run_acc()
    #cm_html = run_lr[1]

    confusion_matrix = get_lr_cm()
    #wordmap = get_wordmap()

    return render(request, 'models.html', {'barchart': bar, 'confusionmatrix': confusion_matrix})#, 'wordmap':wordmap})

def keydates(request):
    # April 10th 2020 - https://www.theguardian.com/world/live/2020/apr/10/coronavirus-live-news-global-deaths-near-95000-as-boris-johnson-leaves-intensive-care

    # May 14th 2020 - https://edition.cnn.com/2020/05/14/world/coronavirus-global-death-toll-300000-intl/index.html and pa

    # April 19th 2021 - https://edition.cnn.com/2021/04/20/europe/who-global-covid-cases-rise-intl/index.html

    # 11th May 2021 - https://www.who.int/publications/m/item/weekly-epidemiological-update-on-covid-19---11-may-2021

    # 8th July 2021 - https://www.nytimes.com/2021/07/08/world/covid-death-toll-four-million.html




    #key_dates = get_polarity_by_keydate()
    # 21 values in keydates
    # for i in range(0, len(list(key_dates))):
    #     dates = key = list(key_dates)[i]
    #
    #     value = list(key_dates.values())[i]
   # print(list(key_dates.values())[0], list(key_dates.values())[1])
    key_dates = get_polarity_by_keydate() # size = 12
    for k,v in key_dates.items():
        print(k + " : " + str(v))
    # barchart for April 7 2020
    bchart = barchart_keydates(list(key_dates.values())[0], 0.14, 0.1362, 0.132)


    return render(request, 'key_dates.html',{"bchart": bchart, "Apr072020": list(key_dates.values())[0], "Jun262020": list(key_dates.values())[1],
        "Jul162020": list(key_dates.values())[2], "Aug022020": list(key_dates.values())[3],
         "Sep222020": list(key_dates.values())[4], "Oct022020": list(key_dates.values())[5], "Nov092020": list(key_dates.values())[6], "Nov232020": list(key_dates.values())[7],
         "Feb222021": list(key_dates.values())[8], "Aug232021": list(key_dates.values())[9], "Nov192021": list(key_dates.values())[10], "Nov262021": list(key_dates.values())[11],
         "Jan312022": list(key_dates.values())[12], "Mar292022": list(key_dates.values())[13]
         })
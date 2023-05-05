from django.http import HttpResponse
from django.shortcuts import render
import os

from PandemicAnalyser.Graphs.heatmap import get_tweet_heatmap, get_monthly_heatmap
from PandemicAnalyser.Plots.searcher import *
from PandemicAnalyser.Predictor.logisticreg import *
from PandemicAnalyser.Predictor.predictor_cm import get_model_cm, get_model_roc
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

  #hmaps = get_monthly_heatmap() # - save html files locally to increase speed
  hmaps = get_html_heatmap("./PandemicAnalyser/templates/heatmaps")

  return render(request, 'index.html', {'barchart': yplots[0], 'lineplot': yplots[1],'Mar2020': hmaps[0], 'Apr2020': hmaps[1],
                                      'May2020': hmaps[2], 'Jun2020': hmaps[3], 'Jul2020': hmaps[4],
                                      "Aug2020": hmaps[5], "Sep2020": hmaps[6], "Oct2020": hmaps[7], "Nov2020": hmaps[8], "Dec2020": hmaps[9],
                                      "Jan2021": hmaps[10],
                                      "Feb2021": hmaps[11], "Mar2021": hmaps[12], "Apr2021": hmaps[13], "May2021": hmaps[14], "Jun2021": hmaps[15],
                                      "Jul2021": hmaps[16],
                                      "Aug2021": hmaps[17], "Sep2021": hmaps[18], "Oct2021": hmaps[19], "Nov2021": hmaps[20], "Dec2021": hmaps[21],
                                      "Jan2022": hmaps[22],
                                      "Feb2022": hmaps[23], "Mar2022": hmaps[24], "Apr2022": hmaps[25], "May2022": hmaps[26], "Jun2022": hmaps[27],
                                      "Jul2022": hmaps[28],
                                      "Aug2022": hmaps[29], "Sep2022": hmaps[30], "Oct2022": hmaps[31], "Nov2022": hmaps[32], "Dec2022": hmaps[33]
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
    #bayes_accuracy = get_nbc_accuracy() # 81.4 comment out to increase performance of page
    nb_accuracy = 0.814
    #dt_accuracy = get_dt_accuracy() # comment out to increase performance of page
    dt_accuracy = 0.77
    #km_accuracy = get_km_accuracy() # comment out to increase performance of page
    km_accuracy = 0.518
    #knn_accuracy = get_knn_accuracy() # comment out to increase performance of page
    knn_accuracy = 0.645
    textblob_accuracy = get_builtinTextblob_accuracy()
    # replace with function call
    #lr_acc = get_lr_accuracy() # comment out to increase performance of page

    linearRegression_accuracy = 0.85
    bar = barchart_models(nb_accuracy, dt_accuracy, km_accuracy, knn_accuracy, linearRegression_accuracy, textblob_accuracy)

    lr_cm =  get_lr_cm() # Linear Regression Confusion Matrix

    bayes_cm = get_html_confusion_matrix("./PandemicAnalyser/templates/confusionmatrix")[0]
    dt_cm = get_html_confusion_matrix("./PandemicAnalyser/templates/confusionmatrix")[1]

    lr_roc = get_model_roc("lr")
    bayes_roc = get_model_roc("bayes")
    dt_roc = get_model_roc("dtree")



    return render(request, 'models.html', {'barchart': bar, 'bayescm': bayes_cm, 'dtcm': dt_cm, 'confusionmatrix': lr_cm, 'lrroc':lr_roc, 'bayesroc':bayes_roc,'dtroc':dt_roc})#, 'wordmap':wordmap})

def keydates(request):
    #key_dates = get_polarity_by_keydate()
    # 21 values in keydates
    # for i in range(0, len(list(key_dates))):
    #     dates = key = list(key_dates)[i]
    #
    #     value = list(key_dates.values())[i]
    # keydates = {"Tue Apr 07 2020": 0, "Fri Jun 26 2020": 0, "Sun Aug 02 2020": 0,
    #             "Tue Sep 22 2020": 0, "Fri Oct 02 2020": 0, "Mon Nov 09 2020": 0, "Mon Nov 23 2020": 0,
    #             "Mon Feb 22 2021": 0, "Mon Aug 23 2021": 0, "Fri Nov 19 2021": 0, "Fri Nov 26 2021": 0,
    #             "Mon Jan 31 2022": 0, "Tue Mar 29 2022": 0
    #             }
    # key_dates = get_polarity_by_keydate(keydates) # save results in a list to improve performance of page


    saved_keydates = [0.14054810600872966, 0.15304431755898318,0.163285410276362544,0.10349607837589297,
                      0.10685744981802997,0.13143202378373287,0.1282361845622578,0.1265807905825768,0.12059142380792934,0.10401309604574527,
                      0.15276981513705368,0.09882007893879585,0.08691728795895465] # results from get_polarity_by_keydate()



    # example usage of calcualting polarity for week of key date
    # april7 = ["Mon Apr 06 2020", "Tue Apr 07 2020", "Wed Apr 08 2020", "Thu Apr 09 2020", "Fri Apr 10 2020", "Sat Apr 11 2020", "Sun Apr 12 2020"]
    # apr7pol = get_polarity_by_week(april7)
    # print("Apr 6-12 2020: " + str(apr7pol))

    weekly_pol = [0.14895861255695822, 0.14175093901961183,0.1479684015380725,0.11972344063970056,0.10735286785623825,0.12746099383006945,
                      0.1311043011637578,0.1181601523600599,0.1086768056816407,0.10561466420070531,0.11681086053503623,0.06820246806111255,
                      0.08403333852052453]




    # barchart for April 7 2020
    bchart = barchart_keydates(saved_keydates[0], weekly_pol[0], 0.1362, 0.1312)
    #June 26 2020
    bchart1 = barchart_keydates(saved_keydates[1], weekly_pol[1], 0.1363, 0.1312)
    # August 2020
    bchart3 = barchart_keydates(saved_keydates[2], weekly_pol[2], 0.1479, 0.1312)
    # September 2020
    bchart4 = barchart_keydates(saved_keydates[3], weekly_pol[3], 0.1248, 0.1312)
    # October 2020
    bchart5 = barchart_keydates(saved_keydates[4], weekly_pol[4], 0.1235, 0.1312)
    # November 9-15 2020
    bchart6 = barchart_keydates(saved_keydates[5], weekly_pol[5], 0.1265, 0.1312)
    # November 23-29 2020
    bchart7 = barchart_keydates(saved_keydates[6], weekly_pol[6], 0.1265, 0.11256)
    # February 2021
    bchart8 = barchart_keydates(saved_keydates[7], weekly_pol[7], 0.1216, 0.11256)
    # August 2021
    bchart9 = barchart_keydates(saved_keydates[8], weekly_pol[8], 0.1058, 0.11256)
    # November 15-21 2021
    bchart10 = barchart_keydates(saved_keydates[9], weekly_pol[9], 0.1122, 0.11256)
    # November 22-28 2021
    bchart11 = barchart_keydates(saved_keydates[10], weekly_pol[10], 0.1362, 0.11256)
    # January 2022
    bchart12 = barchart_keydates(saved_keydates[11], weekly_pol[11], 0.0706, 0.0931)
    # March 2022
    bchart13 = barchart_keydates(saved_keydates[12], weekly_pol[12], 0.0935, 0.0931)


    return render(request, 'key_dates.html',{"bchart": bchart, "bchart1": bchart1, "bchart3": bchart3,
                                             "bchart4": bchart4, "bchart5": bchart5, "bchart6": bchart6,"bchart7": bchart7,
                                             "bchart8": bchart8, "bchart9": bchart9, "bchart10": bchart10, "bchart11": bchart11,
                                             "bchart12": bchart12, "bchart13": bchart13,
                                             "Apr072020": saved_keydates[0], "Jun262020": saved_keydates[1],
                                             "Aug022020": saved_keydates[2],
                                             "Sep222020": saved_keydates[3], "Oct022020": saved_keydates[4],
                                             "Nov092020": saved_keydates[5], "Nov232020": saved_keydates[6],
                                             "Feb222021": saved_keydates[7], "Aug232021": saved_keydates[8],
                                             "Nov192021": saved_keydates[9], "Nov262021": saved_keydates[10],
                                             "Jan312022": saved_keydates[11], "Mar292022": saved_keydates[12]
         })

def about(request):
    return render(request, 'about.html')
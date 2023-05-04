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

  #hmaps = get_monthly_heatmap() # - save html files locally to increase speed
  hmaps = get_html_heatmap("./PandemicAnalyser/templates/heatmaps")

  return render(request, 'index.html', {#'plot': fig_plot, 'piechart':fig_piechart,
                                        'barchart': yplots[0], 'lineplot': yplots[1],
                                        # 'Mar2020': hmaps["2020_03"], 'Apr2020': hmaps["2020_04"],
                                        # 'May2020': hmaps["2020_05"], 'Jun2020': hmaps["2020_06"], 'Jul2020': hmaps["2020_07"],
                                        # "Aug2020": hmaps["2020_08"], "Sep2020": hmaps["2020_09"], "Oct2020": hmaps["2020_10"], "Nov2020": hmaps["2020_11"], "Dec2020": hmaps["2020_12"],
                                        # "Jan2021": hmaps["2021_01"],
                                        # "Feb2021": hmaps["2021_02"], "Mar2021": hmaps["2021_03"], "Apr2021": hmaps["2021_04"], "May2021": hmaps["2021_05"], "Jun2021": hmaps["2021_06"],
                                        # "Jul2021": hmaps["2021_07"],
                                        # "Aug2021": hmaps["2021_08"], "Sep2021": hmaps["2021_09"], "Oct2021": hmaps["2021_10"], "Nov2021": hmaps["2021_11"], "Dec2021": hmaps["2021_12"],
                                        # "Jan2022": hmaps["2022_01"],
                                        # "Feb2022": hmaps["2022_02"], "Mar2022": hmaps["2022_03"], "Apr2022": hmaps["2022_04"], "May2022": hmaps["2022_05"], "Jun2022": hmaps["2022_06"],
                                        # "Jul2022": hmaps["2022_07"],
                                        # "Aug2022": hmaps["2022_08"], "Sep2022": hmaps["2022_09"], "Oct2022": hmaps["2022_10"], "Nov2022": hmaps["2022_11"], "Dec2022": hmaps["2022_12"]
                                      'Mar2020': hmaps[0], 'Apr2020': hmaps[1],
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
    #key_dates = get_polarity_by_keydate() # size = 12
    saved_keydates = [0.14054810600872966, 0.15304431755898318,0.1375485197159457,0.16328541027636254,0.16328541027636254,0.10349607837589297,
                      0.10685744981802997,0.13143202378373287,0.1282361845622578,0.1265807905825768,0.12059142380792934,0.10401309604574527,
                      0.15276981513705368,0.09882007893879585,0.08691728795895465] # results from get_polarity_by_keydate()
    # for k,v in key_dates.items():
    #     print("key date: " + k + " : " + str(v))


    #week 6-12 april 2020 = [
    # april7 = ["Mon Apr 06 2020", "Tue Apr 07 2020", "Wed Apr 08 2020", "Thu Apr 09 2020", "Fri Apr 10 2020", "Sat Apr 11 2020", "Sun Apr 12 2020"]
    # apr7pol = get_polarity_by_week(april7)
    # print("Apr 6-12 2020: " + str(apr7pol))
    # # 22-28 june 2020
    # june26 = ["Mon Jun 22 2020", "Tue Jun 23 2020", "Wed Jun 24 2020", "Thu Jun 25 2020", "Fri Jun 26 2020", "Sat Jun 27 2020", "Sun Jun 28 2020"]
    # jun26pol = get_polarity_by_week(june26)
    # print("Jun 22-28 2020: " + str(jun26pol))
    # # 13-19 july 2020
    # july16 = ["Mon Jul 13 2020", "Tue Jul 14 2020", "Wed Jul 15 2020", "Thu Jul 16 2020", "Fri Jul 17 2020", "Sat Jul 18 2020", "Sun Jul 19 2020"]
    # jul16pol = get_polarity_by_week(july16)
    # print("Jul 13-19 2020: " + str(jul16pol))
    # # 27-2 august 2020
    # august2 = ["Mon Jul 27 2020", "Tue Jul 28 2020", "Wed Jul 29 2020", "Thu Jul 30 2020", "Fri Jul 31 2020", "Sat Aug 01 2020", "Sun Aug 02 2020"]
    # aug2pol = get_polarity_by_week(august2)
    # print("Jul 27-2 August 2020: " + str(aug2pol))
    # # 21-27 september 2020
    # sep22 = ["Mon Sep 21 2020", "Tue Sep 22 2020", "Wed Sep 23 2020", "Thu Sep 24 2020", "Fri Sep 25 2020", "Sat Sep 26 2020", "Sun Sep 27 2020"]
    # sep22pol = get_polarity_by_week(sep22)
    # print("Sep 13-19 2020: " + str(sep22pol))
    # # 28 September - 4 October 2020
    # oct02 = ["Mon Sep 28 2020", "Tue Sep 29 2020", "Wed Sep 30 2020", "Thu Oct 01 2020", "Fri Oct 02 2020", "Sat Oct 03 2020", "Sun Oct 04 2020"]
    # oct02pol = get_polarity_by_week(oct02)
    # print("Sep 28-4 October 2020: " + str(oct02pol))
    # # 9-15 November 2020
    # nov09 = ["Mon Nov 09 2020", "Tue Nov 10 2020", "Wed Nov 11 2020", "Thu Nov 12 2020", "Fri Nov 13 2020", "Sat Nov 14 2020", "Sun Nov 15 2020"]
    # nov09pol = get_polarity_by_week(nov09)
    # print("9-15 November 2020: " + str(nov09pol))
    # # 23 - 29 November 2020
    # nov23 = ["Mon Nov 23 2020", "Tue Nov 24 2020", "Wed Nov 25 2020", "Thu Nov 26 2020", "Fri Nov 27 2020", "Sat Nov 28 2020", "Sun Nov 29 2020"]
    # nov23pol = get_polarity_by_week(nov23)
    # print("23-29 November 2020: " + str(nov23pol))
    # # 22-28 February 2021
    # feb22 = ["Mon Feb 22 2021", "Tue Feb 23 2021", "Wed Feb 24 2021", "Thu Feb 25 2021", "Fri Feb 26 2021", "Sat Feb 27 2021", "Sun Feb 28 2021"]
    # feb22pol = get_polarity_by_week(feb22)
    # print("22-28 February 2021: " + str(feb22pol))
    # # 23-29 August 2021
    # aug23 = ["Mon Aug 23 2021", "Tue Aug 24 2021", "Wed Aug 25 2021", "Thu Aug 26 2021", "Fri Aug 27 2021", "Sat Aug 28 2021", "Sun Aug 29 2021"]
    # aug23pol = get_polarity_by_week(aug23)
    # print("23-29 August 2021: " + str(aug23pol))
    # # 15-21 November 2021
    # nov19 = ["Mon Nov 15 2021", "Tue Nov 16 2021", "Wed Nov 17 2021", "Thu Nov 18 2021", "Fri Nov 19 2021", "Sat Nov 20 2021", "Sun Nov 21 2021"]
    # nov19pol = get_polarity_by_week(nov19)
    # print("15-21 November 2021: " + str(nov19pol))
    # # 22-28 November 2021
    # nov26 = ["Mon Nov 22 2021", "Tue Nov 23 2021", "Wed Nov 24 2021", "Thu Nov 25 2021", "Fri Nov 26 2021", "Sat Nov 27 2021", "Sun Nov 28 2021"]
    # nov26pol = get_polarity_by_week(nov26)
    # print("22-28 November 2021: " + str(nov26pol))
    # # 31 Jan - 6 February 2022
    # jan31 = ["Mon Jan 31 2022", "Tue Feb 01 2022", "Wed Feb 02 2022", "Thu Feb 03 2022", "Fri Feb 04 2022", "Sat Feb 05 2022", "Sun Feb 06 2022"]
    # jan31pol = get_polarity_by_week(jan31)
    # print("31-06 Jan 2022: " + str(jan31pol))
    # # 28 March - 3 April 2022
    # mar29 = ["Mon Mar 28 2022", "Tue Mar 29 2022", "Wed Mar 30 2022", "Thu Mar 31 2022", "Fri Apr 01 2022", "Sat Apr 02 2022", "Sun Apr 03 2022"]
    # mar29pol = get_polarity_by_week(mar29)
    # print("28 March -03 April 2022: " + str(mar29pol))

    # barchart for April 7 2020
    bchart = barchart_keydates(saved_keydates[0], 0.207718, 0.1362, 0.1312)
    #June 26 2020
    bchart1 = barchart_keydates(saved_keydates[1], 0.12383, 0.1363, 0.1312)
    # July 16 2020
    bchart2 = barchart_keydates(saved_keydates[2], 0.145947, 0.1478, 0.1312)
    # August 2020
    bchart3 = barchart_keydates(saved_keydates[3], 0.163285, 0.1479, 0.1312)
    # September 2020
    bchart4 = barchart_keydates(saved_keydates[4], 0.12184, 0.1248, 0.1312)
    # October 2020
    bchart5 = barchart_keydates(saved_keydates[5], 0.12177, 0.1235, 0.1312)
    # November 9-15 2020
    bchart6 = barchart_keydates(saved_keydates[6], 0.13022, 0.1265, 0.1312)
    # November 23-29 2020
    bchart7 = barchart_keydates(saved_keydates[7], 0.10285, 0.1265, 0.11256)
    # February 2021
    bchart8 = barchart_keydates(saved_keydates[8], 0.13323, 0.1216, 0.11256)
    # August 2021
    bchart9 = barchart_keydates(saved_keydates[9], 0.11866, 0.1058, 0.11256)
    # November 15-21 2021
    bchart10 = barchart_keydates(saved_keydates[10], 0.0900, 0.1122, 0.11256)
    # November 22-28 2021
    bchart11 = barchart_keydates(saved_keydates[11], 0.073600, 0.1362, 0.11256)
    # January 2022
    bchart12 = barchart_keydates(saved_keydates[12], 0.051876, 0.0706, 0.0931)
    # March 2022
    bchart13 = barchart_keydates(saved_keydates[13], 0.0701637, 0.0935, 0.0931)


    return render(request, 'key_dates.html',{"bchart": bchart, "bchart1": bchart1,"bchart2": bchart2, "bchart3": bchart3,
                                             "bchart4": bchart4, "bchart5": bchart5, "bchart6": bchart6,"bchart7": bchart7,
                                             "bchart8": bchart8, "bchart9": bchart9, "bchart10": bchart10, "bchart11": bchart11,
                                             "bchart12": bchart12, "bchart13": bchart13,
                                             "Apr072020": saved_keydates[0], "Jun262020": saved_keydates[1],
                                             "Jul162020": saved_keydates[2], "Aug022020": saved_keydates[3],
                                             "Sep222020": saved_keydates[4], "Oct022020": saved_keydates[5],
                                             "Nov092020": saved_keydates[6], "Nov232020": saved_keydates[7],
                                             "Feb222021": saved_keydates[8], "Aug232021": saved_keydates[9],
                                             "Nov192021": saved_keydates[10], "Nov262021": saved_keydates[11],
                                             "Jan312022": saved_keydates[12], "Mar292022": saved_keydates[13]
         })
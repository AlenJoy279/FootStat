import matplotlib.pyplot as plt
import numpy as np
import mpld3
from PandemicAnalyser.models import Tweet

def lineplot_by_month(dict):

    labels = list(dict.keys())
    sizes = dict.values()

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.plot(labels, sizes)

    ax.set_xticks(np.arange(len(labels)))

    ax.set_xticklabels(["Mar 2020", "Apr 2020", "May 2020", "Jun 2020", "Jul 2020", "Aug 2020",
              "Sep 2020", "Oct 2020", "Nov 2020", "Dec 2020", "Jan 2021", "Feb 2021", "Mar 2021",
              "Apr 2021", "May 2021", "Jun 2021", "Jul 2021", "Aug 2021", "Sep 2021", "Oct 2021",
              "Nov 2021", "Dec 2021", "Jan 2022", "Feb 2022", "Mar 2022", "Apr 2022", "May 2022",
              "Jun 2022", "Jul 2022", "Aug 2022", "Sep 2022", "Oct 2022", "Nov 2022", "Dec 2022"])

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    ax.set_title("Sentiment Score by Month")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sentiment Score")

    mpld3.save_html(fig, "All Monthly Sentiment Lineplot")
    return mpld3.fig_to_html(fig)

def lineplot_by_day(date, dic): # make a line plot for every day of the month

    labels = dic.keys()
    sizes = dic.values()

    fig, ax = plt.subplots(figsize=(6, 6))


    ax.plot(labels, sizes)

    ax.set_title("Daily Sentiment Score during " + date[0:3] + " of " + date[4:8])
    ax.set_xlabel("Day")
    ax.set_ylabel("Sentiment Score")


    mpld3.save_html(fig, "Sentiments October 2021")
    return mpld3.fig_to_html(fig)

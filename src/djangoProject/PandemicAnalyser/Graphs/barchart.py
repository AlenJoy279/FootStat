import matplotlib.pyplot as plt
import numpy as np
import mpld3
from PandemicAnalyser.models import Tweet

def barchart_by_month(dict):
    labels = list(dict.keys())
    sizes = dict.values()

    colors = np.random.rand(len(labels), 3) # make random colours for each bar of the bar chart
    fig, ax = plt.subplots(figsize=(10,10))
    ax.bar(labels, sizes,color=colors, align="center")

    ax.set_xticks(np.arange(len(labels)))

    ax.set_xticklabels(["Feb 2020", "Mar 2020", "Apr 2020", "May 2020", "Jun 2020", "Jul 2020", "Aug 2020",
              "Sep 2020", "Oct 2020", "Nov 2020", "Dec 2020", "Jan 2021", "Feb 2021", "Mar 2021",
              "Apr 2021", "May 2021", "Jun 2021", "Jul 2021", "Aug 2021", "Sep 2021", "Oct 2021",
              "Nov 2021", "Dec 2021", "Jan 2022", "Feb 2022", "Mar 2022", "Apr 2022", "May 2022",
              "Jun 2022", "Jul 2022", "Aug 2022", "Sep 2022", "Oct 2022", "Nov 2022", "Dec 2022"])

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    ax.set_title("Sentiment Score by Month")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sentiment Score")

    handles = []
    for i, label in enumerate(ax.get_xticklabels()):
        handles.append(ax.bar(0, 0, color=colors[i], label=label.get_text())[0])
    ax.legend(handles, labels, title="Date", loc="upper left", fontsize="small")

    mpld3.save_html(fig, "All Barchart Monthly")


    return mpld3.fig_to_html(fig)


def barchart_models(bayes, dt, km, knn, lr, txtblob):

    labels = ['Naive Bayes Classifier', 'Decision Tree Classifier', 'K-means clustering', 'KNN clustering', 'Logistic Regression', 'TextBlob Classifier']
    sizes = [bayes, dt, km, knn, lr, txtblob]

    colors = np.random.rand(len(labels), 3)
    fig, ax = plt.subplots(figsize=(10, 10))

    # Set the x-tick marks to the center of each bar
    x_pos = np.arange(len(labels))
    ax.bar(x_pos, sizes, color=colors)

    # Set the x-tick labels at each bar
    ax.set_xticklabels(["Naive Bayes Classifier", "Decision Tree Classifier", "K-means clustering", "KNN clustering", "Logistic Regression", "TextBlob Classifier"])
    ax.set_xticks(x_pos)

    ax.set_title("Sentiment Score by Model")
    ax.set_xlabel("Model")
    ax.set_ylabel("Sentiment Score")

    html = mpld3.fig_to_html(fig)
    # Add center alignment to the HTML code
    centered_html = f'<div style="text-align: center">{html}</div>'


    return centered_html


def barchart_keydates(date, weekly, monthly, yearly):
    sizes = [date, weekly, monthly, yearly]
    labels = ['Daily', 'Weekly', 'Monthly', 'Yearly']

    # Set the positions of the bars on the x-axis

    colors = ['green','orange', 'purple', 'red']
    fig, ax = plt.subplots(figsize=(8, 4))

    # Set the x-tick marks to the center of each bar
    x_pos = np.arange(len(labels))
    ax.bar(x_pos, sizes, color=colors)

    ax.set_xticklabels(["Day", "Week", "Month", "Year"])
    ax.set_xticks(x_pos)

    # Set the x-tick labels at each bar
    plt.xlabel('Timeframe')
    plt.ylabel('Polarity Values')
    plt.title('Sentiment Polarity Comparison')

    html = mpld3.fig_to_html(fig)
    # Add center alignment to the HTML code
    centered_html = f'<div style="text-align: center">{html}</div>'


    return centered_html
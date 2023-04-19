import matplotlib.pyplot as plt
import numpy as np
import mpld3
from PandemicAnalyser.models import Tweet

def piechart_by_month(dict):
    labels = dict.keys()
    sizes = dict.values()

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.legend(
        loc='upper left',
        prop={'size': 11},
        bbox_to_anchor=(0.0, 1),
    )
    fig.set_size_inches(10, 10)
    return mpld3.fig_to_html(fig)

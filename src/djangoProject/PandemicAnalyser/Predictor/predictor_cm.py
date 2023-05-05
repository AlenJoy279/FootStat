import pickle

import mpld3
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import roc_curve, auc
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

from PandemicAnalyser.Predictor.logisticreg import create_dfs_matrices


# Takes in the name of a model to output its confusion matrix. Options: "bayes", "dtree", "lr"
def get_model_cm(model_name):

    model = ""
    if model_name == "bayes":
        model = BernoulliNB()
    elif model_name == "dtree":
        model = DecisionTreeClassifier()
    elif model_name == "lr":
        model = LogisticRegression()
    train_test_matrices = create_dfs_matrices()[-1]
    X_test = train_test_matrices[2]
    y_test = train_test_matrices[3]


    model.fit(train_test_matrices[0], train_test_matrices[1])
    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    # Print the evaluation metrics for the dataset.
    # print(y_pred)
    print(classification_report(y_test, y_pred))
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    categories = ['Negative', 'Positive']
    group_names = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
    group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]
    labels = [f'{v1}n{v2}' for v1, v2 in zip(group_names, group_percentages)]
    labels = np.asarray(labels).reshape(2, 2)
    sns.heatmap(cf_matrix, annot=labels, cmap='Blues', fmt='',
                xticklabels=categories, yticklabels=categories)
    plt.xlabel("Predicted values", fontdict={'size': 14}, labelpad=10)
    plt.ylabel("Actual values", fontdict={'size': 14}, labelpad=10)
    plt.title("Confusion Matrix", fontdict={'size': 18}, pad=20)


    html = mpld3.fig_to_html(plt.gcf())
    centered_html = f'<div style="text-align: center;">{html}</div>'

    mpld3.save_html(plt.gcf(), "confusion_matrix_" + model_name + ".html")

    return centered_html


def get_model_roc(model_name):
    model = ""
    if model_name == "bayes":
        model = BernoulliNB()
    elif model_name == "dtree":
        model = DecisionTreeClassifier()
    elif model_name == "lr":
        model = LogisticRegression()
    train_test_matrices = create_dfs_matrices()[-1]
    X_test = train_test_matrices[2]
    y_test = train_test_matrices[3]

    model.fit(train_test_matrices[0], train_test_matrices[1])
    # Predict values for Test dataset
    y_pred = model.predict(X_test)

    # Plot the ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC CURVE')
    plt.legend(loc="lower right")

    html = mpld3.fig_to_html(plt.gcf())
    centered_html = f'<div style="text-align: center;">{html}</div>'

    return centered_html

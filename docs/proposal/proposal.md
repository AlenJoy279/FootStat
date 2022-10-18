# School of Computing &mdash; Year 4 Project Proposal Form

## SECTION A

|                     |                      |
|---------------------|----------------------|
|Project Title:       | PandemicAnalysis     |
|Student 1 Name:      | Jaime De Rivero Woods|
|Student 1 ID:        | 19447494             |
|Student 2 Name:      | Alen Tom Joy         |
|Student 2 ID:        | 18313576             |
|Project Supervisor:  | Renaat Verbruggen    |


## SECTION B

### Introduction

For our fourth year project, we plan to develop a web application that will perform NLP (Natural Language Processing) and sentiment analysis on a publically available Twitter dataset about the COVID-19 pandemic. The goal of the analysis is to evaluate the general public sentiment around this topic. The application will display the results of the analysis using word clouds and frequency charts, this will allow users to understand the data in a simple manner. We also plan to develop a historical analysis feature to display the sentiments on the topic over time, which will provide information about how the sentiments on this topic have changed.

### Outline

The web application will use a publicly available dataset on the COVID-19 pandemic from Kaggle/GitHub that is maintained and updated periodically. We will perform Natural Language Processing and sentiment analysis on the tweets in the dataset to figure out how positive or negative the data is. In the web application, users will be able to either find the overall sentiment on the topic, or choose the overall sentiment on the topic at a specific moment in time. This historical analysis feature will perform sentiment analysis of past tweets, dating back all the way to (e.g. Feb 2020 when covid pandemic started). The historical analysis will allow users to view the sentiment of the tweets between user selectable dates by way of filters and sliders.

### Background

We teamed up for our third year project, and had an idea to perform sentiment analysis using the Twitter API on a topic. After some discussion we decided it was too complex for the third year project. This year, we went ahead with the idea, and met with Renaat Verbruggen to discuss how we would go about it. He recommended we focus on a public dataset for Twitter to perform NLP and sentiment analysis. We decided to focus on the COVID-19 pandemic as it has been a very relevant topic, and has affected the whole world. We also found it very interesting to perform an analysis of the overall sentiment, to gain further knowledge into how this topic has affected people.

### Achievements

The project will provide a data analysis platform, for those interested in the public perception and overall sentiment of tweets related to the pandemic, and how this changes over time. The users will be any person who has an interest in the topic and wants to gain further knowledge on how people have reacted to the news. In particular, the project could provide insights to government and healthcare professionals dealing with future pandemics. 

### Justification

This web application can be a useful tool for people who wish to gain knowledge on how this topic has affected people's sentiment, as it has impacted so many lives around the world. As this is a current topic, it can be useful in this moment, but it could also be used in the future, if someone wishes to gain insight into what the sentiments about the COVID-19 pandemic were at the time, and how they developed. We haven’t found apps or websites that perform this analysis, so we hope that the information we develop can be specifically useful to academics who might study this topic and use this information on how the news on this topic are perceived overall, how social media has displayed people’s sentiment of the topic, or how the sentiments of people on the topic have changed over time. As a more direct example, the data could be used to identify which strategies gained the most public support or had the least financial impacts to business owners.

### Programming language(s)

We plan to use python’s Django framework and CSS for the webapp, Python and JQuery for the backend processing.

### Programming tools / Tech stack

We will use the Django framework to develop the web application. We will also use JavaScript to run the website. We will store and update datasets on a CentOS or Ubuntu server. Due to the large volumes of Twitter data that needs to be processed, we will use a NoSQL database (MongoDB/Cassandra) for better performance and flexibility. 

For the NLP and sentiment analysis aspects, we will use Jupyter Notebook as well as various Python libraries such as padas, numpy, matplotlib etc. To clean our dataset, we will use the nltk toolkit and for tokenization, we plan to use a tool such as CountVectorizer. 

### Hardware

N/A.

### Learning Challenges

As part of the project, we will have to learn the theory behind NLP and sentiment analysis. This will include things such as generating a clean version of our dataset by removing punctuation and stopwords. We would also need to filter out retweets where relevant. Next, we would need to identify which tools and algorithms are best suited for tokenization in order to convert the data into a vector format.
To achieve this, we will need to learn and gain experience with Python libraries such as pandas and numpy and software tools like Jupyter Notebook. 
Once we obtain the tokenized version of all tweets, we would have to learn how to use the Bayes Theorem to train a Multinomial Naive Bayes classifier model.
 We will then have to learn how to display the sentiment analysis data we have obtained in a useful and informative manner using the Django framework with our web application.
We will also have to learn how to set up a server that locates, retrieves, updates and processes the required Twitter datasets. This may require the use of a basic CI/CD system if it is not possible to update the datasets in place.

### Breakdown of work

#### Student 1 (Jaime de Vivero Woods)

I will focus on the design of the website, including the different pages on the site and how they will communicate with the back end. I will also work on displaying the data we analyse as word clouds, charts or in another format which we may decide to use. 
For the sentiment analysis which we will perform on the datasets, I will work alongside Alen to classify the data. I will also focus on cleaning the dataset and evaluating the performance of our model.

#### Student 2 (Alen Joy)

I will focus on setting up the server and basic automation tasks. This includes implementing a method to fetch and update datasets, database handling, authorization (if necessary) and resource allocation and monitoring.
With regard to sentiment analysis, I will be focusing on the tokenization and model training aspects.

'''
1. extract tweets from mongodb
    -connect to database
    -extract data
2. transform
    -text cleaning
    - sentiment analysis
    - changing data types
3. load: 
    -connect to postgres
    -insert transformed data into postgres
'''

import pymongo
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlalchemy
import psycopg2
import logging
import time


#endpoint_mongodb: "mongodb://mongodb:27017/"
client = pymongo.MongoClient("mongodb://mongodb:27017/") #<- name of your container: Get all this info from your get_tweets.py
db_tweets = client.tweetsdb #<- instead of twitter, the name of your actual database
tweets = db_tweets.tweets #<- instead of tweets the name of your collection 


engine = sqlalchemy.create_engine('postgresql://postgres:3456@postgresdb:5432/postgres') # changed 5432 into 5555.
create_query = '''create table if not exists tweets (text_id TEXT, text TEXT, scores TEXT, constraint tweet4_pkey primary key (text_id));'''
#docker_engine: postgresql://postgres:3456@tweety_pdb:5432/postgres; local_engine: postgres://localhost:5432/northwind
engine.execute(create_query)




def extract():
    '''extract tweets from mongo db'''
    extracted_tweets = list(tweets.find())
    return extracted_tweets


""" def transform(extracted_tweets):
    '''Performs your desired transformations: sentiment analysis, text cleaning, emoji managmenet '''
    transformed_tweets_username = []
    transformed_tweets_text = []
    for tweet in extracted_tweets:
        #transformed_tweets.append(re.sub(r'[{}]+'.format(punctuation),'',tweet['text']))

        transformed_tweets_username.append(tweet['username'])
        transformed_tweets_text.append(tweet['text'])

    return transformed_tweets_username, transformed_tweets_text """


def transform(extracted_tweets_text):
    '''Performs your desired transformations: sentiment analysis, text cleaning, emoji managmenet '''

    transformed_tweets_text = []
    text_id=[]
    for tweet in extracted_tweets:
        transformed_tweets_text.append(tweet['text'])
        text_id.append(tweet['text'][:20])

    return transformed_tweets_text, text_id




def sentiment_analysis(transformed_tweets_text):

    s = SentimentIntensityAnalyzer()
    score = []
    for text in transformed_tweets_text:
        score.append(s.polarity_scores('text')['compound'])
    return score




def load(transformed_tweets_username,transformed_tweets_text,score):    
    
    
    for id0, t, s  in  zip(text_id,transformed_tweets_text, score):

        query = """INSERT INTO tweets(text_id,text,scores) VALUES(%s,%s,%s) ON CONFLICT (text_id) DO NOTHING"""
        values = (id0,t,s)
        engine.execute(query,values)

    logging.critical('inserted into postgres!')

if __name__=='__main__':

    while True:

        extracted_tweets = extract()
        (transformed_tweets_text,text_id) = transform(extracted_tweets)
        score = (sentiment_analysis(transformed_tweets_text))
        load(text_id, transformed_tweets_text, score)
        
        time.sleep(30)
    



#!/usr/bin/env python
# coding: utf-8

import keys
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions
import tweepy
import pandas as pd
from sentiment import *


def analyze(text, term):

    nlu = NaturalLanguageUnderstandingV1(version='2020-08-01', authenticator = IAMAuthenticator(keys.watson_key))
    
    # Reponse is equal to this long thing that took forever to get right and is heavily inspired by the docs. Two methods, one gets emotion and one gets sentiment
    emotionObject = EmotionOptions(targets=[term])
    sentimentObject=SentimentOptions(targets=[term])
    features=Features(emotion=emotionObject, sentiment=sentimentObject)
    response = nlu.analyze(html=text, features=features).get_result()

    # Target Sentiment Score
    target_sentiment=response["sentiment"]["targets"]
    target_sentiment=(target_sentiment[0])["score"]

    # Doc sentiment score
    doc_sentiment=response["sentiment"]["document"]
    doc_sentiment=(doc_sentiment["score"])

    # Target emotion
    target_emotion=response["emotion"]["targets"][0]
    target_joy=target_emotion["emotion"]["joy"]
    target_disgust=target_emotion["emotion"]["disgust"]
    target_anger=target_emotion["emotion"]["anger"]


    # Doc emotion
    doc_emotion=response["emotion"]["document"]
    doc_joy=doc_emotion["emotion"]["joy"]
    doc_disgust=doc_emotion["emotion"]["disgust"]
    doc_anger=doc_emotion["emotion"]["anger"]

    # Format the whole thing as a cool list dictionary
    tweet_metrics=[{"Target Sentiment": target_sentiment, "Target Joy": target_joy, "Target Disgust": target_disgust, "Target Anger": target_anger},
                        {"Doc Sentiment": doc_sentiment, "Doc Joy": doc_joy, "Doc Disgust": doc_disgust, "Doc Anger": doc_anger}]

    return tweet_metrics


def get_tweets(user, tweet_max_id=None, count=200):
    """Idk get the tweets"""
    # Quick Oauth 2
    api = tweepy.API(tweepy.AppAuthHandler(keys.consumer_key, keys.consumer_secret))
    # Create User Tweets Object
    user_tweets = api.user_timeline(screen_name=user, count=count, max_id=tweet_max_id, tweet_mode="extended")
    # Create empty list
    tweet_list = []

    for tweet in user_tweets:
        
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text

        date = tweet.created_at
        tweet_id = tweet.id
        tweet_list.append({"Tweet_ID": tweet_id, "Text": text,
                          "Date": str(date), "User": user})

    # Create dataframe
    tweets_df=pd.DataFrame(tweet_list)

    return tweets_df

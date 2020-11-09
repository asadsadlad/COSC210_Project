# Scraping Partisanship - COSC 210

*How do accounts with a known political affiliation tweet about the same term?* 

It is expected that a conservative acount will tweet about Republicans positively, and Democrats negatively, and vice versa. This project takes a specific terms and performs sentiment analysis on a set of tweets containing that term. It then creates a visualization of the results based on the political affiliation of each account. 


## Each section below would run seperately in a Jupyter notebook. This is a bit confusing, but the process wil go as such:
1. Scrape Tweets, create db (done)
    * Create a JSON file from tweets scraped from a specific user
    * Compile files
    * Repeat these functions until I have sufficient (a lot of) data for a variety of liberal and conservative accounts
2. Create training set
    * Find tweets that have terms that are likely to be positive/negative within those sets (like running "GOP" will get tweets expected to have negative sentiment in liberal accounts and positive sentiment in conservative accounts)
    * Clean tweet links and append to new JSON files (positve/negative)
    * Pull random samples from these JSON files and append to CSV. I won't use a very disciplined method for separating training/testing sets, but if we have a big enough database and do it randomly it should be okay
    * Train Watson custom class using csv (using CURL)
-----------------------------------------------------------------------------
3. Test model

    **For conservative and liberal sets:**

    * Find tweets that match term, clean links, and append to new dataframe
    * For every tweet, run tweet metrics from Watson (functions for this are done)
    * Create new columns for each metric
    * Average these metric columns
    * Average each metric average for a final sentiment value on that term
        - Might be weighted. For example, the "disgust/anger" measure on Watson tends to be more accurate that the sentiment, and the custom class may or may not be more accurate, so one metric might have a greater say in the final value
    * Save two json files, one with all of tweets and their metrics and one with just the calculated averages
    **Final result will be four files**

4. Visualize (basically done)
    * Create dataframes from the previous files
    * Create plots from those files
    * Save plot as html


## Imports
### Because the imports are split between a variety of notebooks, I've listed all of them here.
    Watson imports:
    from ibm_watson import NaturalLanguageUnderstandingV1
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions

    import keys (API keys)
    import json
    import tweepy (Twitter API interface)
    import pandas as pd (pandas)
    import sentiment (seperate file for misc functions and classes)
    from os import listdir (to walk filenames)


## Scrape tweets, create db - These functions won't necessarily run all at once in a tidy program, but instead will be run in jupyter to create the training/data sets
    def users_tweets(user)
        Make tweets frame from get_tweets(user)
        Create counter for loop
        While counter is not 0
            Id is the last tweet ID in the dataframe
            Keep appending the tweets frame with get_user and id as flag - This allows us to get the users past 1,000 tweets
            counter -= 1
        return tweets_frame

    def save_tweets(list of users)
        """Save a file for each user's tweets"""
        for user in list of users
            tweets_frame = users_tweets(user)
            save json file in directory root/scraped_tweets


    def append_json(small_path, big_path, file_name):
        big_frame = empty dataframe with columns "Tweet_ID", "Text", "Date", "User"
        file = list of files in directory small_path
        for file in files
            append big_frame
        reset big_frame index
        save big_frame as json to big_path with file_name
        


## Analyze those (might end up putting this in a class since the (term, path) object seems like it could be used a lot).
Pseudocode isn't as detailed here bc a lot of the mechanics are reused pieces of previous functions

    def clean_text(text)
        if characters in text
            take those chracters out

    def in_json(term, file path)
        create empty dataframe
        read json
        for tweet text in json
            if term in text
                clean_text(text)
                append dataframe with text
        save df as json

    def analyze_tweets(file path, term)
        new columns in json
        for tweet in json
            for text in json
                append new column with results of analyze(text, term)

    def average columns(file path)
        Average the results of this column and store values as dict
        write dict to new json file

    def add_polarity(polarity)
        add a column with all values of either -2 or 2 depending on the polarity of the specific dataset ( )


**A combination of the above functions will be used to create the training set, which will be in csv form.**

## Plotting

    Import libraries

    def data(take in final df)
        """Create points from dataframe"""
        Add jitter to x value so all dots are not on top of each other

    def style plot
        """Style plot"""
        Create and show axes 
        Add axes to layout

        Hide default bokehjs axes
        Create labels
        Create legend

    def show notebook
        """Output notebook in juptyer notebook"""

    def create plot(term)
        """Create Plot w/ term as label"""

    def main(term)

        # Create plot
        
        # Objects to draw
        
        
        # Style plot and add legend
        
        #Show notebook 
        show_notebook
    Call main outputs plot

    ## External functions defined in separate file
    def get_tweets(user, tweet_max_id=None, count)
        """Idk get the tweets"""
        Oauth 2

        Create User Tweets Object
    
        Create empty list
    
        For each tweet get text, date, id, and append to list
        
        Create dataframe

        return tweets_df

    def analyze(text, term): (This was previosly in a class but I don't think that the data stored in this object needs to be reused so a function will do)
        """Get metrics given text and target from watson"""
        Authorize watson

        Make the API object 

        Parse Target Sentiment Score

        Parse Doc sentiment score
        
        Parse Target emotions

        Parse doc emotions

        format the whole thing in a dictionary

        return tweet_metrics






import tweepy
import os
import random
import datetime
import calendar
import csv
import time
import pandas as pd

if __name__ == '__main__':
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    AS = os.environ['AS']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    target = "@jishukuchan"
    # # target = "@saaaaaacchannn"

    tweets = api.user_timeline(target, count=100)

    tweets_raw = []
    for tweet in tweets:
        # print(type(tweet._json))
        # tweet._json["created_at"] =
        tweets_raw.append(tweet._json)

    df = pd.io.json.json_normalize(tweets_raw)

    print(df)

    df.to_pickle('tweet_obj.pkl')

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

    # target = "@jishukuchan"
    targets = []

    with open('user.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == "woman":
                targets.append(row[0])
    f.close()

    print(len(targets))

    tweets_all = []
    cou = 1
    for target in targets:
        print(cou, "/", len(targets), target, end="")
        tweet_cou = 0
        for page in range(5):
            try:
                tweets = api.user_timeline(target, count=200, page=page)
                for tweet in tweets:
                    # print(type(tweet._json))
                    # tweet._json["created_at"] =
                    tweets_all.append(tweet._json)
                    tweet_cou += 1

                    # print(tweet._json["text"])
            except tweepy.error.TweepError:
                continue

        print(" " + str(tweet_cou) + "件取得しました。")

        cou += 1

    df = pd.io.json.json_normalize(tweets_all)

    print(len(df))
    # print(df.columns.values)

    df.to_pickle('tweet_obj.pkl')

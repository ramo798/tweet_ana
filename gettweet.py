import tweepy
import os
import random
import datetime
import calendar
import csv
import time
import pandas as pd
from pymongo import MongoClient


def date_conv(date_str):
    date = date_str
    word = date.split(" ")
    # print(word)
    months = {}
    for i, v in enumerate(calendar.month_abbr):
        months[v] = i

    time_string = word[5] + "-" + str(months[word[1]]) + "-" + word[2] + " " + word[3]
    # print(time_string)
    time_datetime = datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

    return time_datetime


def get_user(sex):
    targets = []
    with open('user.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == sex:
                targets.append(row[0])
    f.close()
    targets = list(set(targets))
    print('対象ユーザ:', len(targets))
    return targets


def add_tweet_to_db(tweet, dbname, collectionname):
    client = MongoClient("mongodb://root:password@localhost:27017")
    db = client[dbname]
    collection = db[collectionname]
    collection.insert_one(tweet)
    client.close()


if __name__ == '__main__':
    client = MongoClient("mongodb://root:password@localhost:27017")
    db = client['tweet']
    collection = db['man']

    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    AS = os.environ['AS']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweet = api.user_timeline("@jishukuchan", count=1)

    targets = get_user("man")

    tweets_all = []
    cou = 1
    for target in targets:
        print(cou, "/", len(targets), target, end="")
        tweet_cou = 0
        for page in range(5):
            try:
                tweets = api.user_timeline(target, count=2000, page=page)
                for tweet in tweets:
                    tweet._json["created_at"] = date_conv(tweet._json["created_at"])
                    tweet._json["text"] = tweet._json["text"].strip()
                    collection.insert_one(tweet._json)
                    tweet_cou += 1
            except tweepy.error.TweepError:
                continue

        print(" " + str(tweet_cou) + "件取得しました。")

        cou += 1
    client.close()

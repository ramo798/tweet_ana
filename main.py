import tweepy
import os
import random
import datetime
import calendar
import csv
import time
from pymongo import MongoClient


def get_user(sex):
    targets = []
    with open('user.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == sex:
                targets.append(row[0])
    f.close()

    print('対象ユーザ:', len(targets))
    return targets


def add_tweet_to_db(tweet, dbname, collectionname):
    client = MongoClient("mongodb://root:password@localhost:27017")
    db = client[dbname]
    collection = db[collectionname]
    collection.insert_one(tweet)
    client.close()


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


def get_tweet(api, u_id):
    res = []
    try:
        tweets = api.user_timeline(u_id)
    except tweepy.error.TweepError:
        return 0

    for tweet in tweets:
        tweet._json["created_at"] = date_conv(tweet._json["created_at"])
        tweet._json["text"] = tweet._json["text"].strip()
        add_tweet_to_db(tweet._json, 'testtest', 'test1')


if __name__ == '__main__':
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    AS = os.environ['AS']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # target = "@jishukuchan"
    target = "@saaaaaacchannn"

    get_user('man')
    get_tweet(api, target)
    # for user in user_list:
    #     get_tweet(api, user)

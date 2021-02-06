import tweepy
import os
import random
import datetime
import calendar
import csv


def date_conv(date_str):
    date = date_str
    word = date.split(" ")

    months = {}
    for i, v in enumerate(calendar.month_abbr):
        months[v] = i

    time_string = word[7] + "-" + str(months[word[1]]) + "-" + word[2]
    time_datetime = datetime.datetime.strptime(time_string, '%Y-%m-%d')

    return time_datetime


def get_tweet(api, u_id):
    res = []
    tweets = api.user_timeline(u_id)
    for tweet in tweets:
        # print(tweet._json['user']['name'])
        # print("")
        created_at = tweet._json["created_at"]
        id_str = tweet._json['user']["id_str"]
        text = tweet._json["text"].strip()
        text_conv = ""
        for a in text:
            text_conv += a.replace('\n', '').replace('\r\n', '')
        name = tweet._json['user']["name"]
        screen_name = tweet._json['user']["screen_name"]
        profile_image_url = tweet._json['user']["profile_image_url"]
        print(name, text_conv)
        with open('tweet_list.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, screen_name, id_str, text_conv,
                             profile_image_url, created_at])
        f.close()


if __name__ == '__main__':
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    AS = os.environ['AS']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    target = "@jishukuchan"

    # date = "Sat Feb 06 10: 11: 49 +0000 2021"
    # print(date_conv(date))

    get_tweet(api, target)

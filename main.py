import tweepy
import os
import random
import datetime
import calendar


def date_conv(date_str):
    date = date_str
    word = date.split(" ")

    months = {}
    for i, v in enumerate(calendar.month_abbr):
        months[v] = i

    time_string = word[7] + "-" + str(months[word[1]]) + "-" + word[2]
    time_datetime = datetime.datetime.strptime(time_string, '%Y-%m-%d')

    return time_datetime


if __name__ == '__main__':
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    AS = os.environ['AS']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    target = "@jishukuchan"

    date = "Sat Feb 06 10: 11: 49 +0000 2021"
    print(date_conv(date))

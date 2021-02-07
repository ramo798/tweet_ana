import tweepy
import os
import random
import datetime
import calendar
import csv
import time


if __name__ == '__main__':
    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    AS = os.environ['AS']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # print(api.get_user(1326914680011550730)._json)
    # res = api.get_user(1326914680011550730)._json
    # screen_name = res['screen_name']
    # print(screen_name)

    with open('active_woman.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            try:
                res = api.get_user(row[0])._json
            except tweepy.error.TweepError:
                continue
            name = res['name']
            screen_name = res['screen_name']
            id_str = res['id_str']
            profile_image_url = res['profile_image_url']
            description = res['description']
            description_c = ""
            for a in description:
                description_c += a.replace('\n', '').replace('\r\n', '')

            with open('result.csv', 'a') as g:
                writer = csv.writer(g)
                writer.writerow([name, screen_name, id_str, description_c,
                                 profile_image_url])
            g.close()

    f.close()

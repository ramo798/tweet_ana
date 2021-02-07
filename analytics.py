import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
import calendar


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


if __name__ == '__main__':

    df = pd.read_pickle('tweet_obj.pkl')

    # print(df_tweet[0])
    # print(df[['created_at', 'user.name']].head(1))

    # 日付をdatetime型に変換する処理
    for index, row in df.iterrows():
        df.at[index, 'created_at'] = date_conv(row['created_at'])
    df['date'] = pd.to_datetime(df['created_at'])

    # 出現回数集計用の数字の用意
    df['count'] = 1

    # print(df.columns.values)
    # print(df[['created_at', 'user.name', 'count', 'date']].head(20))
    # print(df[['user.followers_count', 'user.friends_count', 'user.name', 'date']].head())

    # 時間帯ごとのルイートの集計
    tweet_per_hour = df[['count']].groupby(df['date'].dt.hour).sum()
    tmp = pd.DataFrame({'count': 0}, index=[0])
    for nindex in range(0, 24):
        if not nindex in tweet_per_hour.index.tolist():
            tmp = pd.DataFrame({'count': 0}, index=[nindex])
            tweet_per_hour = pd.concat([tweet_per_hour, tmp])
    tweet_per_hour = tweet_per_hour.sort_index()
    # print(tweet_per_hour.index)

    # 時間帯ごとのツイート数の可視化
    # tweet_per_hour.plot.bar()
    # plt.xlabel('hour', size=12)  # x軸指定
    # plt.ylabel('count', size=12)  # Y軸指定
    # plt.show()

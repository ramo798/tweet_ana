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

    print(df[['created_at', 'user.name', 'count', 'date']].head(20))

    # 時間帯ごとのルイートの集計
    tweet_per_hour = df[['count']].groupby(df['date'].dt.hour).sum()
    print(tweet_per_hour)

    # plt.figure(figsize=(20, 5))
    # g = sns.barplot(x="created_at", y="id", data=df.set_index("created_at").resample("H")["id"].count().reset_index())
    # labels = g.get_xticklabels()
    # g.set_xticklabels(labels, rotation=90)
    # plt.show()

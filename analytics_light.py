import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
import calendar

if __name__ == '__main__':
    df = pd.read_csv('activeuser.csv')

    # print(df[['user.followers_count', 'user.friends_count', 'user.name']].head())

    print(df['user.followers_count'].idxmax())
    # df.plot(kind='scatter', x='user.followers_count', y='user.friends_count')
    # plt.show()

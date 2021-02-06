import datetime
import calendar
import csv

if __name__ == '__main__':
    # print(datetime.datetime.now())
    today = datetime.datetime.now()
    user_list = []

    with open('tweet_list.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            user_list.append(row[2])
    f.close()

    user_list = list(set(user_list))
    # print(user_list)

    # print(len(user_list))

    active_tweet = []
    for user in user_list:
        with open('tweet_list.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == user:
                    target = datetime.datetime.strptime(
                        row[5], '%Y-%m-%d %H:%M:%S')
                    from_dt = today - datetime.timedelta(days=10)
                    to_dt = today
                    if from_dt <= target <= to_dt:
                        active_tweet.append(row[2])
    is_active = []
    for user in user_list:
        if active_tweet.count(user) > 5:
            is_active.append(user)
            with open('active_woman.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([user])
            f.close()

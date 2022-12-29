import time
import datetime
import os
import json

aa = []

n = 0


def get_data():
    while True:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        info = {'sex': n + 1, 'time': time_now}
        time.sleep(1)
        with open('tmp.txt', 'a+') as log:
            log.write(json.dumps(info))


def clear_data():
    aa.clear()
    get_data()


get_data()

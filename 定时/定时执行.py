import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os


def my_job():
    # print("123")
    with open('tmp.txt', 'r') as log:
        all_file = log.read()
        os.system("echo ''>tmp.txtq")
        print(all_file)
        with open('tmp1.txt', 'a+') as log1:
            log1.write(all_file)


if __name__ == '__main__':
    print("定时器启动")
    sched = BlockingScheduler()
    sched.add_job(my_job, 'interval', seconds=5, max_instances=1)
    sched.start()

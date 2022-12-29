from flask import Flask
import time
import pymysql
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=10)
app = Flask(__name__)


@app.route('/')
def update_redis():
    executor.submit(do_update)
    return 'ok'


def do_update():
    # time.sleep(3)
    print('start update cache')
    # time.sleep(1)
    print("end")


if __name__ == '__main__':
    app.run(debug=True)

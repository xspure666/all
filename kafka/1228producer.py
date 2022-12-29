"""
    生产者代码是线程安全的，支持多线程，而消费者则不然
"""

import time
import json
import datetime
from concurrent.futures import ThreadPoolExecutor
from kafka import KafkaProducer


# 发送json数据
# producer = KafkaProducer(bootstrap_servers=["192.168.10.39:9092"], value_serializer=lambda v: json.dumps(v).encode('utf-8'), api_version=(0, 10))

# 发送普通数据
def send():
    try:
        producer = KafkaProducer(bootstrap_servers=["192.168.1.133:9092"])
        print("connect to kafka sucessful!")
    except Exception as e:
        print("connnect to kafka failed", e)
    i = 0
    for m in range(900):
        i += 1
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(time_now, i)
        message = time_now.join(str(i))
        result = {
            "key": str(i)
            # "value": time_now
        }

        # 向指定分区生产json数据
        # producer.send("testTopic", result, partition=0).get(timeout=30)
        # 生产key-value数据，不指定分区
        producer.send("testTopicPartition", key=b'msg%d' % i, value=str.encode(message))

    # time.sleep(3)


if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="kafka_km")  # 我们使用线程池统一管理线程
    for i in range(2):
        thread_pool.submit(send)  # 把四个线程全部投入读取数据的部分

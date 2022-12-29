from kafka import KafkaConsumer
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from kafka.structs import TopicPartition
from elasticsearch_1 import write_es


class MultiThreadKafka(object):

    def __init__(self):
        self.seek = 0  # 偏移量

    def operate(self):
        consumer = KafkaConsumer('testTopicPartition', bootstrap_servers='192.168.1.133:9092', group_id='lmt',
                                 auto_offset_reset='latest')
        while True:
            for msg in consumer:
                message = {"message": msg.value.decode()}
                write_es.write('lmt', message)
                # print(msg.value.decode())
                print('offset:', msg.offset)
        # tp = TopicPartition("testTopicPartition", 0)
        # consumer.assign([tp])
        # while True:
        #     consumer.seek(tp, 3000)
        #     self.seek += 1
        #     consumer_data = next(consumer)
        #     print(threading.current_thread().name)  # 打印线程名
        #     print(consumer_data)  # 打印
        #     # time.sleep(1)

    def main(self):
        thread_pool = ThreadPoolExecutor(max_workers=3, thread_name_prefix="threading_")  # 我们使用线程池统一管理线程
        for i in range(3):
            thread_pool.submit(self.operate, )  # 把四个线程全部投入读取数据的部分


if __name__ == '__main__':
    thread_kafka = MultiThreadKafka()
    thread_kafka.main()

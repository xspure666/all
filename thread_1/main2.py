# coding:utf-8
import threading
import time


def job1():
    # 让这个线程多执行几秒
    print("执行线程：", threading.Thread.name)
    time.sleep(2)
    print("the number of T1 is %s" % threading.current_thread())
    print(" the thread name is :", threading.Thread.name)


if __name__ == "__main__":
    # 创建一个新的线程
    print("start_thread")
    new_thread = threading.Thread(target=job1, name="T1")
    # new_thread_1 = threading.Thread(target=job1, name="T2")
    # 启动新线程
    new_thread.start()
    new_thread.join()
    print("finnish_thread")
    # new_thread_1.start()
    # print("当前线程数量为", threading.active_count())
    # print("所有线程的具体信息", threading.enumerate())
    # print("当前线程具体信息", threading.current_thread())
    # # new_thread.join()
    # new_thread_1.join()

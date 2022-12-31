from multiprocessing import Process  # 多进程的类
import time
import random


def test_fun(name):
    # 随机等待1~5秒
    time.sleep(random.randrange(1, 5))
    print(f"我是{name}子进程！")


# 进程一定要写在“if __name__ == '__main__':”下面
if __name__ == '__main__':
    process_list = []  # 存放开启的进程
    for i in range(3):
        # 进程中的参数args表示调用对象的位置参数元组.注意：元组中只有一个元素时结尾要加","逗号
        p = Process(target=test_fun, args=(f"son{i + 1}",))
        p.start()
        process_list.append(p)
    for i in process_list:
        i.join()  # 阻塞每个子进程，主进程会等待所有子进程结束再结束主进程
    print("主进程结束！")

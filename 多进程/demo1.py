import multiprocessing
import time



def P1(q):
    print(time.asctime(), "准备向que中put数据")
    time.sleep(5)
    q.put("world")


def P2(q):
    print(time.asctime(), "正在从que中读取数据")
    s = q.get()
    print(time.asctime(), "数据拿到了，是", s)


def Hello():
    # 创建一个queue对象
    que = multiprocessing.Queue()

    # 创建一个进程，调用P1方法
    multiprocessing.Process(target=P1, args=(que,)).start()
    # 创建一个进程，调用P2方法
    multiprocessing.Process(target=P2, args=(que,)).start()

Hello()

# coding:utf-8
import threading
import time
import random
import multiprocessing

lock = threading.Lock()
# lock2 = multiprocessing.Lock()


def stu1():
    print("stu1开始选课")
    global course, lock
    lock.acquire()
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu1选课成功,现在篮球课所剩名额为%d" % course)
    else:
        time.sleep(2)
        print("stu1选课失败，篮球课名额为0，请选择其他课程")
    lock.release()


def stu2():
    print("stu2开始选课")
    global course, lock
    lock.acquire()
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu2选课成功,现在篮球课所剩名额为%d" % course)
    else:
        time.sleep(2)
        print("stu2选课成功篮球课所剩名额为%d" % course)
    lock.release()


def stu3(name):
    print("学生：%s开始选课..............." % name)
    time.sleep(2)
    global course, lock
    lock.acquire()
    if course > 0:
        course -= 1
        # time.sleep(2)
        print("%s：选课成功篮球课所剩名额为%d" % (name, course))
    else:
        # time.sleep(2)
        print("%s：选课失败，篮球课名额为0，请选择其他课程" % name)
    lock.release()
    # time.sleep(1)


if __name__ == "__main__":
    # 篮球课名额
    course = 10
    print("初始化篮球名额为： ", course)
    stu_list = ['张一', '李二', '张三', '李四', '张五', '李6', '张7', '李8', '张9', '李10', '张11', '李12']
    for i in random.sample(stu_list, len(stu_list)):
        # for i in range(1, 20):
        t = threading.Thread(target=stu3, kwargs={'name': i})
        t.start()

    # for i in random.sample(stu_list, len(stu_list)):
    #     # for i in range(1, 20):
    #     t = multiprocessing.Process(target=stu3, kwargs={'name': i})
    #     t.start()
        # t.join()
    # T1 = threading.Thread(target=stu1, name="T1")
    # T2 = threading.Thread(target=stu2, name="T2")
    # T3 = threading.Thread(target=stu3, name="T3")
    # T4 = threading.Thread(target=stu3, name="T4")
    # T1.start()
    # T2.start()
    # T3.start()
    # T4.start()
    # T1.join()
    # T2.join()
    # T3.join()
    # T4.join()
    print("选课结束")

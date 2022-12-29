import threading


def thread_info():
    print(threading.activeCount())
    print(threading.active_count())
    print(threading.current_thread().name)
    print(threading.Thread.setName("Hell0"))
    print(threading.current_thread().name)


if __name__ == '__main__':
    thread_info()

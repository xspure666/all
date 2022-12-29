# 导入socket库
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import time

# 客户端

socket_client2 = None


def connect():
    global socket_client2
    server2 = ("192.168.1.133", 8088)
    socket_client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client2.settimeout(3)
    try:
        print("链接服务器")
        socket_client2.connect(server2)
        print("链接服务器成功")
        return socket_client2
    except Exception as message:
        print('连接服务器报错%s' % message)
        time.sleep(1)
    else:
        print('连接服务器成功')


def send_to_server(msg):
    global socket_client2
    try:
        socket_client2.send(msg.encode("gbk"))
        print(socket_client2.recv(1024).decode("utf-8"))
    except Exception as e:
        print("connect failed to server, 延时10秒后重新连接", e)
        time.sleep(10)
        connect()


if __name__ == '__main__':
    connect()
    # thread_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="kafka_km")
    i = 0
    start_time = time.time()
    while True:
        i = i + 1
        # for _ in range(4):
        t1 = threading.Thread(target=send_to_server(str(i)))
        t1.start()
        if i == 10000:
            print(f"耗时：{time.time() - start_time}")
            exit(0)
        else:
            print(type(i), i)
        # print(thread_pool)
        # if i == 100:i = i + 1
        #     exit(0)
        # send_to_server(str(i))

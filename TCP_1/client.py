# 导入socket库
import socket
import threading
import time


# 客户端


def connect():
    server2 = ("192.168.1.133", 8088)
    socket_client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    num = 0
    try:
        socket_client2.connect(server2)
        while True:
            num += 1
            msg = 'client_1 %d' % num
            socket_client2.send(msg.encode("gbk"))
            print(socket_client2.recv(1024).decode("utf-8"))
            # print('send ok')
    except Exception as message:
        print('连接服务器报错%s' % message)
        time.sleep(1)
    else:
        print('连接服务器成功')
        #     break    while True:
        # server2 = ("127.0.0.1", 8080)
        # # global socket_client2
        # socket_client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # try:
        #     socket_client2.connect(server2)
        #     return socket_client2
        # except Exception as message:
        #     print('连接服务器报错%s' % message)
        #     time.sleep(1)
        #     continue
        # else:
        #     print('连接服务器成功')
        #     break


#
# def send_to_server(msg):
#     socket_client2 = connect()
#     socket_client2.send(msg.encode("gbk"))
#     print('发送给服务器的消息：%s' % msg)
#
#
# def main():
#     for i in range(999):
#         if i % 2 == 0:
#             try:
#                 send_to_server(str(i))
#                 time.sleep(1)
#             except Exception as message:
#                 print('消息发送失败%s' % message)
#                 time.sleep(2)
#                 connect()


if __name__ == '__main__':
    connect()
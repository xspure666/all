# 导入模块
import socket
import threading
import multiprocessing
import json
import asyncio
import aiofiles
from concurrent.futures import ThreadPoolExecutor


async def wite_to_file(info):
    async with aiofiles.open("./abc.txt", "a+", encoding="utf-8") as f:
        await f.write(info)
        print("异步写入成功")


# 接收消息
def recv(client_socket):
    ip_port = 8088
    while True:
        client_text = client_socket.recv(1024)
        print("***********", client_text)
        # 如果接收的消息长度不为0，则将其解码输出
        if client_text:
            print("接收到的消息序列号：", client_text)
            # 给客户端响应
            client_socket.send(("收到 %s\n" % client_text).encode('utf-8'))
        # 当客户端断开连接时，会一直发送''空字符串，所以长度为0已下线
        else:
            print("客户端", ip_port, "已下线")
            client_socket.close()
            break


# 程序主入口
def main():
    # 创建TCP套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_socket.bind(("0.0.0.0", 8088))
    # 设置为被动监听状态，128表示最大连接数
    tcp_socket.listen(128)

    pool = ThreadPoolExecutor(max_workers=1)
    while True:
        try:
            client_socket, ip_port = tcp_socket.accept()
            # 等待客户端连接
            print("[新客户端]:", ip_port, "已连接")
            for i in range(1, 2):
                t = multiprocessing.Process(target=recv, args=(client_socket,))
                print(t.name, "接收数据")
                t.start()
                # t1 = threading.Thread(target=recv, args=(client_socket,))
                # t2 = threading.Thread(target=recv, args=(client_socket,))
                # t3 = threading.Thread(target=recv, args=(client_socket,))
                # pool.submit(recv, client_socket)
                # # 设置线程守护
                # # t1.setDaemon(True)
                # # 启动线程
                t1.start()
                t3.start()
                t2.start()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()

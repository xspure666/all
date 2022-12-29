import os, sys, time
import socket


def connect(server, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)

    connect = False
    while True:
        try:
            if connect == False:
                client.connect((server, port))
                connect = True
            client.send(bytes('hello I am in', 'UTF-8'))
            return client
            print("ok")
        except socket.error as e:
            print("Address-related error connecting to server: %s" % e)
            print("faile===", client)
        time.sleep(5)


def sendtoserver():
    client = connect('127.0.0.1', 8081)
    print("??", str(client))
    if 'raddr' in str(client):
        print("ok")
    else:
        print("client failed")
        client = connect('127.0.0.1', 8081)
    while True:
        client.send(bytes('hello I am in', 'UTF-8'))
        print(client.recv(1024).decode('utf-8'))
        time.sleep(1)
    # print("client", client)
    # while True:
    #     client.send(bytes('dfdsafd', 'UTF-8'))
    #     time.sleep(1)


if __name__ == "__main__":
    sendtoserver()

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 5000))  # 三次握手发生的地方,和server的accept方法建立链接

while True:
    inp = input(">>>")
    sk.send(inp.encode('utf-8'))

    msg = sk.recv(1024).decode('utf-8')  # 从服务器接收信息
    if msg.upper() == 'Q':
        break
    print(msg)  # 再打印

sk.close()

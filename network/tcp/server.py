import socket
import threading

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # created a socket sk,(IPV4, TCP)

"""
localhost 代表什么？
localhost 是一个特殊的主机名，指向当前计算机本身。
它与 127.0.0.1 是等效的。也就是说，localhost 是通过 DNS（域名系统）解析成 127.0.0.1，这是一个 回环地址，用于在本地进行网络通信，而不需要访问外部网络。
2. localhost 的作用
当你使用 localhost 时，服务器只会接受来自本地计算机的连接请求，而不会从外部网络（例如互联网）接收连接。这意味着：

你的服务器只能被 同一台机器上的客户端 访问。
如果你希望其他机器（通过网络）访问这个服务器，你需要使用机器的实际 局域网IP地址 或 公网IP地址。
"""
sk.bind(('localhost', 5000))  # represent my own ip or 192.168.0.x own ip or
print("successful bind", flush=True)  # 强制输出

sk.listen()  # 使服务器进入监听模式，等待客户端的连接请求。
print("Server is listening, waiting for connection...", flush=True)

while True: # 和一个人聊完再跟另一个人聊

    conn, addr = sk.accept()  # 等待接电话 等待建立链接，三次握手就发生在这里， 这里会有一个阻塞，一直等到有客户端建立连接才会往下执行代码
    print("A new client has connected")
    """
    新建立了一个socket对象，accept（）返回了一个新的对象
    accept() 方法是一个 阻塞操作，它会让服务器 等待 客户端连接。当有客户端请求连接时，accept() 返回一个 新的socket对象（conn），用于与该客户端进行通信，同时返回客户端的 地址信息（addr）。
    conn：这是一个新的 套接字对象，专门用于和这个连接的客户端进行数据交换（收发数据）。每个连接的客户端都会有自己独立的通信通道。
    addr：这是客户端的IP地址和端口号信息，用于标识连接的客户端。
    
    """
    while True: # 想说多就说多久
        msg = conn.recv(1024).decode("utf-8")
        if msg.upper() == "Q":
            break
        print(msg)

        inp = input(">>>")
        conn.send(inp.encode('utf-8'))
        if inp.upper() == 'Q':
            break

    conn.close()  # 挂电话

sk.close()  # 关机

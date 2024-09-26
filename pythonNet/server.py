import socket
import threading

# 保存所有已连接的客户端
clients = []

# 创建并打开日志文件
log_file = open('output.txt', 'w')


def log_message(message):
    """将消息写入日志文件并打印到控制台"""
    print(message)
    log_file.write(message + '\n')
    log_file.flush()  # 立即将内容写入文件


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字（IPV4，TCP）
sk.bind(('localhost', 5000))  # 绑定到localhost和端口5000
log_message("successful bind")  # 写入日志并打印

sk.listen()  # 使服务器进入监听模式，等待客户端的连接请求。
log_message("Server is listening, waiting for connection...")


# 处理消息广播
def broadcast(message, current_client):
    # 遍历所有客户端，将消息发送给除了当前客户端以外的其他客户端
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)


# 移除已断开的客户端
def remove(client):
    if client in clients:
        clients.remove(client)


# 处理每个客户端的通信逻辑，放入线程中
def handle_client(conn, addr):
    log_message(f"A new client has connected from {addr}")
    clients.append(conn)  # 将新连接的客户端添加到列表中

    while True:  # 想说多就说多久
        try:
            msg = conn.recv(1024)
            if not msg:
                break  # 如果没有收到消息，表示客户端断开连接
            decoded_msg = msg.decode("utf-8")
            log_message(f"Received from {addr}: {decoded_msg}")

            # 检查客户端是否发送了 /quit 以断开连接
            if decoded_msg == "/quit":
                log_message(f"Client {addr} requested to disconnect.")
                break

            # 广播消息给其他客户端
            broadcast(msg, conn)
        except:
            break

    log_message(f"Client {addr} has disconnected.")
    remove(conn)  # 客户端断开时，将其从列表中移除
    conn.close()  # 关闭连接
    log_message(f"Connection with {addr} closed.")


# 循环接受多个客户端的连接
while True:
    conn, addr = sk.accept()  # 等待客户端连接
    # 每当有新的客户端连接时，创建一个新的线程来处理该客户端的通信
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()  # 启动线程，处理客户端请求

# 关闭日志文件
log_file.close()

sk.close()  # 关机


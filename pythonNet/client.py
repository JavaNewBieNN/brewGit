import socket
import threading

# output file path
output_file = "output.txt"

# 创建 output.txt 文件，并写入 HawkID 和姓名
with open(output_file, "w") as f:
    f.write("HawkID: nnie\n")
    f.write("Name: Ning Nie\n\n")

# 现在可以继续添加 log_message 函数，将日志追加写入文件
def log_message(message):
    """将消息写入日志文件并打印到控制台"""
    print(message)  # 打印到控制台
    with open(output_file, "a") as f:  # 以追加模式写入日志
        f.write(message + '\n')

# 你的服务器代码继续运行...

# 处理从服务器接收的消息
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                log_message(f"Server broadcast: {message}")
            else:
                break
        except:
            break


# 连接到服务器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))
log_message("Connected to the server")

# 启动一个新线程接收消息
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# 发送消息给服务器
while True:
    message = input("You: ")

    # 当输入 '/quit' 时，客户端断开连接并优雅退出
    if message == "/quit":
        client_socket.send(message.encode('utf-8'))  # 向服务器发送退出命令
        log_message("You have disconnected from the server")
        break

    client_socket.send(message.encode('utf-8'))
    log_message(f"You: {message}")

client_socket.close()



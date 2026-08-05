import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addres = ('127.0.0.1', 12345)
client_socket.connect(server_addres)

message = "Привет, сервер!1"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
# print(f"Ответ от сервера: {response}")
print(response)

client_socket.close()
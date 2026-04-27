import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

client_socket.send("Привет, сервер!".encode())
print(client_socket.recv(1024).decode())

client_socket.close()

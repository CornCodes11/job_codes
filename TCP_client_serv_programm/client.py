import socket

HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to server")

client_socket.send("Hello Server! This is client.".encode())

data = client_socket.recv(1024).decode()
print("Server says:", data)

client_socket.close()

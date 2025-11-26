import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT} ...")

conn, addr = server_socket.accept()
print("Connected by", addr)

data = conn.recv(1024)
print("Client says:", data.decode())

conn.send("Hello Client! Message received.".encode())

conn.close()
server_socket.close()

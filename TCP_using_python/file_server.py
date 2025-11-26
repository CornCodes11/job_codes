import socket

HOST = '127.0.0.1'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server ready... Waiting for client...")

conn, addr = server.accept()
print("Connected:", addr)

filename = conn.recv(1024).decode()
print("Client requested:", filename)

try:
    f = open(filename, "rb")
    data = f.read()
    conn.sendall(data)
    print("File sent successfully.")
except:
    conn.send(b"ERROR: File not found")

conn.close()
server.close()

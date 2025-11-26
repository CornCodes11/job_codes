import socket

HOST = '127.0.0.1'
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to server")

filename = "sample.txt"     # file you want
client.send(filename.encode())

data = client.recv(100000)  # large buffer
if b"ERROR" in data:
    print("File not found.")
else:
    with open("received.txt", "wb") as f:
        f.write(data)
    print("File received and saved as received.txt")

client.close()

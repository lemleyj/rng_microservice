import socket

HOST = "127.0.0.1"
PORT = 65432

messages = [" ", "(0, 10)", "[111, 222, 333]"]

user_choice = input("What message would you like to send?? 0, 1, or 2")

message = messages[int(user_choice)]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Client sending: {message}")
    s.sendall(bytes(message, 'utf-8'))
    data = s.recv(1024)

print(f"Received from server: {data.decode('utf-8')}")

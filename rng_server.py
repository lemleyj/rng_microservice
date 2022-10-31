## Name: John Lemley
## Description: A microservice that generates a random number and returns it to the user. 

import socket 
import random
from ast import literal_eval

PORT_CHECK = input("Would you like to change the PORT? y for yes, anything else for no")

if PORT_CHECK != 'y':
    PORT = 65432
else:
    PORT = input("What would you like to change the port to?")

HOST = "127.0.0.1"

print(f"Starting server at HOST: {HOST}, PORT: {PORT}")
print(f"TO USE: ")
print(f" - if provided with a blank string, the server will return a random number between 0-10000.")
print(f" - if provided with a range as a tuple [i.e. (0, 10)], the server will return a random number between provided range.")
print(f" - if provided with a list of objects (i.e. [111, 222, 333]), the server will return a random object from the list.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn: 
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            
            if not data:
                break
            

            print(f"rx'd: {data}")

            data = data.decode('utf-8')

            if data == " ":
                random_num = random.randrange(10000)
                return_data = bytes(str(random_num), 'utf-8')
                print(f"sending {random_num}")
                conn.sendall(return_data)

            elif data.startswith("(") and data.endswith(")"):
                data = literal_eval(data)
                random_num = random.randrange(data[0], data[1])
                return_data = bytes(str(random_num), 'utf-8')
                print(f"sending {random_num}")
                conn.sendall(return_data)

            elif data.startswith("[") and data.endswith("]"):
                data = literal_eval(data)
                random_num = random.randrange(len(data))
                return_data = bytes(str(data[random_num]), 'utf-8')
                print(f"sending {data[random_num]}")
                conn.sendall(return_data)
                

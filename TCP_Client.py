import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'

port = 4444

client_socket.connect((host, port))

recieved = client_socket.recv(1024)

recieved_text = recieved.decode('utf-8')

print(recieved_text)

client_socket.close()

# Load the network toolbox
import socket

# Buy a new "phone": IPv4 addresses (AF_INET), reliable connection (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Used for reusing they same address without wait something like that 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# '0.0.0.0' means "accept visitors coming from any of my addresses"
host = '0.0.0.0'

# The "apartment number" visitors must use to reach this program
port = 4444

# Attach the phone to this number. Note the DOUBLE parentheses:
# the outer ones belong to bind(), the inner ones make the (host, port) pair
server_socket.bind((host, port))

# Start waiting for visitors. Up to 3 can wait in line.
server_socket.listen(3)
print(f"Server is waiting on port {port}...")

# Repeat forever, so the server keeps serving visitors
while True:
    # Freeze here until someone connects.
    # clientsocket = the new line for THIS visitor
    # address = the visitor's (IP, port)
    clientsocket, address = server_socket.accept()

    # Log who connected. The f before the quote lets {address} be filled in.
    print(f"received connection from {address}")

    # The greeting. \r\n marks "end of message"
    message = 'hello! Thank you for connecting to the server' + "\r\n"

    # Translate text into bytes (.encode), then send ALL of it (sendall)
    clientsocket.sendall(message.encode('utf-8'))

    # Hang up on this visitor. The () is what actually presses the button!
    clientsocket.close()

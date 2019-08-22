import socket              

s = socket.socket()         # Create a socket object
host = socket.gethostname()  
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024))
s.send("still connected")
s.close                     # Close the socket when done

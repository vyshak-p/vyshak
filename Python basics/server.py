import socket

s = socket.socket()         
host = socket.gethostname() # Getting local host 
port = 12345                
s.bind((host, port))        

s.listen(5)  # Queue of 5               
while True:
   c, addr = s.accept()     # c=client socket object
   print ('Got connection from', addr)
   c.send("Thank you for connecting")
   print (c.recv(1024))
   c.close()

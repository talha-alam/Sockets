import socket

c = socket.socket()

c.connect(('localhost',63603))

name = input("Enter your name")

c.send(bytes(name,'utf-8'))

while 1: 
   incoming_messagge=c.recv(1024)
   incoming_messagge = incoming_messagge.decode()
   print(" Server :", incoming_messagge)
   message= input(str(">>"))
   message = message.encode()
   c.send(message)
   print(" message has been sent...")

print(c.recv(1024).decode())



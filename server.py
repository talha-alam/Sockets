import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost',63603))

s.listen(3)
print('waiting for connection')

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr,name)
    
    while 1:

        display_mess= input(str(">>"))
        display_mess=display_mess.encode()
        c.send(display_mess)
        print(" message has been sent...")
        in_message=c.recv(1024)
        in_message=in_message.decode()
        print(" Client:", in_message)

    c.send(bytes('Welcome to Talhassee','utf-8'))

    c.close()

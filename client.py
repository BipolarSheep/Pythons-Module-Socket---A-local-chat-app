import socket
import sys
import time

x=socket.socket()
h_name= input(str(" Enter the hostname of the server: "))
port = 8080

x.connect((h_name,port))
print("Connected to chat server")

while 1:
    incoming_message=x.recv(1024)
    incoming_message=incoming_message.decode()
    print("Anonymous :", incoming_message)
    message = input(">> ")
    Message = message.encode()
    x.send(Message)
    print(" message has been sent...")

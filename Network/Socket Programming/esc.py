import socket
import pandas as pd 
import numpy as np

SERVER= socket.gethostname()
PORT=9999

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER,PORT))

client.send(bytes("Client ",'utf-8'))


Connected = True
while Connected:
    sm=client.recv(1024).decode('utf-8')
    print(sm)
    ch = input()
    if ch == "I":
        client.send(bytes(ch, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
        d=input()
        client.send(bytes(d, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
        f=input()
        client.send(bytes(f, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
        q=input()
        client.send(bytes(q, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
        c=input()
        client.send(bytes(c, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
    elif( ch == "M"):
        client.send(bytes(ch, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
    elif(ch == "V"):
        client.send(bytes(ch, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
    elif(ch == "U"):
        client.send(bytes(ch, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
    elif(ch == "F"):
        client.send(bytes(ch, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
        f=input()
        client.send(bytes(f, "utf-8"))
        r = client.recv(1024).decode()
        print(r)
    
client.close()









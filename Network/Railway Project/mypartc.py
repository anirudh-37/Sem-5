import socket
import threading 
import random
import string
import pandas as pd 
import numpy as np




SERVER= socket.gethostname()
PORT=9999

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER,PORT))
message = "Client - 1"
message = message.encode('utf-8')
client.send(message)

def send():
    while True:
        rm=client.recv(1024).decode('utf-8')
        print(rm)
        msgts=input()
        msgts=msgts.encode('utf-8')
        client.send(msgts)
       
send()
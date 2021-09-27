from datetime import date, datetime
import socket
import threading 
import random
import string
import pandas as pd 
import numpy as np


SERVER= socket.gethostname()
PORT=9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((SERVER,PORT))

df=pd.read_excel("Cancellation.xlsx")

def client_handle(c,addr):
    connected=True
    x=None
    r = c.recv(1024).decode('utf-8')
    print(r + " connected !")
    while connected:
        cm="Welcome to Cancellation Department"+ "\n" + "Enter Your Name: "
        cm=cm.encode('utf-8')
        c.send(cm)
        name=c.recv(1024).decode('utf-8')
        print(name + " Logged in")
        for i in df.index:
            if(df['Name'][i]==name):
                x=i
        if x!=None:
            cm="User Found, Enter Regtration Number: "
            cm=cm.encode('utf-8')
            c.send(cm)
            x=None
            rno = c.recv(1024).decode('utf-8')
            for i in df.index:
                if(df['Name'][i] == name and df['Regno.'][i]== int(rno)):
                    x = i
            if(x != None):
                cm = "Registration number confirmed :" + "\n" + " Are you sure you want to cancel the ticket ?(Y/N): "
                cm = cm.encode('utf-8')
                c.send(cm)
                a = c.recv(1024).decode('utf-8')
                if(a == 'Y'):
                    df['Status'][x] = 'Cancelled'
                    
                    cm = "Reservation Cancelled "+"\n"+" Thank You!" +"\n"+" Half of the ticket price will be returned. " + "\n" + "Enter Y to continue and diplay the details: " 
                    cm = cm.encode('utf-8')
                    c.send(cm)
                    a = c.recv(1024).decode('utf-8')
                    y = df['Cost'][x]
                    df['Return'][x] = y/2
                    
                    for i in df.index:
                        Cost = df['Cost'][i]
                        Ret = df['Return'][i]
                        df['Total Pay'][i] = int(Cost) - int(Ret)
                    j = df.iloc[x].to_string()
                    cm = j + "\n"  "Do you want to cancel more (Y/N) ?"
                    cm = cm.encode('utf-8')
                    c.send(cm)
                    df.to_csv("Cancellation.csv", index=False)
                    a = c.recv(1024).decode('utf-8')
                    if(a == "N"):
                        connected = False
                        cm="Thank You! " 
                        cm=cm.encode('utf-8')
                        c.send(cm)


                elif(a == 'N'):
                    cm = "Reservation not Cancelled " +"\n"+" Thank You!" + "\n" +"Do you want to continue (Y/N) ?  "
                    cm = cm.encode('utf-8')
                    c.send(cm)
                    a = c.recv(1024).decode('utf-8')
                    if(a == "N"):
                        connected = False
                        cm="Thank You! " 
                        cm=cm.encode('utf-8')
                        c.send(cm)

                        
                    
            elif x == None:
                cm="Your Ticket Was Not Reserved: " + "\n" + "Do you want to cancel other tickets (Y/N)? "
                cm=cm.encode('utf-8')
                c.send(cm)
                a = c.recv(1024).decode('utf-8')
                if(a == "N"):
                    connected = False
                    cm="Thank You! " 
                    cm=cm.encode('utf-8')
                    c.send(cm)


        elif x == None:
            cm="Your Ticket Was Not Reserved: " + "\n" + "Do you want to cancel other tickets (Y/N)? "
            cm=cm.encode('utf-8')
            c.send(cm)
            a = c.recv(1024).decode('utf-8')
            if(a == "N"):
                connected = False
                cm="Thank You! " 
                cm=cm.encode('utf-8')
                c.send(cm)

    print("-------------------------Changes Done----------------------")
    print("\n")

 
    c.close()
def start():
    server.listen()
    print("[Server] Listening..")
    while True:
        c,addr=server.accept()
        t=threading.Thread(target=client_handle,args=(c,addr))
        t.start()

    

print("[SERVER] Starting!")

start()
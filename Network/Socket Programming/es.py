import socket
import threading 
import pandas as pd 
import numpy as np

SERVER= socket.gethostname()
PORT=9999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server.bind((SERVER,PORT))
except socket.error as e:
    print(str(e))

print("[SERVER] listening..")
server.listen(5)
df = pd.DataFrame(pd.read_csv("edata.csv"))
df.set_index(['Date', 'foodid', 'Category', 'Quantity', 'cost', 'Totalcost'])
def client_handle(c,addr):
    fc = c.recv(1024).decode('utf-8')
    print(fc," connected")
    while True:
        
        foc="Welcome to Server, Enter values I,M,V,U or F "
        c.send(foc.encode('utf-8'))
        ch = c.recv(1024).decode('utf-8')
        if(ch == "I"):
            data=[]
            message1="Enter Date"
            c.send(message1.encode('utf-8'))
            date= c.recv(1024).decode('utf-8')
            data.append(date)

            message1 = "Enter food-id"
            c.send(message1.encode())
            fid = c.recv(1024).decode('utf-8')
            data.append(fid)

            if(fid[0] == "D"):
                data.append("Dosa")
            elif(fid[0] == "A"):
                data.append("Apple")
            elif(fid[0] == "B"):
                data.append("Briyani")
            elif(fid[0] == "I"):
                data.append("Italian")

            message1 = "Enter Quantity"
            c.send(message1.encode('utf-8'))
            qty= c.recv(1024).decode('utf-8')
            data.append(qty)

            message1 = "Enter Cost"
            c.send(message1.encode('utf-8'))
            cost = c.recv(1024).decode('utf-8')
            data.append(cost)

            q=int(qty)
            n=int(cost)
            tot=q*n
            data.append(tot)

            print(data)
            l=len(df)
            df.loc[l] = data
            j = df.to_string()
            c.send(j.encode('utf-8'))
            df.to_csv('edata.csv', index=False)
        elif(ch == "M"):
           # x = df['Quantity']
           # y = df["cost"]
            df['Totalcost']=df['Quantity']*df["cost"]
            df.to_csv("edata.csv",index=False)
            str=df.to_string()
            c.send(str.encode('utf-8'))
        elif(ch == "V"):
            j = df.to_string()
            c.send(j.encode('utf-8'))
            continue 
        elif(ch == "U"):
            for i in range(len(df)):
                x = df.loc[i,'foodid'][0]
                if x == 'A':
                    df.loc[i,'Category'] = "Apple"
                elif x == 'B':
                    df.loc[i,'Category'] = "Biryani"
                elif x == 'D':
                    df.loc[i,'Category'] = "Dosa"
                elif x == 'I':
                    df.loc[i,'Category'] = "Italian"
            df.to_csv("edata.csv",index = False)
            j = df.to_string()
            c.send(j.encode('utf-8'))
        elif(ch == "F"):
            message1 = "Enter food-id"
            c.send(message1.encode('utf-8'))
            fid = c.recv(1024).decode('utf-8')
            data = df.loc[df['foodid'] == fid]
            data = data.to_string()
            c.send(data.encode('utf-8'))

            '''for i in range(len(df)):
                if(df.loc[i,'foodid'] == fid):'''




            
                
def start():
    server.listen()
    while True:
        c,addr=server.accept()
        t=threading.Thread(target=client_handle,args=(c,addr))
        t.start()

print("[SERVER] Starting!")
start()
server.close()
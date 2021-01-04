# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:55:35 2020

@author: beaurezm
"""


import socket
import select
import sys
import json


from threading import Thread
global test


hote='192.168.118.106'
port=1933
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((hote,port))
    print("connecte")
    ok=input(">")
    oui=input(">")
    non=input(">")
    Photo={"R":ok,"G":oui,"B":non}
    Photo=json.dumps(Photo)

   
    client.sendall(bytes(Photo,encoding="utf-8"))
    try:
        test=client.recv(1024)
        test=test.decode()
        print(test)
    
    except:
        print("coucou")


    client.close()
except:
    print ("Error")

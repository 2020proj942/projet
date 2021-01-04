# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:55:35 2020

@author: beaurezm
"""
import sys
import os
# import numpy and matplotlib colormaps
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#from skimage import io
import matplotlib.cm as cm

import cv2

###Serveur###
import socket
#from threading import Thread
import sys
import json
import select


from threading import Thread
global test


list_ima = ["01.pgm"]
imtest = Image.open(list_ima[0])
imtest = imtest.resize((400,500))
pix = np.array(imtest)
ok=""
a=0
for i in range (len(pix)):
    for j in range (len(pix[i])):
        if j<(len(pix[i])-1):
            ok=ok+str(pix[i][j])+","
    
        else:
            ok=ok+str(pix[i][j])+";"
           
#print(len(ok))        







hote='192.168.118.106'
port=80
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((hote,port))
#    ok=input(">")
#    oui=input(">")
#    non=input(">")
    Photo={"I":ok}
    Photo=json.dumps(Photo)

   
    client.sendall(bytes(Photo,encoding="utf-8"))

    try:
        test=client.recv(1024)
        test=test.decode()
        print(test)

    
    except:
        pass
    client.close()
except:
    print ("Error")

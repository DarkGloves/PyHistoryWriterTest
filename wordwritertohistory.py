from ctypes.wintypes import PUSHORT
from operator import truediv
import os
from re import A
import sys

cwd=os.getcwd()
os.chdir(cwd + "\\" + "assets" + "\\" + "data" + "\\")
cwd=os.getcwd()
try:
   doc = open ("history.wtf" , "r+")  
except FileNotFoundError:
     doc = open ("history.wtf" , "w")

a = 100000000
b = 1 
for b in range (a) :
    doc = open("history.wtf" , "r+")    
    objects1 = 0
    objects2 = len(doc.readlines())

    for objects1 in range (objects2):
        (doc.readline())
        objects1 = objects1 + 1

    wordwrite = input("input here a word to write, then press ENTER ; do a keyboard interrupt (Ctrl^c) to exit:   ")
    doc.write(str(wordwrite) + "\n")
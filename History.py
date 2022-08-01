import os
import sys

cwd=os.getcwd()
os.chdir(cwd + "\\" + "assets" + "\\" + "data" + "\\")
cwd=os.getcwd()
try:
   doc = open ("history.wtf" , "r+")  
except FileNotFoundError:
     doc = open ("history.wtf" , "w")

doc = open ("history.wtf" , "r+")
objects1 = 0
objects2 = len(doc.readlines())
doc = open ("history.wtf" , "r")

if (len(doc.readline())) == 0:
    print("('empty')")
else:
    doc = open ("history.wtf" , "r")
    for objects1 in range (objects2):
        print(doc.readline())
        objects1 = objects1 + 1
    

print("\r")
print("\r")

input("press ENTER")
exit()

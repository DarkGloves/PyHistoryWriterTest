import os

cwd=os.getcwd()
os.chdir(cwd + "\\" + "assets" + "\\" + "data" + "\\")
cwd=os.getcwd()
try:
    os.remove("history.wtf")
except FileNotFoundError:
    print("*History is already clean")

input("-Done, press ENTER or Ctrl^c to exit")
exit()

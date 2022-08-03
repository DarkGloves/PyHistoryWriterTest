#from optparse import Option
#from turtle import title
from unicodedata import name
from pyfiglet import figlet_format
from termcolor import colored
import time
import pytempfile
import os
from os import system, name

#code starts here xd
timeskeeeeeep = 0
pytempfile.gototempdir() 
num1 = 1
num2 = 1 
num1 == num2
while True:

    if name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    title1 = ((colored(figlet_format("PyTempFileTest"), color="blue")))
    print(title1)
    print("\t By @ItzJustMangelBTW & @AlbertoV1388")   
    if timeskeeeeeep == 0:
        time.sleep(5)
    else:
        time.sleep(0.5)
    timeskeeeeeep = 1
    print("\t Select Option: \n\t1) Write Word to History\n\t2) View History\n\t3) Clear History\n\t4) Exit")
    optionN = int(input("Select Option: "))
    time.sleep(0.1)
    print(optionN)
    if optionN == 1:
        #exec(open("wordwritertohistory.py").read())
        pytempfile.writetempfile()
    elif optionN == 2:
        pytempfile.readtempfile()
    elif optionN == 3:
        pytempfile.cleantempfile()
    elif optionN == 4:
        break
quit()




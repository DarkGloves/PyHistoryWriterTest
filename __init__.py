#from optparse import Option
#from turtle import title
import clearhistory
import History
from pyfiglet import figlet_format
from termcolor import colored
import time

title1 = ((colored(figlet_format("PyHistoryWriterTest"), color="blue")))
print(title1)
print("\t By @ItzJustMangelBTW & @AlbertoV1388")    
time.sleep(5)
print("\t Select Option: \n\t1) Write Word to History\n\t2) View History\n\t3) Clear History\n\t4) Exit")
optionN = int(input("Select Option: "))
time.sleep(2)
print(optionN)
if optionN == 1:
    exec(open("wordwritertohistory.py").read())
elif optionN == 2:
    History.history()
elif optionN == 3:
    clearhistory.clean()
elif optionN == 4:
    quit()



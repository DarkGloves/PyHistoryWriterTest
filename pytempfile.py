import os

#====>go to /assets/data, i will do thx more customizable in a future
#====>cwd = current-working-directory uwu
#====>create assets folder
def gototempdir():
    tempcwd = os.getcwd()
    try:
        os.chdir(tempcwd + "\\" + "assets" + "\\" )
    except FileNotFoundError:
        os.mkdir("assets")
        os.chdir(tempcwd + "\\" + "assets" + "\\" )
    tempcwd = os.getcwd
    try:
        os.chdir(os.getcwd() + "\\" + "data" + "\\")
    except FileNotFoundError:
        os.mkdir("data")
        tempcwd = os.getcwd()
        os.chdir(os.getcwd() + "\\" + "data" + "\\")


    os.getcwd()
    #print("==>" + tempcwd)
# def printcwd():
#     tempcwd = os.getcwd()
#     print("==>" + tempcwd)

#======>It reads the file
#======>It will also create the file in case its missing
def readtempfile():
    try:
        tempdoc = open ("history.wtf" , "r+")  
    except FileNotFoundError:
        tempdoc = open ("history.wtf" , "w")

    tempdoc = open ("history.wtf" , "r+")
    readtempvalue1 = 0
    readtempvalue2 = len(tempdoc.readlines())
    tempdoc = open ("history.wtf" , "r")

    if (len(tempdoc.readline())) == 0:
        print("('empty')")
    else:
        tempdoc = open ("history.wtf" , "r")
    for (readtempvalue1) in range (readtempvalue2):
        print(tempdoc.readline())
        readtempvalue1 = readtempvalue1 + 1
    print("\r")
    print("\r")
    input("press ENTER")


#======>It writes a word to the file
#======>It will also create the file in case its missing
def writetempfile():
    try:
        tempdoc = open ("history.wtf" , "r+")  
    except FileNotFoundError:
        tempdoc = open ("history.wtf" , "w")
    tempdoc = open("history.wtf" , "r+")

    readtempvalue1 = 0
    readtempvalue2 = len(tempdoc.readlines())

    for (readtempvalue1) in range (readtempvalue2):
        (tempdoc.readline())
        readtempvalue1 = readtempvalue1 + 1
    wordwrite = input("Input here a word to write, then press ENTER:   ")
    tempdoc.write(str(wordwrite) + "\n")
    input("done, press ENTER")



#finally, lets end thx guys
#========>clean temp file
def cleantempfile():
    try:
        os.remove("history.wtf")
    except FileNotFoundError:
        print("*History is already clean")
    input("-Done, press ENTER")
#finally
#wait line 69 uwu
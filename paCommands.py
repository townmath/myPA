def selfDestruct():
    import time
    text= 'We will self destruct in 5 seconds, terribly sorry for the inconvenience.\n'
    print text
    for x in range(5):
        time.sleep(1)
        text+= str(5-x)+'\n'
        print (5-x)
    text+='boom\n'
    print ('boom')
    return text

def getRandomLine(fileName,maxNum):
    from random import randint
    textFile=open(fileName,'r')
    randNumber=randint(0,maxNum-1)
    for line in range(randNumber+1):
        nextLine=textFile.readline()
        if not nextLine:
            break
    textFile.close()
    return nextLine
    
def jokes():
    #currently 66 jokes in the file
    return getRandomLine('oneLiners.txt',66)

def quotes():
    #12 quotes, I should probably get this from the file, but not right now. 
    return getRandomLine('quotes.txt',12)

if __name__ == "__main__":
    print jokes()
    import time
    selfDestruct()

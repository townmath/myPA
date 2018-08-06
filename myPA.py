import sys  

import datetime
import time

import paCommands

# Credentials
credFileName='cred.txt'
credFile=open(credFileName,'r')
username = credFile.readline().strip()
password = credFile.readline().strip()
toaddrs=credFile.readline().strip()
keyword=credFile.readline().strip()
credFile.close()
fromaddr=username+'@gmail.com'

date = (datetime.date.today() - datetime.timedelta(7)).strftime("%d-%b-%Y")
print date

#thanks to http://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
def checkMail():#checks mail for specific commands
    import imaplib
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username+'@gmail.com', password)
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    #print keyword
    searchText='(SENTSINCE {date} HEADER Subject '+keyword+')'
    result, data = mail.uid('search', None, searchText.format(date=date))

    #print result, data
    #result, data = mail.uid('fetch', data[0][-1], '(BODY[HEADER.FIELDS (SUBJECT)])')# (DATE SUBJECT)]])') # fetch the header for the given ID
    #    Content-Type: text/plain; charset=UTF-8

    try:
    #if True:
        #print result,data
        #print data[0][:2]
        result, data = mail.uid('fetch', data[0][:3], '(BODY[TEXT])')#prints the body tex
        #print mail.uid('fetch', data[0][:3], '(BODY[HEADER.FIELDS (FROM)])')#prints the body tex
        raw_email = data[0][1] # here's the body, which is raw text of the whole email
        returnCnt=0
        body=''
        for char in raw_email:
            if char=="\n":
                returnCnt+=1
            if returnCnt==3:
                body+=char
        body=body.strip().lower()
        print body
        images=False
        if 'self destruct' in body or 'shutdown' in body:
            emailText=paCommands.selfDestruct()
            subject='Self Destruct Sequence'
        elif 'joke' in body:
            emailText=paCommands.jokes()
            subject='Joke'
        elif 'quote' in body:
            emailText=paCommands.quotes()
            subject='Quotable Quote'
        elif 'python' in body:
            emailText=paCommands.runFile(body[7:],'python')
            images="."
            subject='Results'
        else:
            mail.store("1:*", '+X-GM-LABELS', '\\Trash')
        sent=paCommands.sendEmail(subject,emailText,toaddrs,username,password,
                                  images)
        if sent:
            mail.store("1:*", '+X-GM-LABELS', '\\Trash')
    except:
    #else:
        print "no mail yet "+datetime.datetime.now().strftime('%I:%M%p')
    mail.close()
    mail.logout()


while True:
#if True:#testing
    #while datetime.datetime.now().strftime('%a')!='Mon':
    if '06'<=datetime.datetime.now().strftime('%H')<='23':#24 hour clock
        checkMail()
        time.sleep(1200) #so you don't waste precious clock cycles checking, check every 20 min
    else:
        time.sleep(7200)#sleep the night away
    #while datetime.datetime.now().strftime('%a')!='Tue':#dow
    #while datetime.datetime.now().strftime('%I')!='06':#12 hour clock


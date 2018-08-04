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
    import subprocess
    subprocess.Popen(['shutdown','-h','+1','Good day, sir.'])
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

def runFile(filename,command):
    #ie runFile('testing123.py','python')
    print command
    import subprocess
    import time
    isError=False
    curTime=time.clock()#start timer
    entry='File Ran: '+filename+'\n'
    #print (filename)
    data = subprocess.Popen([command,filename],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output=data.stdout.readline().decode()
    ellapsed=time.clock()-curTime
    #print (ellapsed)
    entry+='Time Ellapsed: '+str(ellapsed)+'\n'
    while output:
        entry+=output.strip()+'\n'
        output=data.stdout.readline().decode()
    errData=data.stderr.readline().decode()
    while errData:
        entry+=errData.strip()+'\n'
        errData=data.stderr.readline().decode()
    print entry
    directory=''
    for folder in filename.split('/'):
        if not folder.endswith('.py'):
            directory+=folder+'/'
    return entry+'\n',directory

#https://docs.python.org/2/library/email-examples.html
def addImages(subject,text,toaddrs,fromaddr,images):
    # Here are the email package modules we'll need
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    import os
    import time

    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = subject#'Our family reunion'
    # me == the sender's email address
    # family = the list of all recipients' email addresses
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg.preamble = text

    # Assume we know that the image files are all in PNG format
    tenMinutes=10*60
    for filename in os.listdir(images):
        if filename.endswith(".png") and time.time()-os.path.getctime(filename)<tenMinutes:
            # Open the files in binary mode.  Let the MIMEImage class automatically
            # guess the specific image type.
            fp = open(filename, 'rb')
            img = MIMEImage(fp.read())
            fp.close()
            img.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(img)
    return msg.as_string()

#thanks to https://pbeblog.wordpress.com/category/programming/python/
def sendEmail(subject,text,toaddrs,username,password,images=False):
    import smtplib
    fromaddr=username+'@gmail.com'
    text = "Good morning, sir, you are looking quite well today.  Here is/are your " + subject + ".\n\n" + text
    text += '\nSir, will that be all?'

    if images:
        msg=addImages(subject,text,toaddrs,fromaddr,images)
    else:
        # Prepare actual message
        msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (fromaddr, toaddrs,#", ".join(toaddrs),
               subject, text)
    #try:
    if True:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        #print fromaddr,toaddrs,msg
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        print 'I successfully sent the email'
        return True
    #except:
    else:
        print "Terribly sorry sir, I failed to send the email"
        return False

def testSendEmail():
    # Credentials
    credFileName='cred.txt'
    credFile=open(credFileName,'r')
    username = credFile.readline().strip()
    password = credFile.readline().strip()
    toaddrs=credFile.readline().strip()
    keyword=credFile.readline().strip()
    credFile.close()
    #sendEmail(keyword,"quote",username+"@gmail.com",username,password)
    #sendEmail("testing","123",toaddrs,username,password)
    sendEmail("testing","123",toaddrs,username,password,".")

    
if __name__ == "__main__":
    print quotes()
    fileName='testing123.py'
    runFile(fileName,'python')
    testSendEmail()
    #selfDestruct()

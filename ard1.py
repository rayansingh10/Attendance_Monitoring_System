import openpyx1
import satplib, ssl
import serial

ser=serial.Serial("COM7",9608)
rfidTag=["9A 55 82 Be", "15 28 90 5C","AS EF 91 38","71 98 DA DF"]
rfidName=["TEST", "M.VARUN REDDY", "RAYAN SINGH","VARUN SINGH"] 
rfidEmail=["espArduno@gmail.com", "varunmr2003@gmail.com", "rayanthakur6401@gmail.com","varunsingh2021@vitstudent.ac.in"]

path="test.xlsx"
wbObj=openpyx1.load_workbook(path)
sheetObj=wbObj.active


def isAuth (UID): #function that returns index of the uid
    for i in rfidTag: 
        if i == UID:
            x=rfidTag.index(1) 
            return x
    return -1

## EMAIL CONNECTION
port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email ="esparduno@gmail.com" # Sender email
password = "rsywlixcqxblfyhw"

# SETTING A NEW DATE
def newDate():
    dateStr=input("Enter the date for attendance: colm-sheetObj.max_column #maximum no of columns")# input date 
    colm=sheetObj.max_column
    sheetObj.cell(row=1, column=colm+1) 
    cellObj.value=dateStr
    for x in range(2, len(rfidTag)+2):
        cellObj=sheetObj.cell(row=x, column=colm+1)
        cellObj.value="absent"
    wbObj.save(filename="test.xlsx")
    return dateStr


def markPresent(index): 
    colm=sheetObj.max_column
    cell0bj=sheetObj.cell(row=index+2, column=colm) 
    cell0bj.value="present"
    wbObj.save(filename="test.xlsx")

def addewEntry(index,name):
    colm=sheetObj.max_column
    roww=sheetObj.max_row
    cellObj=sheetObj.cell(row=roww+1,column=1)
    cellObj.value=name
    wbObj.save(filename="test.xlxs")

modeInput = input("""
HELLO WORLD!, TO THE RFID ATTENDANCE SYSTEM

COMMANDS:

1. TO TAKE ATTENDANCE
2. TO QUTI THE PROGRAM

YOUR INPUT:
""")

if int(modeInput)==1:
    #DATE SECTION:
    dateStr2 = newDate()
    while True:
        index = -1
        # line1 = ser.readline().decode().rstrip() #approximate your rfid card to the sensor
        print("Approximate your card... ")
        line1 = ser.readline().decode.strip() #uid tag line
        print("UID: "+line1)
        index = isAuth(line1) # authorisatiion func call
        
        if index == -1:
            print("Access Denied")
            continue
        print("Hello, "+rfidName[index])

        #excel data base updation
        markPresent(index)

        #Email Section
        receiver_email = rfidEmail[index] # enter receiver address
        message = "Marked attendance for "+dateStr2

        context = ssl.create_default_context()
        with smptlib.SMTP_SSL(smtp_server, port, context = context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
else:
    exit()

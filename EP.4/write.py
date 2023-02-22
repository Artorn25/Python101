# ชื่อโปรเเกรม writefile.py
import csv

def writedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('สวัสดี ')

def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        file.writelines(text + '\n')


def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        #data = file.readlines()  # export to list
        data = file.read()
        print(data)

readdata()
#adddata('สมุด')
#adddata('ลูกอม')
#adddata('หมากฝรั่ง')

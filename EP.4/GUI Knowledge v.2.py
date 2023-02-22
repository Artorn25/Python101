from tkinter import *
from tkinter import ttk  # theme of tk
from tkinter import messagebox

import csv

def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerow(datalist)  # datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)  # fr = file reader
        data = list(fr)
    return data

GUI = Tk()  # หน้าจอของโปรเเกรม
GUI.title('โปรเเกรมเก็บข้อมูล')  # ชื่อโปรเเกรม
GUI.geometry('900x500')  # ขนาดโปรเเกรม

background = Label(GUI, bg="blue")
background.pack(fill=BOTH, expand=True)

L1 = Label(GUI, text='โปรเเกรมบันทึกความรู้',
           font=('TH Sarabun New', 20), fg='green')
L1.place(x=250, y=50)

# image
FB1 = LabelFrame(GUI)
FB1.place(x=210, y=100)
image = PhotoImage(file='image.png')
label_1 = Label(FB1, image=image)
label_1.pack()

# text
FB2 = LabelFrame(GUI,font=('TH Sarabun New', 16,"bold"))
FB2.place(x=500, y=95)


text = Text(FB2, font=('TH Sarabun New', 16), height=10, width=80)
text.pack(pady=10, padx=15)
#entry = Entry(FB2)
#entry.pack(ipadx=50, ipady=5)

scroll = ttk.Scrollbar(FB2, orient=VERTICAL, command=text.yview)
scroll.place(x=640, y=12, height=280)
text.config(yscrollcommand=scroll.set)

data = readcsv()
for row in data:
    text.insert(END,row)
    text.insert(END,'\n')

#
LF1 = ttk.LabelFrame(GUI, text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=200, y=320)

v_data = StringVar()  # ตัวแปรพิเศษที่ใช้กับข้อความ
E1 = ttk.Entry(LF1, textvariable=v_data, font=('TH Sarabun New', 18))
E1.pack(padx=50, pady=8)

from datetime import datetime

#save data
def SaveData():
    t = datetime.now().strftime('วันที่ %d:%m:%Y เวลา %H:%M:%S')
    data = v_data.get()  # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา , ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    nofi = 'บันทึกเรียบร้อย'
    messagebox.showinfo('เเจ้งเตือน', nofi)
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

# button
B4 = ttk.Button(LF1,text='บันทึกข้อมูล',command=SaveData)
B4.pack(ipadx=50,ipady=5)   

GUI.mainloop()

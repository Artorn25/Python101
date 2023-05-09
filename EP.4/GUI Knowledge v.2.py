from tkinter  import *
from tkinter import ttk  # theme of ttk
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
GUI.title('Program keep data')  # ชื่อโปรเเกรม
GUI.geometry('800x500')  # ขนาดโปรเเกรม

background = Label(GUI, bg="blue")
background.pack(fill=BOTH, expand=True)

L1 = Label(GUI, text='ระบบเก็บข้อมูล',
           font=('TH Sarabun New', 20,"bold"), fg='green')
L1.place(x=280, y=50)

# image
FB1 = LabelFrame(GUI)
FB1.place(x=210, y=100)
image = PhotoImage(file='image.png')
label_1 = Label(FB1, image=image)
label_1.pack()

# text
FB2 = LabelFrame(GUI,font=('TH Sarabun New', 14,"bold"))
FB2.place(x=520, y=100)

text = Text(FB2, font=('TH Sarabun New', 12), height=10, width=50)

scroll = ttk.Scrollbar(FB2, orient=VERTICAL)
scroll.place(x=296, y=12, height=221)

text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)

text.pack(pady=10, padx=10)

#
LF1 = ttk.LabelFrame(GUI, text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=208, y=320)

v_data = StringVar()  # ตัวแปรพิเศษที่ใช้กับข้อความ
E1 = ttk.Entry(LF1, textvariable=v_data, font=('TH Sarabun New', 16))
E1.pack(padx=50, pady=6)

#Show data
def ShowData():
    data = readcsv()
    for row in data:
        text.insert(END,row)
        text.insert(END,'\n')
               
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
B1 = ttk.Button(LF1,text='บันทึกข้อมูล',command=SaveData)
B1.pack(ipadx=30,ipady=5)   

B2 = ttk.Button(LF1,text='เเสดงข้อมูล', command=ShowData)
B2.pack(ipadx=30,ipady=5,padx=5,pady=5)
GUI.mainloop()

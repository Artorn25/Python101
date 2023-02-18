from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอของโปรเเกรม
GUI.title('โปรเเกรมเก็บข้อมูล') #ชื่อโปรเเกรม
GUI.geometry('800x400') # ขนาดโปรเเกรม

background = Label(GUI,bg="blue")
background.pack(fill=BOTH , expand=True)

L1 = Label(GUI,text = 'โปรเเกรมบันทึกความรู้',font=('Angsana New',20),fg='green')
L1.place(x=250,y=50)
#B1 = ttk.Button(GUI, text = 'เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)# internal padding  _ __px

FB1 = LabelFrame(GUI)
FB1.place(x=210,y=100)
image = PhotoImage(file='image.png')
label_1=Label(FB1, image=image)
label_1.pack()

FB2 = LabelFrame(GUI)
FB2.place(x=230,y=320)
entry = Entry(FB2)
entry.pack(ipadx=50,ipady=5)

def get_text():
    text = entry.get()
    print('',text)
    nofi =  'บันทึกเรียบร้อย'
    messagebox.showinfo('เเจ้งเตือน',nofi)

FB3 = LabelFrame(GUI)#text='money'
FB3.place(x=250,y=370)
B2 = ttk.Button(FB3, text = 'บันทึกข้อมูล',command=get_text)
B2.pack(ipadx=50,ipady=10)#padx=30,pady=30


GUI.mainloop()

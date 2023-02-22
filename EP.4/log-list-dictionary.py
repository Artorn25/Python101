Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===
Traceback (most recent call last):
  File "C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py", line 11, in <module>
    adddata('น้ำเปล่า')
TypeError: adddata() takes 0 positional arguments but 1 was given

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===
Traceback (most recent call last):
  File "C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py", line 11, in <module>
    adddata('ช้าวผัดกะเพราไข่ดาว')
  File "C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py", line 9, in adddata
    file.writeline(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'. Did you mean: 'writelines'?

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===
['สมุด\n', 'ลูกอม\n', 'หมากฝรั่ง\n']

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===
Traceback (most recent call last):
  File "C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py", line 19, in <module>
    readdata()
  File "C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py", line 16, in readdata
    data = fileread()
NameError: name 'fileread' is not defined

==== RESTART: C:/Users/jinje/OneDrive/เดสก์ท็อป/Python/EP.4/write.py ===
สมุด
ลูกอม
หมากฝรั่ง

box = []
box = [ ]
box.append('สมุด')
box.append('ลูกอม')
box.append('หมากฝรั่ง')
print(box)
['สมุด', 'ลูกอม', 'หมากฝรั่ง']
print(box[0])
สมุด
print(box[1])
ลูกอม
print(box[2])
หมากฝรั่ง
print(box[-2])
ลูกอม
print(box[-1])
หมากฝรั่ง
print(box[-3])
สมุด
brand = {'pen':['Lamy','Pental','Fiber-castal'],'pencil':['hourse','stantdard'],'eraser':'2สี'}
print(brand)
{'pen': ['Lamy', 'Pental', 'Fiber-castal'], 'pencil': ['hourse', 'stantdard'], 'eraser': '2สี'}
print(brand['pen'])
['Lamy', 'Pental', 'Fiber-castal']
print(brand['pen'][0])
Lamy
print(brand['pencil'][0])
hourse
print(brand['eraser'][0])
2
print(brand['eraser'])
2สี
print(len(box))
3
print(brand.value())
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(brand.value())
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
print(brand.values())
dict_values([['Lamy', 'Pental', 'Fiber-castal'], ['hourse', 'stantdard'], '2สี'])
print(brand.keys())
dict_keys(['pen', 'pencil', 'eraser'])
for b in box:
    print(b)

    
สมุด
ลูกอม
หมากฝรั่ง
>>> for br in brand.keys():
...     print(br)
... 
...     
pen
pencil
eraser
>>> for br in brand.values():
...     print(br)
... 
...     
['Lamy', 'Pental', 'Fiber-castal']
['hourse', 'stantdard']
2สี
>>> for br in brand:
...     print(br)
... 
...     
pen
pencil
eraser
>>> for br in brand.items():
...     print(br)
... 
...     
('pen', ['Lamy', 'Pental', 'Fiber-castal'])
('pencil', ['hourse', 'stantdard'])
('eraser', '2สี')
>>> len(brand)
3

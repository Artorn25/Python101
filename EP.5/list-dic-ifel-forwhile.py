Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = ['Somsak','Sompon','Somsri','Sompa']
print(friend)
['Somsak', 'Sompon', 'Somsri', 'Sompa']
friend.append('Somchai')
print(friend)
['Somsak', 'Sompon', 'Somsri', 'Sompa', 'Somchai']
friend.remove('Somsak')
print(friend)
['Sompon', 'Somsri', 'Sompa', 'Somchai']
del friend[0]
print(friend)
['Somsri', 'Sompa', 'Somchai']
print(friend[0])
Somsri
number = [6,1,2,7,9,3]
number.sort()
print(number)
[1, 2, 3, 6, 7, 9]
del number[0]
print(number)
[2, 3, 6, 7, 9]
del number[-1]
print(number)
[2, 3, 6, 7]
number[0] + number[1] + number[2]
11
print(sum(number))
18
tel = {'eak': '0548846621','fah':'0145687789','kong':'0645885541'}
print(tel['eak'])
0548846621
print(tel['fah'])
0145687789
tel['eak'] = '0787786632'
print(tel)
{'eak': '0787786632', 'fah': '0145687789', 'kong': '0645885541'}
tel.items()
dict_items([('eak', '0787786632'), ('fah', '0145687789'), ('kong', '0645885541')])
for f in friend:
    print(f)

    
Somsri
Sompa
Somchai
for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(5):
    print(i+1)

    
1
2
3
4
5
list(range(5))
[0, 1, 2, 3, 4]
for i in [0,1,2,3,4]:
    print(i)

    
0
1
2
3
4
for t in tel.items()ซ
SyntaxError: incomplete input
for t in tel.items():
    print(t)

    
('eak', '0787786632')
('fah', '0145687789')
('kong', '0645885541')
for t in tel.items():
    print(t[1])

    
0787786632
0145687789
0645885541
for t in tel.values():
    print(t)

    
0787786632
0145687789
0645885541
for t in tel.keys():
    print(t)

    
eak
fah
kong
import time
while True:
    print('สวัสดีวันอังคาร')
    time.sleep(1)

    
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
Traceback (most recent call last):
  File "<pyshell#50>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt

ไเ
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
while False:
    print('Hello ')
    print('Hello ')
    print('Hello ')
    print('Hello ')
    print('Hello ')
    print('Hello ')

    
friend = 'To'
while friend == 'To':
    print("Let 's go")

    
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Let 's go
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    print("Let 's go")
KeyboardInterrupt
def Yourmoney(money):
    if money > 300:
        print('ไปเที่ยว')
        elif money > 200:
            
SyntaxError: invalid syntax
def Yourmoney(money):
    if money > 300:
        print('ไปเที่ยว')
    elif money > 200:
        print('ไปตลาด')
    else :
        print('มาม่า')

        
Yourmoney(200)
มาม่า
def Yourmoney(money):
    if money >= 300:
        print('ไปเที่ยว')
...     elif money >=200:
...         print('ไปตลาด')
...     else :
...         print('มาม่า')
... 
...         
>>> Yourmoney(300)
ไปเที่ยว
>>> if False:
...     print('h1')
... 
...     
>>> if True:
...     print('h1')
... 
...     
h1
>>> money = 100
>>> while money >= 100:
...     print ('Ready')
...     time.sleep(1)
... 
...     
Ready
Ready
Ready
Ready
Ready
Ready
Traceback (most recent call last):
  File "<pyshell#86>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt

class System:
    # Attribute
    systemName = 'ระบบทำใบขับขี่รถยนต์เเละมอเตอร์ไซต์ '
    #pointName = 'ในส่วนของการทำใบขับขี่รถยนต์นั้น '

    # Constructor
    def __init__(self, career='',select=''):
        print('เฉพาะคนที่ได้รับการยืนยันตัวตน')
        self.career = career
        self.select = select

    # Method
    def hello(self):
        print('สวัสดีครับ ขอต้อนรับสู่การทำใบขับบี่รถยนต์ในภาคเช้าครับ')


    def teach(self):
        print(f'ผู้สมัครจะมาทำใบขับขี่ {self.select}')

class Membercar(System):
    def __init__(self, fullname, level, genter, contact, career,scoreschoice,scorespractice,age,select):
        super().__init__(career,select)
        self.fullname = fullname
        self.level = level
        self.genter = genter
        self.contact = contact
        self.scoreschoice = scoreschoice
        self.scorespractice = scorespractice
        self.age = age
        self.scorestotal = scoreschoice + scorespractice

    def scanAge(self):
        if self.age >= 20:
            print(f'คุณผ่านเกณฑ์เรื่องอายุสามารถทำใบขับขี่ {self.select} ได้ครับ')
            if self.scoreschoice >= 80:
                print(f'คุณได้คะเเนน {self.scoreschoice} ในภาคทฤษฎี ซึ่งถือว่าคุณผ่าน ไปสูู่บททดสอบอันถัดไป')
                if self.scorespractice >= 70:
                    print(f'คุณได้คะเเนน {self.scorespractice} ในภาคปฎิบัตื ซึ่งถือว่าคุณผ่าน กรุณาไปรับใบขับขี่ {self.select} ได้เลยครับ')
                else:
                    print(f'คุณได้คะเเนน {self.scorespractice} ในภาคปฎิบัติ ซึ่งถือว่า ไม่ผ่านการทำแบบทดสอบใบขับขี่ {self.select} กรุณามาทำใหม่ในครั้งหน้าครับ')
            else:
                print(f'คุณได้คะเเนน {self.scoreschoice} ในภาคทฤษฎี ซึ่งถือว่า ไม่ผ่านการทำแบบทดสอบใบขับขี่ {self.select} กรุณามาทำใหม่ในครั้งหน้าครับ')
        else :
            print(f'คุณไม่ผ่านเกณฑ์ในเรื่องอายุครับ เนื่องจากคุณอายุ {self.age} ปี ซึ่งยังไม่ถึง 20 ปีบริบูรณ์ครับ')

class Membermotercycle(System):
    def __init__(self, fullname, level, genter, contact, career,scoreschoice,scorespractice,age,select):
        super().__init__(career,select)
        self.fullname = fullname
        self.level = level
        self.genter = genter
        self.contact = contact
        self.scoreschoice = scoreschoice
        self.scorespractice = scorespractice
        self.age = age
        self.scorestotal = scoreschoice + scorespractice

    def scanAge(self):
        if self.age >= 15:
            print(f'คุณผ่านเกณฑ์เรื่องอายุสามารถทำใบขับขี่ {self.select} ได้ครับ')
            if self.scoreschoice >= 80:
                print(f'คุณได้คะเเนน {self.scoreschoice} ในภาคทฤษฎี ซึ่งถือว่าคุณผ่าน ไปสูู่บททดสอบอันถัดไป')
                if self.scorespractice >= 70:
                    print(f'คุณได้คะเเนน {self.scorespractice} ในภาคปฎิบัตื ซึ่งถือว่าคุณผ่าน กรุณาไปรับใบขับขี่ {self.select} ได้เลยครับ')
                else:
                    print(f'คุณได้คะเเนน {self.scorespractice} ในภาคปฎิบัติ ซึ่งถือว่า ไม่ผ่านการทำแบบทดสอบใบขับขี่ {self.select} กรุณามาทำใหม่ในครั้งหน้าครับ')
            else:
                print(f'คุณได้คะเเนน {self.scoreschoice} ในภาคทฤษฎี ซึ่งถือว่า ไม่ผ่านการทำแบบทดสอบใบขับขี่ {self.select} กรุณามาทำใหม่ในครั้งหน้าครับ')
        else :
            print(f'คุณไม่ผ่านเกณฑ์ในเรื่องอายุครับ เนื่องจากคุณอายุ {self.age} ปี ซึ่งยังไม่ถึง 20 ปีบริบูรณ์ครับ')
    

print('==========================')
member01 = Membercar('สมพงศ์', 'ปริญญาโท', 'ชาย', '098-6582214' ,'ค้าขาย',80,90,26,'รถยนต์')
member01.hello()
member01.teach()
print(f'{member01.systemName}')
print(f'ชื่อผู้สมัคร {member01.fullname}')
print(f'ระดับจบการศึกษา {member01.level}')
print(f'เพศ {member01.genter}')
print(f'เบอร์ติดต่อ {member01.contact}')
print(f'อาชีพที่ทำ {member01.career}')
print(f'อายุ {member01.age}')
member01.scanAge()
print(f'คะเเนนสอบทั้งหมดในภาคทฤษฎ๊เเละภาคปฎิบัติได้ {member01.scorestotal} เต็ม 200 คะเเนน')
print('==========================')
member02 = Membermotercycle('มงคล', 'มัธยมศึกษาตอนต้น', 'ชาย', '098-6582214' ,'นักเรียน',80,50,16,'มอเตอร์ไซต์')
member02.hello()
member02.teach()
print(f'{member02.systemName}')
print(f'ชื่อผู้สมัคร {member02.fullname}')
print(f'ระดับจบการศึกษา {member02.level}')
print(f'เพศ {member02.genter}')
print(f'เบอร์ติดต่อ {member02.contact}')
print(f'อาชีพที่ทำ {member02.career}')
print(f'อายุ {member02.age}')
member02.scanAge()
print(f'คะเเนนสอบทั้งหมดในภาคทฤษฎ๊เเละภาคปฎิบัติได้ {member01.scorestotal} เต็ม 200 คะเเนน')



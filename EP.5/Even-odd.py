def check(number):
    for d in number.items():
        if d[1]%2 == 0 & d[1]== 0:
            print(d[0] , d[1],'is Even')
        else :
            print(d[0],d[1],'is Odd')
            


number = {'A' :25,'B' :26,'C' :30,'D':35,'F':28,'G':31}
check(number)



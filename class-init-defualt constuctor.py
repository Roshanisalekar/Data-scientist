#--------------------------------------------------------------------------------------------------
# example :1

class defualitconstuctor:
    def __init__(self):
        pass
    
ds=defualitconstuctor()

# output:

# PS C:\Data scientist>
#-------------------------------------------------------------------------------------------------------
# example :2
    
class Student:            # creating class
    def __init__(self):  #init:- defualit call
        self.name='roshani'
        self.age=34
        print(f'{self.name} and {self.age}')
     

s1=Student()  # s1= object
# print(s1.name)
# print(s1.age)

# output:-

# roshani and 34
#----------------------------------------------------------------------------------------------------
# example : 3

class car:
    def __init__(self):
        self.brand="mercedes"
        self.color='red'
        print(f'{self.brand} and {self.color}')

car1=car()
# print(car1.brand)
# print(car1.color)

# output:-
# mercedes and red
# mercedes
# red
#--------------------------------------------------------------------------------------------------------
# example :4 

class Teacher:
    def __init__(self):
        self.name='RAJENDRA'
        self.teach='best'
        self.speack='effective communication '
        self.subject='python'
        print(f"{self.name} and {self.teach} and { self.speack} and { self.subject}")

t1=Teacher()
print(t1.name)
print(t1.teach)
print(t1.speack)
print(t1.subject)

# output:-

# RAJENDRA and best and effective communication  and python
# RAJENDRA
# best
# effective communication
# python
#---------------------------------------------------------------------------------------------------
# examle :5 

class language:
    def __init__(self):
        self.module1='python'
        self.module2='sql'
        self.module3='deep-learning'
        self.module4='machine-learning'
        self.module5='AI'
        self.module6='big data'

l1=language()
print(l1.module1)
print(l1.module2)

print(l1.module3)
print(l1.module4)

print(l1.module5)
print(l1.module6)

# output:-

# python
# sql
# deep-learning
# machine-learning
# AI
# big data
#---------------------------------------------------------------------------------------------------------
# example : 6

class familymember:
    def __init__(self):
        self.myname="roshani"
        self.father='ankush'
        self.mother='savita'
        self.bigbrother='amol'
        self.brother='sagar'

f1=familymember()
print(f1.myname)
print(f1.father)
print(f1.mother)
print(f1.bigbrother)
print(f1.brother)

# output:

# roshani
# ankush
# savita
# amol
# sagar
#--------------------------------------------------------------------------------------------------------
# example : 7

class college:
    def __init__(self):
        self.clgname='ycc'
        self.place='gansoli'
        self.principlename='manish'

c1=college()
print(c1.clgname)
print(c1.place)
print(c1.principlename)

# output :

# ycc
# gansoli
# manish

#---------------------------------------------------------------------------------------------------------
# example :- 8

class menu:
    def __init__(self):
        self.menu1='pavbhaji'
        self.menu2='vadapav'
        self.menu3='panipuri'

m1=menu()
print(m1.menu1)
print(m1.menu2)

print(m1.menu3)

# output: 

# pavbhaji
# vadapav
# panipuri
#------------------------------------------------------------------------------------------------------

# example : 9

class topic:
    p1='variable'
    p2='oop'
    p3='loop'
    p4='conditional'

t1=topic()
print(t1.p1)
print(t1.p2)
print(t1.p3)
print(t1.p4)

# output:

# variable
# oop
# loop
# conditional
#-----------------------------------------------------------------------------------------------------------
# example :10

class computer:
    def __init__(self):
        self.part1='cpu'
        self.part2='mouse'
        self.part3='keyboard'

c=computer()
print(c.part1)
print(c.part2)
print(c.part3)

# output:-

# cpu
# mouse
# keyboard
#----------------------------------------------------------------------------------------------------------

# example :11 

class developer:
    def __init__(self):
        self.developer1='python'
        self.developer2='java'
        self.developer3='c++'
        self.developer4='c'
        self.developer5='AI'

d1=developer()
print(d1.developer1)
print(d1.developer2)
print(d1.developer3)
print(d1.developer4)
print(d1.developer5)

# output:-

# python
# java
# c++
# c
# AI

#------------------------------------------------------------------------------------------------------
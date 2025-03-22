# class : class is blueprint or templete for creating object .
# object :- object is instance of class

# for example :- 1

class Student:    # creating class
    name='roshani'

s1=Student()  # s1= object
print(s1.name)



# output:

# roshani

# for example :- 2

class car:
    brand="mercedes"
    color='red'

car1=car()
print(car1.brand)
print(car1.color)

car2=car()
print(car2.brand)
print(car2.color)

# output:
# mercedes
# red

# red
# mercedes

# example : 3

class Teacher:
    name='RAJENDRA'
    teach='best'
    speack='effective communication '
    subject='python'

t1=Teacher()
print(t1.name)
print(t1.teach)
print(t1.speack)
print(t1.subject)

# output:

# RAJENDRA
# best
# effective communication
# python


# example : 4

class language:
    module1='python'
    module2='sql'
    module3='deep-learning'
    module4='machine-learning'
    module5='AI'
    module6='big data'

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

# example : 5
class familymember:
   myname="roshani"
   father='ankush'
   mother='savita'
   bigbrother='amol'
   brother='sagar'

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

# example : 6 

class college:
    clgname='ycc'
    place='gansoli'
    principlename='manish'

c1=college()
print(c1.clgname)
print(c1.place)
print(c1.principlename)

# output :

# ycc
# gansoli
# manish

# example :- 7

class menu:
    menu1='pavbhaji'
    menu2='vadapav'
    menu3='panipuri'

m1=menu()
print(m1.menu1)
print(m1.menu2)

print(m1.menu3)

# output: 

# pavbhaji
# vadapav
# panipuri

# example : 8 

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

# example :9

class computer:
    part1='cpu'
    part2='mouse'
    part3='keyboard'

c=computer()
print(c.part1)
print(c.part2)
print(c.part3)

# output:-

# cpu
# mouse
# keyboard

# example :10 

class developer:
    developer1='python'
    developer2='java'
    developer3='c++'
    developer4='c'
    developer5='AI'

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
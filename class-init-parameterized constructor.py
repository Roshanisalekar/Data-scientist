#-----------------------------------------------------------------------------------------------------------
# example: 1

class Student:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print(f"{self.name} {self.surname}")

s1=Student('roshani','salekar')
s1=Student('savita','salekar')
s1=Student('roshan','lekar')
s1=Student('shani','mane')
s1=Student('roshu','madre')

s2=Student('divya','jadhav')

# output :

# roshani salekar
# savita salekar
# roshan lekar
# shani mane
# roshu madre
# divya jadhav
#-----------------------------------------------------------------------------------------------------------
# example: 2

class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        print(f'{self.brand} and {self.color}')

car1=car('bmw','black')
car1=car('tesla','red')
car1=car('mercedes','white')

# output :

# bmw and black
# tesla and red
# mercedes and white

#-------------------------------------------------------------------------------------------------
# example :- 3

class Teacher:
    def __init__(self,name,teach,speack,subject):
        self.name=name
        self.teach=teach
        self.speack=speack
        self.subject=subject
        print(f"{self.name} and {self.teach} and { self.speack} and { self.subject}")

t1=Teacher('rajendra','best','effective communication','python')

t2=Teacher('raju','good','communication','java')

# output:-

# rajendra and best and effective communication and python
# raju and good and communication and java

#---------------------------------------------------------------------------------------------

# examle :5 

class language:
    def __init__(self,module1,module2,module3,module4,module5,module6):
        self.module1=module1
        self.module2=module2
        self.module3=module3
        self.module4=module4
        self.module5=module5
        self.module6=module6
        print(f"{self.module1} and {self.module2} and { self.module2} and { self.module4}")


l1=language('pyhon','sql','AI','DP','ML','BIGDATA')
print(l1.module5)
print(l1.module6)

# output :
# pyhon and sql and sql and DP
# ML
# BIGDATA

#---------------------------------------------------------------------------------------------------------
# example : 6

class familymember:
    def __init__(self,myname,father,mother,bigbrother,brother):
        self.myname=myname
        self.father=father
        self.mother=mother
        self.bigbrother=bigbrother
        self.brother=brother
        print(f"{self.myname} and {self.father} and { self.mother} and { self.brother}")

f1=familymember('roshani','ankush',"savita","amol","sagar")
print(f1.bigbrother)
print(f1.mother)

# output:-
# roshani and ankush and savita and sagar
# amol
# savita

#--------------------------------------------------------------------------------------------------------
# example : 7

class college:
    def __init__(self,clgname,place,principlename):
        self.clgname=clgname
        self.place=place
        self.principlename=principlename
        print(f"{self.clgname} and {self.place} and { self.place} and { self.principlename}")


c1=college('ycc','ghansoli','kedar')
print(c1.clgname)
print(c1.place)

# output:

# ycc and ghansoli and ghansoli and kedar
# ycc
# ghansoli


#---------------------------------------------------------------------------------------------------------
# example :- 8

class menu:
    def __init__(self,menu1,menu2,menu3):
        self.menu1=menu1
        self.menu2=menu2
        self.menu3=menu3
        print(f"{self.menu1} and {self.menu2} and { self.menu3} and { self.menu1}")


m1=menu('pavbhaji','vadapav','panipauri')
print(m1.menu1)
print(m1.menu2)

print(m1.menu3)

# output:-
# pavbhaji and vadapav and panipauri and pavbhaji
# pavbhaji
# vadapav
# panipauri

#------------------------------------------------------------------------------------------------------

# example : 9

class topic:
    def __init__(self,p1,p2,p3,p4):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4

t1=topic('loop','conditonal','variable','oop')
print(t1.p1)
print(t1.p2)
print(t1.p3)
print(t1.p4)

# output :-

# loop
# conditonal
# variable
# oop

#-----------------------------------------------------------------------------------------------------------
# example :10

class computer:
    def __init__(self,part1,part2,part3):
        self.part1=part1
        self.part2=part2
        self.part3=part3

c=computer('keyboard','cpu',"mouse")
print(c.part1)
print(c.part2)


# output:
# oop
# keyboard
# cpu
#-------------------------------------------------------------------------------------------

# example : 11

name="roshani"
age=23
class man():
    gender="male"
    def __init__(self,name):
        self.name=name
    def display(self):
        #return f" my name is {self.name}"
        return f" my name is {name}"
obj=man("sagar")
print(obj.display())

# output:-
#  my name is roshani

#-------------------------------------------------------------------------------------------

# example : 12

class family():
    gender="female"
    def __init__(self,father,mother,brother,sister):
        self.father=father
        self.mother=mother
        self.brother=brother
        self.sister=sister

    def show(self):
        return f"{self.father},{self.mother},{self.brother},{self.sister} is my family "
    
obj1=family("ankush","savita","sagar","divya")
print(obj1.show())

# output :-
# ankush,savita,sagar,divya is my family 

#-------------------------------------------------------------------------------------------

# example : 13


age=30
class char():
    gender="male"
    def __init__(self,age):
        self.age=age
    def countofage(self):
        self.age=self.age-5
        return self.age
obj=char(34)
print(obj.countofage())
print(obj.age)

# output:-
# 29
# 29

#-----------------------------------------------------------------------------------------------------------

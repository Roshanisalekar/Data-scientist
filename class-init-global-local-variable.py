# global variable :  global variable is commonly access for any object
# local variable :  only access class 
#----------------------------------------------------------------------------------------------------------
# example:1

class student:
    place='ghansoli'
    college='ycc'
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print(f"{self.name} {self.surname}")

s1=student('payal','jagdale')
print(s1.name)
print(s1.college)


s2=student('mansi','jagu')
print(s2.name)
print(s2.college)

# output:

# payal jagdale
# payal
# ycc
# mansi jagu
# mansi
# ycc
#--------------------------------------------------------------------------------------------------------------------

# example:2

class programming:
    USE='VS CODE'
    def __init__(self,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3
        print(f'{self.l1} and {self.l2} and {self.l3} is used to {self.USE}')

p1=programming('python','java','AI')
print(programming.USE)

# output:-

# python and java and AI is used to VS CODE
# VS CODE

#-----------------------------------------------------------------------------------------------------------

#example :3

class hotel:
    payment='cash'
    def __init__(self,menu1,menu2,payment):
        self.menu1=menu1
        self.menu2=menu2
        self.payment=payment
        print(f'{self.menu1} and {self.menu2}')
        print( f'{payment} and {self.payment}')

h1=hotel('chikane','biryani','online')
print(hotel.payment)


# output:-

# chikane and biryani
# online and online

# cash
#----------------------------------------------------------------------------------------------------------------

 #example :4 

class makeup:
    m='pawder'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        print(f'{self.m1} and {self.m2} and {self.m3} { self.m}')

mu=makeup('lipstick','kajal','liyener')
print(mu.m)

# output:
# lipstick and kajal and liyener pawder
# pawder

#--------------------------------------------------------------------------------------------------------------

#example : 5
class masale:
    masala='maggic'
    def _init_(self,masala1,masala2,masala3):

        self.masala1=masala1
        self.masala2=masala2
        self.masala3=masala3
        
        

        print(f'{self.masala1} and {self.masala2} and {self.masala3} and {self.masala}')

m=masale("chicken","paneer","misal")
print(m.masala)

# output:
# chicken and paneer and misal and maggic
# maggic

#----------------------------------------------------------------------------------------
# example :6

class color:
    c='black'
    def _init_(self,c1,c2,c3):
        self.c1=c1
        self.c2=c2
        self.c3=c3
        print(f'{self.c1} vs {self.c2} vs {self.c3} vs {self.c}')
        
colours=color('red','blue','green')

col=color('pink','white','orange')

# output:
# red vs blue vs green vs black
# pink vs white vs orange vs black
#----------------------------------------------------------------------------------------

#example : 7


class datatype:
    c='imutable'
    def _init_(self,d1,d2,d3):
        self.d1=d1
        self.d2=d2
        self.d3=d3
        print(f'{self.d1} vs {self.d2} vs {self.d3} vs {self.c}')
        
types=datatype('complex','float','int')

t1=datatype('tuple','list','string')

# output:
# complex vs float vs int vs imutable
# tuple vs list vs string vs imutable

#------------------------------------------------------------------------------------------

# example : 8

class data_sciencetist:
    subject="data anaytics"
    def _init_(self,s1,s2,s3,s4,s5):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        print(f"{self.s1} ,{self.s2},{self.s3},{self.s4},{self.s5},{self.subject}")

data=data_sciencetist('python','sql','AL','DL','ML')
        
# OUTPUT:

# python ,sql,AL,DL,ML,data anaytics

#--------------------------------------------------------------------------------------

# example :9

class developer:
    def _init_(self,developer1,developer2,developer3,developer4,developer5):
        self.developer1=developer1
        self.developer2=developer2
        self.developer3=developer3
        self.developer4=developer4
        self.developer5=developer5
        print(f"{developer1},{developer2}")
        
        
dev=developer("java","python","c++","c","c#")

# output:
    
# java,python
    
#--------------------------------------------------------------------------------------
        
# example:10

class car:
    color='white'
    style='royal'
    def _init_(self,brand,color):
        self.brand=brand
        self.color=color
        print(f"{self.brand} is  color {self.color} and {self.style}")
car1=car('bmw','black')


# output:        
# bmw is color black and royal

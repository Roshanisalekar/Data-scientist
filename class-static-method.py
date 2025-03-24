# static method : it is uesd to secific method call

# 1> self   2> @staticmethod
#--------------------------------------------------------------------------------------------------------------
# example :1

class student:
    name='sagar'
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print(f'{name} and {self.name}')

    @staticmethod
    def show():
        print("i love coding")

s1=student('roshni',mark=90)
s1.show()

# output:
# roshni and roshni
# i love coding

#-----------------------------------------------------------------------------------------------------------
# example :2

class logic():
    @staticmethod
    def callme():
        print("call me again")

l1=logic()
l1.callme()

# output:
# call me again
#--------------------------------------------------------------------------------------------------------------
# example :3

class developer():
    def code(self):
        print("python developer")

d1=developer()
d1.code()

# output:
# python developer

#--------------------------------------------------------------------------------------------------------------
# example :4
 
class book():
    def chapter(self):
        print("object-oriented-programming")
b=book()
b.chapter()

# output:
# object-oriented-programming

#--------------------------------------------------------------------------------------------------------------

# example :5

class family():
    @staticmethod
    def funny():
        print("my family is funny")

f=family()
f.funny()

# output:
# my family is funny

#------------------------------------------------------------------------------------------------------------------

# example : 6


class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        print(f'{self.brand} and {self.color}')

    @staticmethod
    def move():
        print("fastly")

car1=car('bmw','black')
car1=car('tesla','red')
car1=car('mercedes','white')

car1.move()
# output:

# bmw and black
# tesla and red
# mercedes and white
# fastly

#------------------------------------------------------------------------------------------------------------------

# example : 7

class car():
    def start(self):
        print("car is starting.....")

    def stop(self):
        print("car is stoping.....")

car1=car()

car1.start()
car1.stop()

# output:-

# car is starting.....
# car is stoping.....

#------------------------------------------------------------------------------------------------------------------

# example : 8 

class bag():
    @staticmethod
    def color():
        print("color is red")
    @staticmethod
    def brand():
        print("bmw")

b1=bag()
b1.color()
b1.brand()

# output:-

# color is red
# bmw

#------------------------------------------------------------------------------------------------------------------

# example : 9 

class college():
    @staticmethod
    def ycc():
        print("ycc is best college")

    def tilak(self):
        print("tilak is normal college")

c=college()
c.ycc()
c.tilak()

# output:-
 
# ycc is best college
# tilak is normal college

#-----------------------------------------------------------------------------------------------------------
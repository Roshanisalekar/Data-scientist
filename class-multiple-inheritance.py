#----------------------------------------------------------------------------------------------------------------
# example :- 1 

class A:
    def a(self):
        print("class A")

class B(A):
    def b(self):
        print("class B")

class c(B):
    def c(self):
        print("class c")

c=c()

c.b()
c.a()
c.c()

# output :-

# class B
# class A
# class c

#----------------------------------------------------------------------------------------------------------------
# example :- 2

class car():
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

class toyotacar(car):

    def __init__(self,brand):
        self.brand=brand
        print(f"{self.brand}")
    
class fortuner(toyotacar):

    def __init__(self,color):
        self.color=color
        print(f"{color}")

c1=fortuner('red')
c1.start()
c1.stop()


# output :-

# red
# car started
# car stopped

#----------------------------------------------------------------------------------------------------------------
# example :- 3

class college:
    def __init__(self,name):
        self.name=name

class principle(college):
    def __init__(self,name):
        self.name=name

    def sayhello(self):
        print("hello everybudy")

class university(principle):
    def __init__(self,name):
        self.name=name
        print(f"{name}")

u=university('mumbai')
u.sayhello()

# output:-
# mumbai
# hello everybudy

# ----------------------------------------------------------------------------------------------------------------
# example :- 4

class grandfather:
    grandfather="chhaberav"

    def brave(self):
        print("grandfather is brave")

class grandmother(grandfather):

    def strong(self):
        print("my family ")


class family(grandmother):
    dad="ankush"

    def __init__(self,brother,brother1):
        self.brother=brother
        self.brother1=brother1
        print(f"{brother1}")

f=family("amol",'sagar')

print(f.dad)
f.strong()
f.brave()

# output:-
# sagar
# ankush
# my family
# grandfather is brave

# ----------------------------------------------------------------------------------------------------------------
# example :- 5

class data_science:
    trainer="rajendra sir"

    def teach(self):
        print("teaching is best")

class module(data_science):

    def __init__(self,m1):
        self.m1=m1
        print(f"{m1}")

class me(module):

    def me(self):
        print("i am best student")


m=me("python")
print(m.trainer)

# output:
# python
# rajendra sir

#-------------------------------------------------------------------------------------------------------------------
# example :- 6

        
class dad():
    money="2lac"
    home="2BHK"
    height=5.6
    def talk(self):
        return "my voice is hard"
    def walk(self):
        return "faster"

        
class mom(dad):
    salary=25000
    home="1BHK"
    
    def talk(self):
        return "my voice is smooth"
    def walk(self):
        return "slower"
    def sleep(self):
        return "I am sleeping 4 hours"

obj=mom()
print(obj.height)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
print(obj.home)
print(obj.salary)
print(obj.home)
print(obj.money)
print(obj.sleep())
print(obj.walk())

class son(mom,dad):
    pass

obj=son()
print(obj.money)
print(obj.home)
print(obj.salary)
print(obj.home)

# output:-

# 2lac
# 1BHK
# 25000
# 1BHK

#----------------------------------------------------------------------------------------------------------

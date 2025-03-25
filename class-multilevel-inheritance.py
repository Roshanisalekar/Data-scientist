 #-------------------------------------------------------------------------------------------------------------------

 # exampl.e : 1

class A:
    def a(self):
        print("class A")

class B:
    def b(self):
        print("class B")

class c(B,A):
    def c(self):
        print("class c")

c=c()

c.b()
c.a()
c.c()

# output:-

# class B
# class A
# class c

#-------------------------------------------------------------------------------------------------------------------

# exampl.e : 2


class car():
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

class toyotacar():

    def __init__(self,brand):
        self.brand=brand
        print(f"{self.brand}")
    
class fortuner(toyotacar,car):

    def __init__(self,color):
        self.color=color
        print(f"{color}")

c1=fortuner('red')
c1.start()
c1.stop()
# c1.toyotacar()


# output:-
# red
# car started
# car stopped

#----------------------------------------------------------------------------------------------------------------
# example :- 3

class college:
    def __init__(self,name):
        self.name=name

class principle():
    def __init__(self,name):
        self.name=name

    def sayhello(self):
        print("hello everybudy")

class university(principle,college):
    def __init__(self,name):
        self.name=name
        print(f"{name}")

u=university('mumbai')
u.sayhello()
# u.principle("raju")

# output:-
# mumbai
# hello everybudy


# ----------------------------------------------------------------------------------------------------------------
# example :- 4

class grandfather:
    grandfather="chhaberav"

    def brave(self):
        print("grandfather is brave")

class grandmother():

    def strong(self):
        print("my family ")


class family(grandmother,grandfather):
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

class module():

    def __init__(self,m1):
        self.m1=m1
        print(f"{m1}")

class me(data_science,module):

    def me(self):
        print("i am best student")


m=me("python")
print(m.trainer)

# output:
# python
# rajendra sir

#-------------------------------------------------------------------------------------------------------------------
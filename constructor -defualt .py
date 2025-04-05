# example : 1  defualt constuctor automatically called       
#-------------------------------------------------------------------------------------------------------------
class A:

    name="savi"
    age=22

    def __init__(self):
        print(self.name)


a=A()

# output:-

# roshani
# --------------------------------------------------------------------------------------------------------------

# example : 2  two and more than  defualt constuctor in program that only run currently constuctor .
class A:
    name="roshani"
    age=22

    def __init__(self):
        print(self.name)

    def __init__(self):
        print("my name is ",self.name," and age is",self.age)

a=A()

# output :- 
# my name is  roshani  and age is 22
#----------------------------------------------------------------------------------------------------------------

# example :3   manualy method ko object ke throgh call karna padega

class A:
    name="sagar"
    age=30

    def __init__(self):
        print(self.name)

    def show(self):
        print(self.age)

a=A()
a.show()

# output:- 

# sagar
# 30

#------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
# example :1

class myclass():
    def createname(self,name):
        self.name=name
    def displayname(self):
        return self.name
    def sayhello(self):
        return f"hello dear {self.name}"
cob1=myclass()
cob2=myclass()

print(cob1.createname("raj"))
print(cob2.createname("kumar"))#NameError: name 'kumar' is not defined

print(cob1.sayhello())
print(cob2.sayhello())

# output:-

# None
# None
# hello dear raj  
# hello dear kumar

#-------------------------------------------------------------------------------------------------------------------
# example :2 

 
class developer():
    def python(self,name):
        self.name=name
        return name
    def dispalyname(self):
        return self.name
    def html():
        return f"{self.name} is easy language"
obj1=developer()
obj2=developer()

obj1.python("python")
print(obj1.dispalyname())

obj2.python("php")
print(obj2.dispalyname())

# output:-

# python
# php
#----------------------------------------------------------------------------------------------------------------------
# example :- 3

name="roshani"
age=20

class exp():
    name="DIVYA"
    age=23
    def greet(self):
        return f" my name is {self.name} and my age is {age}"
    def greetgreet(self):
        return f" my name is {self.name} and my age is {self.age}"
    def greet3(abc):
        return f" my name is {name} and my age is {abc.age}"

obj=exp()
print(obj.greet())
print(obj.greetgreet())
print(obj.greet3())

# output:-

#  my name is DIVYA and my age is 20
#  my name is DIVYA and my age is 23
#  my name is roshani and my age is 23

#---------------------------------------------------------------------------------------------------------------
# example :- 4

class syit():
    def rollno(self,number):
        self.number=number
    def displayrollno(self):
        return self.number


obj1=syit()
obj2=syit()

obj1.rollno(101)
print(obj1.displayrollno())

obj2.rollno(102)
print(obj2.displayrollno())

# output:- 
# 101
# 102

#-------------------------------------------------------------------------------------------------------------
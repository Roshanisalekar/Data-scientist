#--------------------------------------------------------------------------------------------------------------
# example :1

class car():
    color="black"

    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

        
class toyotacar(car):

    def __init__(self,name):
        self.name=name
        print(f"{name}")

c1=toyotacar("bmw")
c1.start()
c1.stop()

    
c2=toyotacar("fortuner")

# output:
# bmw
# car started
# car stopped
# fortuner   
#----------------------------------------------------------------------------------------------------------------------
# example : 2 

class student():
    college="ycc"

    def open(self):
        print("college start timing is 7 : 30 am")

    
    def close(self):
        print("college close timing is 5 : 30 pm")

class college(student):

    def __init__(self,fy,sy,ty):
        self.fy=fy
        self.sy=sy
        self.ty=ty
        print(f'{sy}')


c=college(70,80,90)
c.open()
c.close()

# output :- 
# 80
# college start timing is 7 : 30 am
# college close timing is 5 : 30 pm

#----------------------------------------------------------------------------------------------------------------------
# example : 3

class employee():
    name='roshni'
    def education(self):
        print("she is educated")

class company(employee):
    def __init__(self,salary):
        self.salary=salary
        print(f"{salary}")

com=company(100000)
print(com.name)
com.education()

# output:-

# 100000
# roshni
# she is educated

#----------------------------------------------------------------------------------------------------------------------
# example : 4

class makeup():
    artist="divya"

    def hairstyle(self):
        print(f"hairstyle is nice")

class shop(makeup):
    def __init__(self,prize):
        self.prize=prize
        print(f"{prize}")

sh=shop(2345)
sh.hairstyle()
print(sh.artist)

# output:-

# 2345
# hairstyle is nice
# divya

#----------------------------------------------------------------------------------------------------------------------
# example : 5

class skill():
    employee='developer'

    def skill1(self):
        print("skill is important for developer")

class data_science(skill):

    def __init__(self,language):
        self.language=language
        print(f"{self.language}")

d=data_science('python')
d.skill1()

# output:-
# python
# skill is important for developer

#-----------------------------------------------------------------------------------------------------
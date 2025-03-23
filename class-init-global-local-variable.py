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
# aptitude

# example NO : 1
a=[]
print(a)
print(len(a)) # len 0 
b=100
b
print(type(b))
a=(1,2),(3,4)
print(a)
print(type(a))

# 

# example NO : 2

a=[1,2,3,4,1,1,3,4,2]
b=set(a)
print(b) 

# example NO : 3 

raj=25000
mansi=35000
roshan='ketan'

temp=raj
raj=roshan
roshan=mansi
mansi=temp
print(raj)
print(mansi)
print(roshan)

# example NO : 4 

print(set())  
#print(set(tuple(list(2,1))))  #TypeError: list expected at most 1 argument, got 2  
a=set(list(tuple("salekar"))) # Strring is allow only one but integer is not allow
print(a) 

# example NO : 5

# 0,""(empty string),null makes the condition False .if condition is false ,elif or else executed but if it true if is executed.

if " ":   
    print('a')
elif "raj":
    print("b")
else :
    print("b")
    
# example NO : 6
"""
x=20
y=30
if x<y:
    print(yes)#NameError: name 'yes' is not defined  or  yes is variable
else:
    print("yes") """
    
# example NO : 7

# logical operator : and
x=20
y=30
if x<y and x>y:
    print("yes")
else:
    print("no")

# example NO : 8   

# logical operator : or 

x=20
y=30
if x<y or  x>y:
    print("yes")
else:
    print("no")
    
# example NO : 9

# logical operator : and

#NameError: 

"""
x=20
y=30
if x<y and m==n: #NameError: name 'm' is not defined
    print("yes")
else:
    print("no")
""" 

# example NO : 10 

"""
a=(1,2,3,6,7)
if a  in (1,6):
    print("yes")
else:
    print("no")
"""

# example NO : 11

a=-23
b=20
if (a+b)+3:  # -3+3 =0  condition is false then else part will be executed.
    print("yes")
else:
    print("no")
    
    
# example NO : 12

if (30-27)-3:    #3-3=0 condition is false then else part will be executed.
    print("yes")
else:
    print("no")
    
    
# example NO : 13

# SyntaxError: invalid syntax

"""

if 34,"raj":  #  condition is only one times of one condition is accept . there are two condition 34,and "raj" 
    print("yes")
else:
    print("no") """
    

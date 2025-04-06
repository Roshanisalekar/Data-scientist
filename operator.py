# logical operator 

a=(1>2) or not(1>2)
print(a)

a=(2<1) or not(1>2)
print(a)

# membership operator

a=[1,2,3,4,5]
print(2 in a)

print(5 not in a)

#rint(a in 5)#ypeError: argument of type 'int' is not iterable

# identify operator

print(a is 5)

print(5 is a)

print(a is [1,2,3,4,5])
x=4
print(4 is x)
print(x is 4)
print(x is not 4)
print(4 is not x)

# assignment operator 

x=2
x -=1
print(x)

x +=43
print(x)

z=(6!=6.0)
print(z)

# arithmatical operator

a=3
b=5
print(a//b)
print(a%b)
print(a/b)

print(a+b)
print(a-b)

print(a*b)
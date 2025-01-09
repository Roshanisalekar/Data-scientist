#concatination operation 

# number ,string ,tuple ,list are supported by concatenation .
# dictionary , set  are does not supported by concatenation .  (directly)

#number
a=123
b=234
c=a+b
print(c)
print(type(c))

#string 
a='123'
b="roshani"
c=a+b
print(c)
print(type(c))

#tuple
a=(1,2,3,'raj')
b=(1,2,3,'kadam')
c=a+b
print(c)
print(type(c))

#list
a=[1]
b=[24]
c=a+b
print(c)
d=[25]
d=c+d
print(d)
print(type(d))

# dictionary
a={'a':1}
b={'b':2}
c={3:'c'}
# d =a+b+c  print(d) concatenation does not support dictionary
e=(a,b,c) 
print(e)
print(type(e))

#set 
a={1,2,6}
b={3,4,5}
#c=a+b
#print(c)  print(c) concatenation does not support dictionary
d=(a,b)
print(d)
print(type(d))
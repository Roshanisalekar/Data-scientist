#Replication  operation 

# number ,string ,tuple ,list are supported by Replication .
# dictionary , set  are does not supported by Replication .  (directly)

#number
a=123
b=234
c=a*b
print(c)
print(type(c))

#string 
a='roshani'
b=a*3
print(b)
c=(a+" ")*3
print(c)
print(type(c))

#tuple
a=('raj') # why datatype string this is tuple  because of  only one value .interpreted can be assume that string 
b=a*3
print(b)
print(type(b))

#list
a=[1,3,2,"raj"]
b=[4,5,6,'kadam']
c=[a,b]*3
print(c)
print(type(c))
#d=(a+" "+b)*3
#print(d)

# dictionary
a ={'a':'b','c':2}
b={'d':5}
c=(a,b)
print(c)
print(type(c))
#c=a*3            print(d) Replication does not support dictionary
#d=(Dict(a*3))
#print(d)

# set 
a={1,'raj'}
b={3,'kadam'}
c=(a,b)*3
print(c)
print(type(c))

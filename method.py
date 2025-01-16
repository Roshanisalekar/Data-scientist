#string
print('string')
a="My nAmE is rOsHanI"
print(len(a))
print(a.upper())
print(a.capitalize())
print(a.find('A'))
print(a.index("r"))
print(a.find('x'))
print(a.find('z'))

b=a.upper()
print(b)
b=a.replace('rOsHanI','Gajani')
print(b)

#tuple
print('tuple')
a=(1,2,3,-24,1,1,1,2)
print(a)

print(a.index(2))
print(max(a))
print(min(a))
print(all(a))
print(any(a))
print(a.count(1))

a=(1,1,2,3,1,2,4,3,1)
b=(a[2:6:1]+a[-2: :1])
print(b)

#list
print('list')
x=[1,2,'Raj','jitender',4,5]
x.remove('jitender')
print(x)


#print(x.find(2))
x.insert(2,'manav')
print(x)
print("list method use")
a=['RAJ',1,2,-1.3]

a[3]='mahesh'
print(a)
a.insert(1,'kadam')# insert value in list
print(a)

#a.clear(3)#TypeError: list.clear() takes no arguments (1 given)
print(a)

#a[3]=null#NameError: name 'null' is not defined
print(a)

del a[3] #used to string delete 
print(a)

print("dictionary method use")

x={}# empty dictionary
x['a']=2
print(x) # insert to dictionary key and value 
x['b']=3 
x['c']=4 
x['d']=5
print(x)
x['a']=1
x['b']=2 
x['c']=3 
x['d']=4
print(x)
print(x.keys())  # find keys 
print(x.values()) #find values
print(x.items()) # find pair unique
print(x.get('c'))  # key ki value nikale / get value 
 
print(x.get('e',"doesn't exist"))
print(x.get('e',"5000"))
print(x)

print(x.setdefault('e',5000)) # add  value and key in dictionary using setdefault value
print(x)

print(x.setdefault('b',1000))
print(x)

del x['d']
print(x)



y={'f':7,'g':8,'h':9}
z=x,y
print(z)
print(type(z))
z=(x.update(y))
print(z)

ROSHANI=(x.update(y))
print(ROSHANI)
x.update(y)
print(x)

a=[1,2]
b=[3,4]#c=a,b //
c=a+b
print(c) # list
print(type(c))

print("variable using")
x=10
y=20
x=x+y # 10+20=30
y=x-y  #30-20=10
x=x-y #30-10=20
print(f"x={x}")
print(f"y={y}")

print("3 way variable using")
x=20
y=10
z=x
x=y
y=z
print(f"x={x}")
print(f"y={y}")


# set: unique element

a = {1, 1, 2, 3, 2, 4, 3, 5, 6}
b = {4, 4, 5, 5, 6, 4, 7, 8, 9}

# union : both  set element
# type :1
c = a | b
print(c)  # output:{1, 2, 3, 4, 5, 6, 7, 8, 9}

# type :2
d = a.union(b)
print(d)

# intersection : both common element
# type :1

e = a & b
print(e)

# type :2
d = a.intersection(b)  # output:{4, 5, 6}
print(d)


g=a-b
print(g) #output :{1, 2, 3} a set  may unique 
q=b-a
print(q) #output :{8, 9, 7}  b set may unique

#m=g+q
#print(q)#TypeError: unsupported operand type(s) for+: 'set' and 'set'


s=g|q
print(s)  #output :{1, 2, 3, 7, 8, 9}

r=a.copy() #output :{1, 2, 3, 4, 5, 6}
print(r)
 
r=b.copy()  #output :{4, 5, 6, 7, 8, 9}
print(r)

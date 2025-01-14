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
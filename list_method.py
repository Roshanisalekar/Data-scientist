a=[1,2,3,4,5,6]
a.append(7)
print(a)

a.append(10)
print(a)

a.append(15)
print(a)

a.extend([8,9,10])
print(a)

a.extend([12,34,56])
print(a)

a.extend(['@',"#","$"])
print(a)

a.insert(2,'three')
print(a)

a.insert(0,"roshani")
print(a)

a.insert(1,"savi")
print(a)

b=[2,6,9,7,5,3,2]
b.sort()
print(b)

b.count(3)
print(b)

b.sort(reverse=True)
print(b)

b.reverse()
print(b)

a.remove('three')
print(a)

a.pop(9)
print(a)
c=a.copy()
print(c)

c.clear()
print(c)

c.clear()
print(c)

c.append(567)
print(c)

c.extend([123,456,234,980,6789])
print(c)

d=c.copy()
print(d)

a={'dad':50,'mom':48,'sis':20,'bro':18}

print(a)

print(a.keys())

#.values()
print(a.values())

print(a.items())  #key and value pair with tuple

print(a.get('mom'))

print(a.get("uncle","dont have")) 
print(a)

print(a.update({'uncle':53}))
print(a)

print(a.update({'mom':45}))
print(a)

a.setdefault("mama",45)
print(a)

b={'unty':40,'c.bro':15}
a.update(b)
print(a)

a={1,2,3,4}
b={3,4,5,6}
print(a|b)

print(a.union(b))

print(b.union(a))

print(a&b)

print(a.intersection(b))

print(b.intersection(a))

print(a-b)
print(b-a)

print(a.difference(b))
c=set()
c=a.copy()
print(c)

# c.copy(a)# tyError: set.copy() takes no arguments (1 given)
# print(c)

c=b.copy()
print(c)

a.add(7)
print(a)

# a.add(b)#tpeError: unhashable type: 'set'
# print(a)
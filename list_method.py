#-------------------------------------------------------------------------------------------------------------------

                                        # list method 

# 1> append
# 2> remove 
# 3> insert 
# 4> pop 
# 5> extend 
# 6> index 
# 7> copy 
# 8> reverse 
# 9> sort
# 10> sort(reverse) 
# 11> count 
# 12> clear
#---------------------------------------------------------------------------------------------------------------------

# list method 
a=[1,2,3,"raj",6]
print(a)

#------------------------------------------------------------------------------------------------------------------------
# add element in list
# 4th  value add in list
a.append(4)
print(a)

# 8 value add in list
a.append(8)
print(a)

# 12 value add in list 
a.append(12)
print(a) 

# 16 value add in list 
a.append(16)
print(a)

# 20 value add in list 
a.append(20)
print(a)

#-------------------------------------------------------------------------------------------------------------------

# 20 value remove in list
a.remove(20)
print(a)

# 16 value remove in list 
a.remove(16)
print(a)

# 12 value remove in list 
a.remove(12)
print(a)

# 8 value remove in list 
a.remove(8)
print(a)

# 4 value remove in list 
a.remove(4)
print(a)

#------------------------------------------------------------------------------------------------------------

# add element in list with the help of list 

# 4 value add in list
a.insert(3,4)
print(a)

# 5 value add in list
a.insert(2,5)
print(a)

# 23 value add in list
a.insert(1,23)
print(a)

# 44 value add in list
a.insert(0,44)
print(a)

# 4 value add in list
a.insert(4,4)
print(a)

#--------------------------------------------------------------------------------------------------------------

# remove element in list with help of pop

# 4 value pop in list
a.pop(4)
print(a)

# 44 value remove in list 
a.pop(0)
print(a)

# 23 value pop in list
a.pop(1)
print(a)

# 5 value pop in list
a.pop(2)
print(a)

# 4 value pop in list
a.pop(3)
print(a)

#----------------------------------------------------------------------------------------------------------

# add list in the list with help of extend


b=[9,8,7,6]
a.extend(b)
print(a)

c=["manu","nanu"]
a.extend(c)
print(a)

d=["shamu",12,90]
a.extend(d)
print(a)

e=[(1,2,3)]
a.extend(e)
print(a)

f=[{56,78}]
a.extend(f)
print(a)

#----------------------------------------------------------------------------------------------------------------

# find value of with help find method
# find index manu
z=a.index("manu")
print(z)

# find index shamu
z=a.index("shamu")
print(z)


# find index raj
z=a.index("raj")
print(z)


# find index 90
z=a.index(90)
print(z)


# find index 12
z=a.index(12)
print(z)

# find index roshani

#z=a.index("roshni")
#print(z)

# ValueError: 'roshni' is not in list
#----------------------------------------------------------------------------------------------------------

# cpoy for new variable in list
z=a.copy()
print(z)

#----------------------------------------------------------------------------------------------------------

#  reverse for list 
a.reverse()
print(a)

#-----------------------------------------------------------------------------------------------------

# count for no of variable existed in list
a=a.count(6)
print(a)

#-----------------------------------------------------------------------------------------------------

# sorted are list

p=[10,38,5,6,74,2,8,6]
p.sort()
print(p)

#----------------------------------------------------------------------------------------------
# reverse sorted are list
p.sort(reverse=True)
print(p)

#--------------------------------------------------------------------------------------------------
# clear for list 
z.clear()
print(z)

#------------------------------------------------------------------------------------------------
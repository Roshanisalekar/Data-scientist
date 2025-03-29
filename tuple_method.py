#-----------------------------------------------------------------------------------------------------------------
#                                                           tuple method

# 1> count
# 2> index
# 3> all
# 4> any
# 5> max 
# 6> min
# 6> len

a=(1,2,3,"raj",5)
print(a)

# output :-
# (1, 2, 3, 'raj', 5)
#--------------------------------------------------------------------------------------------------------------

# tuple object directly not change 

#a[2]=14  # TypeError: 'tuple' object does not support item assignment
# print(a)
#------------------------------------------------------------------------------------------------------------

# tuple with one items

b=("roshani",)
print(b)
print(type(b))

# output:-
# <class 'tuple'>

#---------------------------------------------------------------------------------------------------------

# tuple length 

a=(1,2,3,"raj",5)
print(len(a))

# output:-
# 5
#------------------------------------------------------------------------------------------------------

# tuple max 

z=(1,23,57,4,6)
print(max(z))

#output :-
# 57

# ----------------------------------------------------------------------------------------------------------

# tuple min

z=(1,23,57,4,6)
print(min(z))

#output :-
# 1

#--------------------------------------------------------------------------------------------------------

# tuple all

z=(1,23,57,4,6)
print(all(z))

#output :-
# True

#------------------------------------------------------------------------------------------------------

# tuple any

z=(1,23,57,4,6)
print(any(z))


#--------------------------------------------------------------------------------------------------
# tuple count 

z=(1,23,57,4,4,4,6)
print(z.count(4))

# output :-
# 3

#----------------------------------------------------------------------------------------------------

#tuple index 

z=(1,23,57,4,6)
z=z.index(23)
print(z)

# output:-
# 1
#-------------------------------------------------------------------------------------------------------


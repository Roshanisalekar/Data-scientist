# program : 1
# addtion two value 
a=10
b=20
c=a+b
print(c)

# output : 30 
############################################################################################################
# program :2 

# addtion two value 

fun=(lambda a,b:a+b)
print(fun(30,40))
# output : 70

###########################################################################################################
# program :3
# addtion three  value 

lb=(lambda x,y,z:x-y-z)
print(lb(50,40,10))
# output : 0
#########################################################################################################
# program :4 
# print value :
1 
2
3
4
5

# lambda function not use for loop because lambda function one line code .

#for a in range(lambda x,y,z : x+y+z)
#print(a(ld(50,40,10)))

#########################################################################################################
# program :5 

fun=(lambda a,b:a>b)
print(fun(30,40))
# output : false

###############################################################################################################

# program :6 

#fun=(lambda a,b:a in b)
#print(fun(30,40)) 

#output : TypeError: argument of type 'int' is not iterable

#################################################################################################################

# program : 7


fun=(lambda a,b:a in b)
print(fun(10,(10,20,40)))

# output : true 
##################################################################################################################
# program : 8 

fun=(lambda a,b:a is b)
print(fun(10,(10,20,30)))

# output: false
###################################################################################################################

# program : 9


fun=(lambda a,b:a is b)
print(fun(10,10))

# output : true 
######################################################################################################################

# program : 10 


fun=(lambda a,b:a is b)
print(fun((10,20),10))

# output : false 

##############################################################################################################

# program : 11

fun=(lambda a,b:a is b)
print(fun(10,(10,20)))

# output : false 

########################################################################################################

# program :12

fun=(lambda a,b,c:a is b in c)
print(fun(10,10,(0.10,'10',10.00,10)))

# output : true 

######################################################################################################




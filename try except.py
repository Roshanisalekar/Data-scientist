# -------------------------------Indexerror-------------------------------------------

# program : 1
#---------------------------------------------------------------------------------------


# list=[10,20,30]
# #print(list)
# try:
#     print(list[4])
# except IndexError as msg:
#     print("find the error :- ",msg)
# else:
#     print("there is no error")
# finally:
#     print("no matter what it is,program done")



# output 1:

# find the error :-  list index out of range
# no matter what it is,program done

# output 2 :

# 20
# there is no error
# no matter what it is,program done

#--------------------------------------Nameerror---------------------------------------------------

# program : 2
#---------------------------------------------------------------------------------------------------

# a=10
# #print(y)

# try:
#     print(y)
# except NameError as msg:
#     print("find the error :-",msg)
# else:
#     print("threr is no error")
# finally:
#     print("no matter what it is,program done ")

# output :

# find the error :- name 'y' is not defined
# no matter what it is,program done


#--------------------------------------Typeerror---------------------------------------------------

# program : 3
#---------------------------------------------------------------------------------------------------

# a='10'
# b=20


# try:
#     c=a/b
#     print(c)
# except TypeError as msg:
#     print("find the error :-",msg)
# else:
#     print("there is no error")
# finally:
#     print("no matter what it is ,program done")

# output:

# find the error :- unsupported operand type(s) for /: 'str' and 'int'
# no matter what it is ,program done


#--------------------------------------attributeserror---------------------------------------------------

# program : 4
#---------------------------------------------------------------------------------------------------

# str1="my name is roshani"


# try:
#     str1=str1.reversed()
#     print(str1)
# except AttributeError as msg:
#     print("find the error :-",msg)
# else:
#     print("there is no error")
# finally:
#     print("no matter what it is ,program done")

# output:

# find the error :- 'str' object has no attribute 'reversed'
# no matter what it is ,program done

#--------------------------------------zeroerror---------------------------------------------------

# program : 5
#---------------------------------------------------------------------------------------------------

# a=int(input("enter a num1 :"))
# b=int(input("enter a num2 :"))
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError as msg:
#     print("find the error :-",msg)
# finally:
#     print("no matter what it is,program done")

# output:

# enter a num1 :12
# enter a num2 :0
# find the error :- division by zero
# no matter what it is,program done 

#--------------------------------------valueerror---------------------------------------------------

# program : 6
#---------------------------------------------------------------------------------------------------

# a=int(input("enter a num1 :"))
# b=int(input("enter a num2 :"))


# try:
#     print(a/b)
# except ValueError as msg:
#     print("find the error :-",msg)
# else:
#     print("there is no error")
# finally:
#     print("no matter what it is , program done")

# output:

# b=int(input("enter a num2 :"))
#       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'python'


#-------------------------------------------  FileNotFoundError------------------------------------

# program : 7 
#---------------------------------------------------------------------------------------------------

a=open("C:\Data scientist\what is errror.py",'r')

try :
    content=a.read()
    print(content)
except FileNotFoundError as msg:
    print("find the error :-")
else:
    print("there is no error")
finally:
    print("no matter what it is, program code")

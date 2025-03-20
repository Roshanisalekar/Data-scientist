# if-elif-else statement : the condition is true then block of executed when elif condition is true then block of executed  but condition is false then else part will be excuted.

# syntax :
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# example :

"check whether age is grater than equal to 18 or not"

age=int(input("enter your age :"))
if age>=18:
    print("you can vote!")
elif age<=0:
    print("invalid age")
else:
    print("you cannot vote ")
print("thanks")

# output:

# enter your age :0
# invalid age
# thanks
# example NO  :1

# write a program to take marks and get greate as output for this condition 

print("if else ladder")
mark=float(input("enter a marks :"))


if mark<=100 and mark>=75 :
    print("A+")
elif mark>=100:
    print("invalid marks")
elif mark>=65:
    print("A")
elif mark>=55:
    print("B")
elif mark>=45:
    print("C")  
elif mark>=35:
    print("D")
else:
   print('FAIL')


# example NO  :2

#write a program check the given number divisible by 4 or 11 .

n=int(input("enter a number :"))
if(n%4==0):
    print("divisible by 4")
elif (n!=38):
    print("not divisible by 38")
else:
    print("not divisible")



# example NO  : 3 

# write a program check whether the given year leap year or not .

n=int(input("enter a years :"))

if(n%400==0) or (n%4==0 and n%100!=0):
    print("this is leap years")
else:
    print("this is not leap years")





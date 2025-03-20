#break :  The break keyword is used to break out a for loop, or a while loop.

# example : 1
for i in range(1,10):
    print(i)
    if i==5:
        break
print()

# example :2 
a=[1,2,3,45,5]
for i in a:
    print(i,end=" ")
    if i==45:
        break
print()

# example : 3

d="roshani salekar"
for i in d:
    print(i,end=" ")
    if i==" ":
        break
print()
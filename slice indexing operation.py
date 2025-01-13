#string slicing         
a="My name is Rajendra and he loves python"
#=012345678910
#you find Rajendra and he loves
b=a[11:-7:1]
print(b)

#you find Rajendra and he loves
b=a[11:-7:2]  # step :2
print(b)

#you find Rajendra loves python
b=a[11:20:1]+a[-12: :1]
print(b)

#tuple slicing
a=('a',1,2,'b','raj','abc@1','mahi')
#you find 2,b,mahi,abc1
b=(a[2],a[3],a[6],a[5][0:3:1]+a[5][4])
print(b)

#list slicing
a=('o',1,9,'b','car','payal','mahesh')
#you find 
b=[a[2],a[3],a[6],a[5][0:3:1]+a[5][4]]
print(b)

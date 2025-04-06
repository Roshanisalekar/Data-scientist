# example :1
if "raj":
    print("no")
else:
    print("yes")
# no

# example :2

# if raj:
#     print("no")
# else:
#     print("yes")

   #NameError: name 'raj' is not defined

# example :3

if (1,2,3):
    print("no")
else:
    print("yes")

# example :4
if []:
    print("no")
else:
    print("yes")

# example :5

a=0
if a:
    print("no")
else:
    print("yes")
# example :6

a=1
if a-1:
    print("no")
else:
    print("yes")

# example :7

a=1
if a-1:
    if a+5:
        print("y")
    else:
        print("n")
else:
    if "no":
        print("wow")
# example :8

a=1
if a-1:
    if a+5:
        print("y")
    else:
        print("n")
else:
    if a-1:
        print("wow")
    else:
        if a-1:
            print("r")
        else:
            print("w")

# example :9

a=25
if a>10:
    if a>20:
        if a>30:
            print("r")
        else:
            if a>25:
                print("m")
            else:
                print("n")
    else:
        print("q")
else:
    print("t")

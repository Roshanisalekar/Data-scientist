# example :- global  variable

choice="global"

def message():
    print("inside the function",choice)

message()


# example :- local  variable 
def msg():
    # local variable 
    choice="i love coding"
    print(choice)

msg()
# outside local variable use nahi karte 

#print(choice) # NameError: name 'choice' is not defined
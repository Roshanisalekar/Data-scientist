# 3 type of argument 

# 1> positional argument
# 2> keyword argument
# 3> defualt argument
# example :- 1 

# positional  argument

def greet(name):
    print('hi',name)

greet('sagar')

# output :-
# hi sagar
# example :- 2

# keyword argument 

def welcome(name,city):
    print(f'welcome {name} to the {city}')

welcome('roshani','newzearland')
welcome('newzearland','roshani')
welcome(name='roshani',city='newzealand')

# output :-

# welcome roshani to the newzearland
# welcome newzearland to the roshani
# welcome roshani to the newzealand

# example :- 3

# defualt argument 

def friend(name='nida',name1='niki'):
    print(f'my friends name is {name} and {name1}')

friend()
friend("savita",'ankush')

# output :

# my friends name is nida and niki
# my friends name is savita and ankush
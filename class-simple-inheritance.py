# simple inheritance :- simple inheritance is nothing but which contain only one parent class and only one child class .

class calcutation:

    num1=int(input("Enter a num1 :"))
    num2=int(input("Enter a num2 :"))

    def add(self):
        print("addtion :-",self.num1+self.num2)

    def sub(self):
        print("subtraction:-",self.num1-self.num2)

class simple(calcutation):

    
    def multi(self):
        print("multiplication :-",self.num1*self.num2)

    def div(self):
        print("division :-",self.num1/self.num2)

    
    def rem(self):
        print("reminder :-",self.num1%self.num2)


s=simple()

s.add()
s.sub()
s.multi()
s.div()
s.rem()

# output :-


# Enter a num1 :20
# Enter a num2 :10
# addtion :- 30        
# subtraction:- 10     
# multiplication :- 200
# division :- 2.0      
# reminder :- 0 
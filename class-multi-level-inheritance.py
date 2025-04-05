# multi-level inheritance  :- in this inheritance we have one parent class and multiple child class 

class father:
    surname="salekar"

class son(father):

    def show(self):
        print("ankush",self.surname)

class Grandson(son):

    def disp(self):
        print("amol",self.surname)
        print("sagar",self.surname)

s=son()
s.show()

# output :-   ankush salekar

g=Grandson()
g.disp()
g.show()

# output :- 

# amol salekar
# sagar salekar
# ankush salekar
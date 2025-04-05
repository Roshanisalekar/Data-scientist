# hierarchical inheritance :-  which contain one parent class and multiple child classes but each child class access parent class properties  

class father:
    surname="salekar"

    def show(self):
        print("my surname is ",self.surname)

class son1(father):
    
    def disp(self):
        print("my name is aakash ",self.surname)


class son2(father):
    
    def see(self):
        print("my name is sagar ",self.surname)

s1=son1()
s1.disp()
s1.show()

s2=son2()
s2.see()
s2.show()

# output:- 

# my name is aakash  salekar
# my surname is  salekar
# my name is sagar  salekar
# my surname is  salekar
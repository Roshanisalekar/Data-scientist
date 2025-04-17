abstraction :- hiding unnecesary details from user through class and method .

class student:

    def __init__(self,name,surname,percentage):
        self.name=name
        self.surname=surname
        self.percentage=percentage
    
    def student_details(self):
        
        print(f"{self.name } {self.surname } is percentage {self.percentage +2}%")


s1=student("roshni","salekar",56)
s1.student_details()

s2=student("nida","padel",90)
s2.student_details()
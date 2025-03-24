# create student class that takes name & marks of 3 subjects as argument in constructor .
# then create a method to print the average.

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def get(self):
        sum=0
        for val in self.mark:
            sum +=val
        print('hi',self.name,"your avg marks is",sum/3)
s1=student('roshani',[9.5,9.8,9.7])
print(s1.name)
print(s1.mark)
s1.get()
s1.name='sagar'
s1.mark=[2,3,4]
# s1.mark=[23,87,1]
print(s1.get())

# output :-

# roshani
# [9.5, 9.8, 9.7]
# hi roshani your avg marks is 9.666666666666666
# hi sagar your avg marks is 37.0
# None
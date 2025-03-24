
class person:
    __name="roshani"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()
        print("hide")
     

p1=person()
print(p1.welcome())

# p1.__hello() # AttributeError: 'person' object has no attribute '__hello'
#p1.__name  # AttributeError: 'person' object has no attribute '__name'

# output: 

# hello person
# hide
# None
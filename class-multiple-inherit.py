# multiple inheritance :- which contain more parent classes and only one child class is called multiple inheritance .

class roshani :

    back="oracle Db and java"
    def backend(self):
        print("backed task implemented using ",self.back)

class kaustubh :

    front="html ,css and javascript"
    def fronted(self):
        print("fronted task implemented using ",self.front)     

class Teamlead(kaustubh,roshani):

    def show(self):
        print("dynamic website created .....")


t=Teamlead()
t.fronted()
t.backend()
t.show()


# output:-

# fronted task implemented using  html ,css and javascript
# backed task implemented using  oracle Db and java
# dynamic website created .....
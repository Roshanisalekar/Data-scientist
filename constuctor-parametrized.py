class A:
    name="amol"
    age=58

    def __init__(self,name,age,grade):
        print(name,age,grade)

    def show(self):
        print(self.name)

a=A("savi",45,"o")
a.show()

b=A("sani",89,"A+")
c=A("kartik",87,"B+")

# output:-

# savi 45 o
# amol
# sani 89 A+
# kartik 87 B+
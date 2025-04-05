# same class may subko access kar sakte hai
# example : 1

class A:
    a=10  #public
    _b=20  #protected
    __c=None  # private

    print(a," ",_b," ",__c)

a=A()

# output:-
# 10   20   None

#----------------------------------------------------------------------------------------------------------------
#  same class and method may used kar sakte hai 

# example : 2

class A:
    a=10  #public
    _b=20  #protected
    __c=None  # private

    def add(self):
        self.__c = self.a + self._b
        print("addition two number ",self.__c)

acc=A()
acc.add()

# output:-
# addition two number  30

#----------------------------------------------------------------------------------------------------------------

# class ke bahar public and protected access karsakte hai but not access privete 

# example : 3


class A:
    a=10  #public
    _b=20  #protected
    __c=None  # private

    def add(self):
        self.__c = self.a + self._b
        print("addition two number ",self.__c)

acc=A()
acc.add()
#print(acc.a)
#print(acc._b)
#print(acc.__c)

# output:- 
# addition two number  30
# 10
# 20

# AttributeError: 'A' object has no attribute '__c'

#-----------------------------------------------------------------------------------------------------------

# derived class  :-  derived class may  public and protected access karte hai but not used privete 

# example :- 4 

class parents():
    a=10  #public
    _b=20  #protected
    __c=None  # private


class derived(parents):

    def show(self):
        print(self.a)
        print(self._b)
       # print(self.__c)  # AttributeError: 'derived' object has no attribute '_derived__c'

obj=derived()
obj.show()

# output:- 
# 10
# 

#--------------------------------------------------------------------------------------------------------------

# derived class ko object ke through access karen ge
# example :- 5 

class parents():
    a=10  #public
    _b=20  #protected
    __c=None  # private


class derived(parents):
    pass


obj=derived()

print(obj.a)
print(obj._b)
# print(obj.__c)  # AttributeError: 'derived' object has no attribute '__c'

# output:- 


# 10
# 20

# --------------------------------------------------------------------------------------------------

# one class  ke attribute used karke other class may used karo  

class A :
    a=20
    _b=40
    __c=60
    print(a," ",_b," ",__c)

class B:
    print(A.a)
    print(A._b)
    # print(A.__c)  # AttributeError: type object 'A' has no attribute '_B__c'. Did you mean: '_A__c'?

obj=b()

# output :- 
# 20   40   60
# 20
# 40

#---------------------------------------------------------------------------------------------------------------
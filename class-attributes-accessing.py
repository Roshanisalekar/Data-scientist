# class attributes accessing : object attributes is high priority as compare to class attributes (local attributes)

# 1> class attributes : class attributes access for used to (self. )
#-----------------------------------------------------------------------------------------------------------
# example :1   -----class attributes------

class family():
    father='amol'
    def __init__(self):

        print(f"{self.father}")

f1=family()

# output:-

# amol
#----------------------------------------------------------------------------------------------------------

# example :2    ----class attributes-----

class color():
    like='black'
    def __init__(self):
        print(f"{self.like}")

c1=color()
# output:-
# black

#-------------------------------------------------------------------------------------------------------------
# example : 3   ------object attributes---------

class student:
    name='sagar'
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print(f'{name} and {self.name}')


s1=student('roshni',mark=90)


# output:
# roshni and roshni

#-------------------------------------------------------------------------------------------------------------

# example : 4

class mobile():
    app="youtube"
    def __init__(self,app1,app2):
        self.app1=app1
        self.app2=app2
        print(f"{self.app} vs {app1}")

m1=mobile('enki','google')

# output :
# youtube vs enki

#--------------------------------------------------------------------------------------------------------------
# example : 5 -----object:local------

language="python"
class programming():
    language="c++"
    def __init__(self,language):
       # self.language=language
        print(f"{language} vs {self.language} vs {language}")
p1=programming('java')

# output:
# java vs c++ vs java

#--------------------------------------------------------------------------------------------------------------
# example : 6  -----global||| ------

language="python"
class programming():
    language="c++"   
    def __init__(self):
        self.language=language
        print(f"{language} vs {language} vs {self.language}")
p1=programming()

# output:
# python vs python vs python

#--------------------------------------------------------------------------------------------------------------
# example : 7  -----global||| ------

language="python"
class programming():
    language="c++"   
    def __init__(self):
        #self.language=language
        print(f"{language} vs {language} vs {self.language}")
p1=programming()

# output:
# python vs python vs c++


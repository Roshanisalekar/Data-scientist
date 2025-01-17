                      String method


(1) capitalize() : The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

example : 

txt = "python is FUN!"

            x = txt.capitalize()

             print (x)

(2)  Center () :  The center() method will center align the string, using a specified character (space is default) as the fill character.

example : 

txt = "banana"

        x = txt.center(20)

        print(x)

(3) Count () : The count() method returns the number of times a specified value appears in the string.

example :

 txt = "I love apples, apple are my favorite fruit"

           x = txt.count("apple")

           print(x)

(4) endswith () :  The endswith() method returns True if the string ends with the specified value, otherwise False.

example :

txt = "Hello, welcome to my world"

             x = txt.endswith("g")

             print(x)


(5)startswith () :The startswith() method returns True if the string starts with the specified value, otherwise False.

example :

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


(6) Find ()  : 

The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

example :

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


(7) index () :

The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.

example :

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

(8) strip () :

The strip() method removes any leading, and trailing whitespaces.

Leading means at the beginning of the string, trailing means at the end.

You can specify which character(s) to remove, if not, any whitespaces will be removed.

example : 
 
txt = "     nida     "

x = txt.strip()

print("of all friend", x, "is my favorite")

(9) rstrip () :

The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

example :

txt = "     Nida     "

x = txt.rstrip()

print("of all friends", x, "is my favorite")

(10) lstrip() : Remove spaces to the left of the string

txt = "     nida     "

x = txt.lstrip()

print("of all friends", x, "is my favorite")


(11) upper () :

The upper() method returns a string where all characters are in upper case.

Symbols and Numbers are ignored.

example :

txt = "Hello my friends"

x = txt.upper()

print(x)


(12)  replace () : The replace() method replaces a specified phrase with another specified phrase.

example :

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)








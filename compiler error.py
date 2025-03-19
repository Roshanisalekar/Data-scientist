
#program :  1 |||||||   expected ':'      |||||||||
# for i in range(1,10)
#     print('yes')
#     if (True):
#         print('yes')

# output :

# SyntaxError: expected ':'


#program : 2  |||||||   expected  :  IndentationError    |||||||||

# for i in range(1,10):
#     print('yes')
# if (True):
# print('yes')

# output:

# IndentationError: expected an indented block after 'if' statement on line 17

#program : 3  |||||||   expected :  ' (string not completed)      |||||||||

# for i in range(1,10):
#     print('yes')
#     if (True):
#         print('no)

# output :

# SyntaxError: unterminated string literal (detected at line 29)

# program :4  |||||||   expected :  ,       |||||||||

# for i in range(1 .10):
#     print('yes')
#     if (True):
#         print('no')

# output:



#SyntaxError: invalid syntax. Perhaps you forgot a comma?

# program : 5   |||||||   expected : ,      |||||||||

# for i in range(1 10):
#     print('yes')
#     if (True):
#         print('no')

# output:
#SyntaxError: invalid syntax. Perhaps you forgot a comma?

# program : 6   |||||||   expected  :  )     |||||||||

# for i in range(1,10:
#     print('yes')
#     if (True):
#         print('no')

# output:

# SyntaxError: invalid syntax

# program : 7   |||||||   expected : def     |||||||||

# sum(a,b):
#      c=a*b
#      print(c)

# sum(12,5)  

# output :

#SyntaxError: invalid syntax

# program :8   |||||||   expected :  value      |||||||||

# a=12
# b=    

# print(a+b)

# output :
# SyntaxError: invalid syntax


# program :9    |||||||   expected : b      |||||||||

# a=12
# b=23  

# print(a+)

# output :
# SyntaxError: invalid syntax

# program :10  |||||||   expected : =      |||||||||

# a 12
# b=23  

# print(a-b)

# output:
# SyntaxError: invalid syntax

# program :11   |||||||   expected : b      |||||||||

# def sum(a,b): 
#     c=a*
#     print(c)

# sum(12,5)

#output :
# SyntaxError: invalid syntax

# program :12  |||||||   expected : None is keyword     |||||||||

# def None(a,b): 
#     c=a*
#     print(c)

# None(12,5)
# output:

# SyntaxError: invalid syntax


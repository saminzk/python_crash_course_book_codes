# # x = 300
# def my_func():
#     global x
#     x = 200
#     # print(x)

# my_func()
# print(x)

# def myFunc1():
#     x = 'Jane'
#     def myFunc2():
#         nonlocal x
#         x = 'hello'
#     myFunc2()
#     return x

# print(myFunc1())

# x = "global"

# def outer():
#     x = 'enclosing'
#     def inner():
#         x = 'local'
#         print("Inner: ",x)
#     inner()
#     print('outer: ',x)

# outer()
# print("global: ",x )

# def changeCase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changeCase
# def myFunction():
#     return 'Hello Sally'


# @changeCase
# def otherFunction():
#     return 'I am speed.'

def myFunction():
    return "Have a great day."


print(myFunction.__doc__)
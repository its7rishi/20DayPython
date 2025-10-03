""" SCOPE """

# * Local Scope
# variables created inside a function belong to the local scope of that function,
# and can only be used inside that function.
""" 
def myfunc():
    x = 300
    print(x)  

myfunc()  # 300
# print(x)  # Error: x is not defined
 """


# * Function Inside Function

# ? local variable can be accessed from an inner function
""" 
def myfunc():
    x = 300
    
    def myInnerFunction():
        print(x)

    myInnerFunction()
 """

# * Global Scope
# variables created in the main body of the code are global variables and belong to the global scope  
""" 
x = 300

def myfunc():
    print(x)

myfunc()  # 300

 """

# * Naming Variables
# If you create a variable with the same name inside a function, this variable will be local
x = 300

def myfunc():
    x = 200
    print(x)  

myfunc()  # 200
print(x)  # 300


# * Global Keyword
# If you need to create a global variable, but are stuck in the local scope,
# you can use the global keyword to declare which variables are global.

# Example 1

""" 

def globalFunc():
    global x
    x = 300

globalFunc()

print(x)  # 300 
 """

# Example 2
""" 
y = 500

def  myFlobalFunc():
    global y
    y = 300

myFlobalFunc()

print(y)  # 300
 """

# * Non Local Keyword
# The nonlocal keyword is used to work with variables inside nested functions,
# where the variable should not belong to the inner function.
# Use the nonlocal keyword to declare that the variable is not local.

def myfunc():
    x = 'Jane'
    def myfunc2():
        nonlocal x
        x = "Hello"
    myfunc2()
    return x

print(myfunc())  # Hello
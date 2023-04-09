""" A variable inside a function is only
    available to the functions inside the
    function itself"""

def myFun1():
    x = 30
    print(x)


def myFun2():
    x = 30
    print(x)

    # Lets create another function that will use the x variable
    def myInnerFun():
        a = x + 50
        print(a)

    # Calling second function from the main function
    myInnerFun()


print("\n\n---- The first function with same variable -----\n\n")
myFun1()

print("\n\n---- The inner function with same variable -----\n\n")
myFun2()




print("\n\n------ Global Variables ----------\n\n")

""" Global variable can be access from
    anywhere within your code space
"""

x = 600

def myNum():
    a = x + 2
    print(a)


# Call method to see if global variable was accessed and increment by 2
print("---- Calling the variable from inside a method----")
myNum()

print("\n\n---- Calling the variable from inside a method----")
# Call the variable itself outside to see if we got the actual value of the
# Global variable
print(x)


print("\n\n------ Global Variables From Inside A Method----------\n\n")

""" Global variable can be accessed from inside
    a function hence, you have to use the keyword 'global'
"""

def myEcs():
    global x
    x = 50
    a = x + 5
    print(a)

#Call the method from outside
print("\n\nPrint the result of the method call. The original value of x should be incremented by 5")
myEcs()

# Print the variable from outside the function
print("\n\nPrint the result of the original value of x. This should be 50")
print(x)


























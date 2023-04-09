import math

"""
    Checking the minimum and maximum
    using math function in python
"""

# Finding minimum using math func
x = min(45, 78, 8)
print("The minimum of [45, 78, 8] is = " + str(x))


# Finding maximum using math func
x = max(45, 78, 8)
print("The minimum of [45, 78, 8] is = " + str(x))


# The abs func from math return the absolute whole number of a given number
decimalNum = abs(-5.89)
print("The abs of the decimal number is " + str(decimalNum))

# The pow func from math func returns the x to the power of y
powOf = pow(4, 5)
print("The power of 4 to 5 is " + str(powOf))


# From the math module, we can get the square root method to find the sqrt of any num
mySqrt = math.sqrt(5)
print("The square root of 5 is " + str(mySqrt))

# We can use the ceil func from math to round up the result of sqrt of 5
print("The round up of the sqrt of 5 is " + str(math.ceil(mySqrt)))

# We can use the floor func from math to round down the result of sqrt of 5
print("The round down of the sqrt of 5 is " + str(math.floor(mySqrt)))

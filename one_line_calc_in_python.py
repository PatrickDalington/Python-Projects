####### SINGLE LINE CALCULATOR PROJECT ############
"""
More features will be added as time goes on!
Let me know if you would like to contribute.
I will also appreciate your feedback.
Thank you!!!
"""


"""
Lessons:
    1. Lists in python
        (a) pop() submethod of list
    2. Strings
        (a) String slicing
        (b) Length of String
    3. Functions
        (a) Function with parameters
        (b) Function without parameters
    4. Control Flow in Python
        (a) if statement
        (b) elif statement
    5. Type Casting in python
        (a) int
    6. Loop
        (a) For Loop

    7. Print method in Python
"""


#Begining of code

#Function for adding both numbers
def addition(a, b):
    return a + b

#Function for multiplying both numbers
def multiplication(a, b):
    return a * b

#Functiton for subtracting one number from the other
def subtraction(a, b):
    return a - b

#Function for dividing numbers
def division(a, b):
    return a / b

#This function check if the user would like to continue using the calc.
def checkResponse():
    response = input("Would you like to continue? Y/N:  ")
    if response == 'Y' or response == 'y':
        getInput()
    elif response == 'N' or response == 'n':
        # If no, then we showed a little appreciation to the user for using our calculator ):
        print("\n\nThank you for using Patrick's Calculator\n\n")


#Displaying simple title for the calculator
print("\n\n=============== Simple Calculator In Python ===============\n")



#This function runs the calcutions
def getInput():
    
    i = input('Enter figures\n') #Getting input from user
    lv = [] #Store numbers from left to the point of symbole( [898]+, -, * ...)
    rv = [] #Store numbers to the right after the symbol ( +, -, *...[356])
    lc=0    #Using this varable to track how many numbers comes before the symbol


    # Looping through to check where the symbol starts before string slicing
    for sign in i:

        # If sign reach then...Yayy, we got to a symbol. Now check which symbol using conditional statement
        if sign == '+':

            # Slice string inputed from zero to how many times it looped before getting to the (+) symbol.
            # I tracked this incrementing lv (left value each time until symbol reached)
            lv.append(i[0:lc])

            # Slice the string again this time adding 1 to the left value (lv)
            # Reason for removing one is becasue the symbol is a value and you don't want to include it in the right values (rv)
            # So therefore we removed it by adding one to the left value and stretching it all to the len of string to get all values at the right hand side.
            rv.append(i[lc + 1:len(i)])

            # Since we had created a function earlier that takes two aurguments, We decleared variables a and b
            # Again, since we are doing calculation here, we have to type cast the value inputed by the user explicitly.
            # Please note that every input gotten from the user through the input method returns a string. You have to type cast for your use case.
            # The pop method used here is to call the first item of the lv and rv. Remenber we sliced the original inputed string and stored the accordingly [rv/lv]
            a = int(lv.pop())
            b = int (rv.pop())

            # Right here we called the addition function inside the print method and pass the aurguments a and b to it.
            # This will print the result of the 
            print(addition(a, b))


            # It is time for you to ask the user if they want to continue. We created the function earlier called checkResponse() at the top.
            # You can go back and read through the content of this method again.
            checkResponse()

            # We break the loop to prevent it from running forever.
            break
        
        elif sign == '-':
            lv.append(i[0:lc])
            rv.append(i[lc + 1:len(i)])
            a = int(lv.pop())
            b = int (rv.pop())
            print(subtraction(a, b))
            checkResponse()
            break
        elif sign == '*':
            lv.append(i[0:lc])
            rv.append(i[lc + 1:len(i)])
            a = int(lv.pop())
            b = int(rv.pop())
            print(multiplication(a, b))
            checkResponse()
            break
        elif sign == '/':
            lv.append(i[0:lc])
            rv.append(i[lc + 1:len(i)])
            a = int(lv.pop())
            b = int(rv.pop())
            print(division(a, b))
            checkResponse()
            break

        # Increamenting left count since we haven't gotten to the symbol (+, -, *....)
        # This is important because it tells us how many numbers are before the symbol. Knowing the number will let us know what to store in the left value list.
        lc = lc + 1
        

# Call the main method    
getInput()










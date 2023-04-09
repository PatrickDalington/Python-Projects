import helloModule
import platform

# Getting the operating system of your pc
x = platform.system()
print("\n\nYour operating system is " + x + "\n\n")



# Getting the dir
x = dir(platform)
print("\n\nDir is:\n\n")
print(x)


helloModule.sayHello("Patrick")

cal = helloModule.MyCalculator(100, 60)
cal.addition()

cal = helloModule.MyCalculator(100, 50)
cal.subtraction()

cal = helloModule.MyCalculator(100, 50)
cal.multiplication()

cal = helloModule.MyCalculator(100, 50)
cal.division()

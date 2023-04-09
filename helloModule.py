def sayHello(name):
    print("Hello, " + name)

def cal(a, b):
    result = a + b
    return result

class MyCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        print("\n\nThe addition of " + str(self.x) + " and " + str(self.y) + " is:")
        print(self.x + self.y)

    def subtraction(self):
        print("\n\nThe subtraction of " + str(self.y) + " from " + str(self.x) + " is:")
        print(self.x - self.y)

    def multiplication(self):
        print("\n\nThe multiplication of " + str(self.x) + " and " + str(self.y) + " is:")
        print(self.x * self.y)

    def division(self):
        print("\n\nThe division of " + str(self.x) + " and " + str(self.y) + " is:")
        print(self.x / self.y)

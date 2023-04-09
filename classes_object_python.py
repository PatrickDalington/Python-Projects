


"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Patrick", 27)
person2 = Person("Sandra", 23)

print(person1.name)
print(person1.age)

print('---------------------------------')

print(person2.name)
print(person2.age)

"""
print("-----------------Student Record -----------------")

"""String representation in a class"""








"""Creating empty class"""
class MyEmptyClass:
    #input pass to avoid error
    pass









""" Creating A Class for Student Records"""

class Students:
    def __init__(self, name, subject, score):
        self.name = name
        self.subject = subject
        self.score = score

    def __str__(self):
        return f"{self.name}{self.subject}({self.score})"

    def sayHello(self):
        print("I am " + self.name + ",\nThis is my score")


students = [["Patrick", "English", 78], ["Tobi", "English", 90],
            ["Olayinka", "English", 65]]

counter = 0
for x in students:
    counter = counter + 1

    print("\n--------------------- Stuent: " + str(counter) + "------------------")

    if counter ==  2:
        x[2] = 100
        st = Students(x[0], x[1], x[2])
        del st.subject
    else:
        st = Students(x[0], x[1], x[2])
        
    st.sayHello()
    print(x[1] + ": " + str(x[2]))

print("\n\n--------------End Of Student Record--------------\n\n")
    

student1 = Students("Benard", "English", 67)
student1.sayHello()

print(student1.subject + ": " + str(student1.score))



print("\n\n\n----------------------------\n\n\n")






""" Creating A child Class that Inherite From The Parent Class Students"""

class Teachers(Students):
    
    def __init__(self, name, subject, score, teacherName):
        super().__init__(name, subject, score)
        self.teacherName = teacherName

    def sayWelcome(self):
        print("Hello Everyone\nMy name is " + self.name + ".\nMy best subject is "
              + self.subject + ".\nI scored "
              + str(self.score) + "% last semester.\nMr " + self.teacherName
              + " is my best lecturer.\nThank you for coming to my convocation!\n")
        


teacher1 = Teachers("Tonia", "Biology", 98, "Bryant")
teacher1.sayWelcome()
print(teacher1.teacherName)




























myTuple = ("Rice", "Beans", "Spagetti")
interate = iter(myTuple)

""" The following will print the content of myTupple hence it has a next value"""
print(next(interate))
print(next(interate))
print(next(interate))

""" Let us try to iterate through string"""
myName = "Patrick"
interate = iter(myName)


print("\n\n-------Without For Loop----------\n\n")

#Without for loop
print(next(interate))
print(next(interate))
print(next(interate))
print(next(interate))
print(next(interate))
print(next(interate))
print(next(interate))


print("\n\n-------With For Loop----------\n\n")
#Using for loop
for x in myName:
    print(x)
    


""" Iterator Class in Python """

print("\n\n---------- Interator Class ---------------\n\n")

class IncrementNums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


inc = IncrementNums()
myInc = iter(inc)

# Without for loop

print(next(myInc))
print(next(myInc))
print(next(myInc))
print(next(myInc))


# With for loop

for x in myInc:
    print("\n\nNo: " + str(x))

























import json

""" Learning how to use json (Java Script Data) in python.
    Converting json data to python dictionary.
"""

# Example of json file

studentInfo = '{"name":"Patrick","age":40,"city": "Alabama"}'


""" Lets convert the json file to what python can identify
    After loaded with submethod of json, Python can now identify the datas
    as a python dictionary.
"""

# Pass the studentInfo
pythonDic = json.loads(studentInfo)

# Now we have all studentInfo stored in pythonDic as dictionary.
# Lets try to access some data from the studentInfo

# Print city of the student
print(pythonDic["city"])

# Print name of the student
print(pythonDic["name"])


""" Let us try to convert python dictionary to json file """

# Python dictionary

student1 = {"name":"Opara Daniel"
            , "Age":70
            , "DOB":"20/09/1997"}


# We can use json.dump to convert the above dictionary to json file

jData = json.dumps(student1)


# Lets print it out so that we can see how the json file look like
print(jData)



# Lets convert a Python object containing all the legal data types:

print("\n\n-------------- Raw Data -------------------------")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))



# To make the above data very easy to read, the dumps method has parameter space
# for how you may want to indent the result or data.

print("\n\n-------------- Organized Data -------------------------")
print(json.dumps(x, indent=4))


# We can further organize the data passed

print("\n\n-------------- More Organized Data -------------------------")
print(json.dumps(x, indent=4, separators=(". ", " = ")))
















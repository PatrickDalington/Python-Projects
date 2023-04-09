Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======= RESTART: C:\Users\HP\Documents\Python-Projects\json_in_python.py =======
Alabama
Patrick
{"name": "Opara Daniel", "Age": 70, "DOB": "20/09/1997"}


-------------- Raw Data -------------------------
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}


-------------- Organized Data -------------------------
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}


-------------- More Organized Data -------------------------
{
    "name" = "John". 
    "age" = 30. 
    "married" = true. 
    "divorced" = false. 
    "children" = [
        "Ann". 
        "Billy"
    ]. 
    "pets" = null. 
    "cars" = [
        {
            "model" = "BMW 230". 
            "mpg" = 27.5
        }. 
        {
            "model" = "Ford Edge". 
            "mpg" = 24.1
        }
    ]
}

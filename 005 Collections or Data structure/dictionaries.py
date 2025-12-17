# Dictionaries are used to store data values in key:value pairs
# A Disctionary is a collection which is ordered(in python version 3.7, dictionaries are ordered. Earlier, dictionaries are unordered), changeable and do not allow duplicates.
# Dictionaries are written with curly brackets {}, and have keys and values
car = {
    "brand": "BMW",
    "model": "M4 Competition",
    "Year": "2026"
}
print(car)

# Dictionary items can be referred to by using the key name.
print(car["brand"])

# Duplicates not allowed : Duplicate values will overwrite existing values
car = {
    "brand": "BMW",
    "model": "M4 Competition",
    "Year": "2026",
    "Year": "2020"
}
print(car)

# Dictionary length : use len() method get length of the dictionary
print(len(car))

# Dictionary items can be of any data type
sportCar = {
    "brand": "Porsche",
    "electrice": False,
    "model": "911 gt3 RS",
    "year": 2024,
    "colors" : ["red", "white", "blue"]
}
print(sportCar)

# It is also possiable to use the dict() constructor to make a dictionary
myCar = dict(brand="BMW", model="M5 Competition", year=2025, color="blue")
print(myCar)

#
# Access Dictionary items : 
# we can use get() as similer to use key
print(myCar.get("brand"))
print(myCar.get("color"))
# keys(): will return a list of all the keys in the dictionary
carKeys = myCar.keys()
print(carKeys)
# The list of keys is the view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
myCar["price"] = "2.4cr"   
print(carKeys)

# values(): method will return a list of all the vlaued in the dictionary
carValues = myCar.values()
print(carValues)
# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will reflected in the values list.
myCar["color"] = "red"
print(carValues)

# item() : will return eache item in a dictionary, as tuple in a list
carItems = myCar.items()
print(carItems)

# Check if the key exists : using "in"
if "brand" in myCar:
    print(f"The brand of my car is : {myCar["brand"]}")
else:
    print("You don't have a brand property.")
    
# 
# Change values :
# using key name 
myCar["price"] = "3cr"
print(myCar)
# using "update()" method
myCar.update({"price": "3.2cr"})
print(myCar)

# 
# Add new item: 
# using a new index key and assigning a value to it:
myCar["engin"] = "V8 4.4L twin turbo"
print(myCar)
# using update() method:
myCar.update({"seating_capacity": 4}) 
print(myCar)

#
# Removing items:
# pop(key) : removes the item with the specified key name
myCar.pop("seating_capacity")
print(myCar)

# popitem() : removes the last inserted item (in versions before 3.7, a random item is removed)
myCar.popitem()
print(myCar)

# del keyword removes the item with specified key name
del myCar["price"]
print(myCar)
# "del" can also delete the dictionary completely
del sportCar
# print(sportCar)
# Clear() : empties the dictionary
car.clear()
print(car)

#
# Loop through dictionary
# by default for loop with dictionary, it returns only keys of the dictionary
for i in myCar:
    print(i)
print()
# return values
for i in myCar.values():
    print(i)
print()
# or
for i in myCar:
    print(myCar[i])
print()
# Loop through both key and value by using the items() method
for x,y in myCar.items():
    print(x, y)

#
# Copy a Dictionary
# you can not copy a dictionary simply by typing dict2 = dict1 , because dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be make in dict2.
# make a copy of a dictionary with the copy() method
newCar = myCar.copy()
print(newCar)
# using buit-in "dict()"
newCar = dict(myCar)
print(newCar)

#
# nested dictionary
myCars = {
    "car1" : {
        "brand": "BMW",
        "model" : "M5 Competition",
        "year" : 2025,
        "color" : "Blue"
    },
    "car2" : {
        "brand": "Mercedes",
        "model" : "AMG G63",
        "year" : 2024,
        "color" : "Black"
    },
    "car3" : {
        "brand": "Porsche",
        "model" : "911 GT3 RS",
        "year" : 2023,
        "color" : "Yellow"
    }, 
}
print(myCars)
print(myCars["car2"]["brand"])
print(myCars["car3"]["model"])
# loop through nested dictionary:
for x, obj in myCars.items():
    print(x)
    for y in obj:
        print(y, ":", obj[y])
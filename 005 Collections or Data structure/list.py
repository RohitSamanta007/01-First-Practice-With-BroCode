# collection = single "variable" used to store multiple values

# List = [] -> items are ordered, changeable, and allow duplicate values.
# Ordered = the items have a defined order, and the order will not change, if we add new items
# Changeable = can change the value of a item, add item, delete an item
# list can contain differnt data types.
list1 = ["abc", 34, True, 40.3]

fruits = ["apple", "bannana", "orange", "mango"]

print(fruits[1])
print(fruits[1:3])
print(fruits[3:1:-1])

# Negative indexing means start from the end
print(fruits[-1]) # -1 refers to last item
print(fruits[-2]) # -2 refers to second last items in the list

# check if an item exists using "in" keyword
if "apple" in fruits:
    print("Yes apple is in the list")
else:
    print("Apple is missing in the list")

# list length = determine number of items in a list using "len()" function
print(f"The length of the fruits list is : {len(fruits)}")

# list constuctor
cars = list(("Thar Roxx", "BMW m340i", "Audi RS Q8", "AMG G63"))
print(cars)
print(f"The type of cars list is : {type(cars)}")

# change the item value
fruits[0] = "Coconut"
print(fruits)

#
# change the range of item values
fruits[:2] = ["Watemelon", "Cherry"]
print(fruits)
# change the second value by replacing it with two new values
fruits[1:2] = ["Apple", "Bannana"] # the length of the list will change when the number of items inserted does not match the number of items replaced
print(fruits)
fruits[1:3] = ["Apple"] # if we inserted less item than we replace, the new items will be inserted where you specified, and the remaining items will move accordingly
print(fruits)

#
# insert(index, value) => insert a new item, without replacing any of the existing values
fruits.insert(2, "Bannana")
print(fruits)

# append(value)  => add an item to the end of the list
fruits.append("DragonFruits")
print(fruits)

# Extend list -> append elements from another list to the current list using "extend()": elements will be added to the end of the list
another_fruits = ["papaya", "Jackfruit"]
fruits.extend(another_fruits)
print(fruits)

#
# Remove list items
# Remove specified item - using "remove()" -> it removes the first occurrence if duplicates exists
fruits.remove("papaya")
print(fruits)

# remove specified index using "pop(index)"
fruits.pop(1)
print(fruits)
#if we do not specify the index "pop()" will remove the last item
fruits.pop()
print(fruits)

# del keyword also removes the specified index
del fruits[0]
print(fruits)
# "del" keyword can also delete the list completely
del cars
# print(cars) # it gives error as this list don't exists any more

# clear() -> empties the list => list still remains, but it has no content
another_fruits.clear()
print(another_fruits)

#
# List Comprehension : offers a shoter syntex when you want to create a new list based on the value of an existing list.
fruits.append("cherry")
fruits.append("apple")
print(fruits)
# Q: Wanat a list containing only the fruits with the letter "a" in this name
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(f"The newlist items containing the character 'a' : {newlist}")

# the above code can be written short in this from with the help of list comprehension:
newlist = [x for x in fruits if "a" in x]
print(f"The newlist items containing the character 'a' with list-comprehension : {newlist}")
# syntax : newlist = [expression for item in iterable if condition == True]
# The reutrn value is a new list, leaving the old list unchanged.

# accept items that are not "apple"
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# accept only number lower than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)

# set the values in the new list to upper case
newlist = [x.upper() for x in fruits]
print(newlist)

# set all values in the new list to "hello"
newlist = ["Hello" for x in fruits]
print(newlist)

# return "orange" instead of "banana"
newlist = [x if x != "Bannana" else "orange" for x in fruits]
print(newlist)


#
# Sort List => using "sort()" -> sort the list alphanumerically , ascending by default
fruits.sort() # sort the list alphabetically in ascending order -> sort() method is case sensitive, resulting in all capital letters being sorted before lower case letter
print(fruits)

# case insensitive sort
fruits.sort(key = str.lower)
print(fruits)

# sort the list in descending order
fruits.sort(reverse=True)
print(fruits)
fruits.sort(reverse=True, key=str.lower) # case insensitive sort
print(fruits)

# Customize sort function
def myFunction(n):
    return abs(n-50)

newlist = [100, 50, 65, 82, 23]
newlist.sort(key=myFunction)
print(newlist)

#
# Reverse the order of the list => reverse() : regurdless of alphabate
fruits.reverse()
print(fruits)

#
# Copy List : you can not copy a list simply typing "list2 = list1" because list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
# using "copy()" to copy a list
newlist = fruits.copy()
print(newlist)
newlist[0] = "Rohit Samanta"
print(fruits)
print(newlist)

#using "list()" method
newlist = list(fruits)
print(newlist)

#using slice ":" operator
newlist = fruits[:]
print(newlist)

#
# Join two list 
list1 = ["a", "b","a", "c", "a"]
list2 = [1, 2, 3]
# using "+":
list3 = list1 + list2
print(list3)

#
# "count(value)" : return the number of times the specified value appers in the list
print(list3.count("a"))


#
# 2d list : 
groceries = [
    ["apple", "banana", "orange"],
    ["onion", "garlic", "potato"],
    ["chicken", "egg", "fish"]
]
print(groceries)
print(groceries[2][1])

for i in groceries:
    for j in i:
        print(j, end=" ")
    print()
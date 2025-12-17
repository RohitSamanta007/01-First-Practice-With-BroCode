# A tuple is a collection which is ordered and unchangeable
# Tuples are written with rounded bracker ()

fruits = ("apple", "cherry", "banana" )
print(fruits)

# Tuple items are ordered, unchangeable, and allow duplicate values. and accessed by index tupel[index] from 0
# Ordered -> means that the items have a predefined order, and that order will not change
# unchangeable -> that we can not change, add , remove items after tuple has been created (but we can add another tuple to a tuple)
# allow duplicates -> since tuples are indexed, they can have items with the same value

# tupel length
print(len(fruits))
print(type(fruits))

# tuple with one item
name = ("Rohit Samanta") # it wil be consider as string
print(type(name))
name = ("Rohit Samanta",) # add comma (,) : now it consider as tuple 
print(type(name))


# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

# tuple constructor
newTuple = tuple((1, 2, 4, 5, 6, 2, 3))
print(type(newTuple))
print(newTuple)

#
# Access Tuple : same as list
print(fruits[0])
# Search the first occurence of the value and return its position
position = fruits.index("banana")
print(position)

#
# Change the tuple value
# Once the tuple is created , we can not change its values. Tuples are unchangeable, immutable
# But there is a workaround, You can convert the tuple into a list, change the list and convert the list back into a tuple
tempTuple = list(fruits)
tempTuple[1] = "Mango"
fruits = tuple(tempTuple)
print(fruits)
# we can add and remove item in a tuple in the same way above

#
# Add Tuple to a tuple : allowed normally
anotherFruits = ("Mango", "Coconut", "SugerCane")
fruits += anotherFruits
print(fruits)
# Multiply Tuples : multiply the content of a tuple a given number of times, you can use the * operator
multiplyTuple = fruits * 2
print(multiplyTuple)

#
# Unpacking a tuple : 
# when we create a tuple, we normally assign values to it. This is called "packing" a tuple
# We are also allowed to extract the values back into variables. This is called "unpacking"
(red, brown, green) = anotherFruits
print(red)
print(brown)
print(green)
# The number of variables must match the number of values in tuple, if not you must use a asterisk to collect the remaining values as a list
(red, orange, yellow, *another) = fruits
print(red)
print(orange)
print(yellow)
print(another)
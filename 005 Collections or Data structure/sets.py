# A set is a collection which is unordered, unchangeable, and unindexed. and do not allow duplicate values
# Set items are unchangeable, but we can remove and add new items
# sets are written with curly brackets
fruits = {"Apple", "Banana", "Mango"}
print(type(fruits))
print(fruits)

# Sets are unordered, so you cannot be sure in which order the items will appear. We can not be referred to by index or key 
# Items appear in a different order every time you use them

# Duplicates are not allowed -> duplicates values are ignored
newFruits = {"Coconut", "Cherry", "Watermelon", "Coconut"}
print(newFruits)

# The values True and 1 are considered the same value in sets, and are treated as duplicates -> appears only true
newSet = {"apple", "banana", True, 1, 2}
print(newSet)

# len() : determine how many items a set has -> it avoids duplicate in count
print(len(newFruits))

# you can not access items in a set by refering to an index or a key
# But you can loop through the set items using a for loop
for x in fruits:
    print(x)
# check for an item in set
print("Banana" in fruits)

#
# Add set items: using "add(item)"
fruits.add("Orange")
print(fruits)
# add items from another set to the current set : using "update()"
fruits.update(newFruits)
print(fruits)
# the object in the update() method does not have to be a set, it can be any iterable object(tuples, lists, dictionaries)

#
# Remove set items
# remove an item using: remove()
fruits.remove("Orange") # if the item to remove does not exists, it will raise an error
print(fruits)
# remove an items using: discard()
fruits.discard("Coconut") # if the item to remove does not exists, discard() will not raise an error.
print(fruits)
# we can also use the "pop()" method to remove an item , but it will remove a random item. so we can sure what item that gets removed. The return value of the "pop()" method is the removed item
temp = fruits.pop()
print(fruits)
print(temp)
# "del" keyword will delete the set completely
thisSet = {"Hello", "World"}
del thisSet
# print(thisSet) # it gives error as "thisSet" does not exists any more
# "clear()": empties the set
# newFruits.clear()
print(newFruits)

#
# Join Set : 
# union()  : returns a new set with all items from both sets
allFruits = fruits.union(newFruits)
print(allFruits)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
# we can use the "|" operator instead of the union() method
allFruits = fruits | newFruits
print(allFruits)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)
# the union() method allows we to join a set with the other data types, like list or tuples
# but the "|" operator only allows you to join sets with sets, and not with other data types like union()

# update() : changes the original set, and does not return a new set
set1.update(set2)
print(set1)
# both union() and update() will exclude any duplicates items

# intersection() : will return a new set, that only contains the items that are present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
# we can use the "&" operator instead of "intersection()" method
set4 = set1 & set2
print(set4)
# "&" operator only allows you to join sets with sets, and not other data types like you can with the intersection() method

# intersection_update() : will also keep only the duplicates, but it will change the original set instead of returing a new set.
set1.intersection_update(set2)
print(set1)

# difference() : method will return a new set that will contain only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
# we can use "-" operator instead of the difference() method
set4 = set1 - set2
print(set4)
#The "-"" operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

# symmetric_difference() : will keep only the elements that are not present in both sets
set5 = set1.symmetric_difference(set2)
print(set5)
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set6 = set1 ^ set2
print(set6)
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# frozenset : is immutable version of set. It contains unique, unordered, unchangeable elements, elements cannot be added or removed from a frozenset
# Create a frozenset:
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
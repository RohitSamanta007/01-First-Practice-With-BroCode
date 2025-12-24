# The "open()" function : Open a file for reading/writing or create, it take two parameters: filename, and mode(optional)
# Four different methods(modes) for opening a file:
# "r" -Read : Default value, Opens a file for reading, error if the file does not exists
# "a" -Append : Opens a file for appending, creats the file if it does not exists.
# "w" -Write : Opens a file for writing, creats the file if it does not exist
# "x" -Create : Creats the specified file, returns an error if the file exists

# In addition we can specify if the file should be handled as binary or text mode
# "t" -Text : Default value, Text mode
# "b" -Binary : Binary mode (e.g : images)

f = open("D:\\Python\\01 First Practice With BroCode\\011 File Handling\\text1.txt")
# f = open("text1.txt", "rt") # file should be in same working directory

# The "open()" function returns a file object, which has a "read()" method for reading the content of the file
print("Hello")
print(f.read())

print()

# we can also use "with" statement when opening a file
with open("text1.txt") as f:
    print(f.read())
# You do not have to worry about closing your files, the "with" statement takes care of that

# closing files : it is good practice to always close the file when you are done with it
# if you are not using the "with" statement, you must write a close statement in order to close the file
f.close()
# we should always close our file. In some case, due to buffering, changes made to a file may not show untill you colse the file.

# By default, the "read()" method returns the whole text, but you can also specify how many characters you want to return
print()
with open("text1.txt") as f:
    print(f.read(5)) # return the first 5 characters of the file
    
# You can return one line by using "readline()" method
with open('text1.txt') as f:
    print(f.readline())
    print(f.readline()) # by calling "readline()" two times, you can read the two first lines

# By lopping through the line of the file, you can read the whole file, line by line:
with open("text1.txt") as f:
    for x in f:
        print(x)
        
#
# Write to an Existing File: you must add a parameter to the "open()" function
# "a" -Append: Will append to the end of the file.
# "w" -Write : will overwrite any existing content.
with open("text1.txt", "a") as f:
    f.write("\nThis is appended file content")

print()

with open("text1.txt") as f:
    print(f.read())


# 
# Overwrite existing Content : use the "w" parameter
with open("text1.txt", "w") as f:
    f.write("New content of the file , that is replaced the previous one")

with open("text1.txt") as f:
    print(f.read())
    
    
# Create a new file : use "open()" method , with one the following parameter: 
# "x" -Create : will create a file, returns an error if the file exits
f = open("testFile.txt", "x")
f.close()


#
# Delete File 
# To delete file you must import the OS module, and run its "os.remove()" function.
import os
# os.remove("testFile.txt")

# To avoid getting an error, we might want to check if the file exists before you try to delete it
if os.path.exists("testFile.txt"):
    os.remove("testFile.txt")
else:
    print("The file does not exists")

# delete folder : use the "os.rmdir()" method
os.rmdir("newFolder") # You can only remove empty folders

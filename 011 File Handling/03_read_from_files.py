# Read text file
filePath = "./011 File Handling/text1.txt"

try:
    with open(filePath, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{filePath}' is not found")
except PermissionError:
    print(f"You do not have permission to read that file")


# Read json file content
print()
print("Content of the Json file")

import json

filePath = "./011 File Handling/output.json"

try:
    with open(filePath, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print(f"File '{filePath}' is not found")
except PermissionError:
    print(f"You do not have permission to read that file")


# Read csv file
print()
print("Content of the csv file")
import csv

filePath = "./011 File Handling/output.csv"

try:
    with open(filePath, "r") as file:
        content = csv.reader(file)
        for line in content:
            # print(line)
            print(line[0]) # access a specific collumn
except FileNotFoundError:
    print(f"File '{filePath}' is not found")
except PermissionError:
    print(f"You do not have permission to read that file")

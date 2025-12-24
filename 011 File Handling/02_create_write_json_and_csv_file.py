# Create a new json file with file content
import json

employee = {
    "name" : "Rohit Samanta",
    "position" : "Manager",
    "age" : 24
}

filePath = "./011 File Handling/output.json"

try:
    with open(filePath, "w") as file:
        json.dump(employee, file, indent=4) # convert json format to json string and write it to the json file
        print(f"json file '{filePath}' is created.")
        
except FileExistsError:
    print("That file already exists!")
    


# create a csv file with content : (CSV) : comma separated value
import csv

employees = [
    ["Name", "Age", "Job"],
    ["Rohit Samanta", 24, "Android Developer"],
    ["Agni Banerjee", 22, "Web Developer"],
    ["Gourabh Saha", 23, "Analyst"],
]

filePath = "./011 File Handling/output.csv"

try:
    with open(filePath, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

        print(f"CSV file '{filePath}' is created")
except:
    print()
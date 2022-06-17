# Loops in Pyhton

studentName = ["Shantanu", "Mayank", "Mohan", "Abhishek"]

for name in studentName:
    print(name)


studentMarks = [["Shantanu", 78],["Mayank", 50],["Mohan", 90],["Abhishek",60]]

for name,mark in studentMarks:
    print(name, mark)


dict1 = dict(studentMarks)
for key in dict1:
    print(dict1[key])

for key, value in dict1.items():
    if value < 90:
        print(f"Name: {key}, Mark: {value}")
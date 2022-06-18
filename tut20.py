# File IO Basic | Python

"""
r - Open file for reading - Default mode
w - Open a file for writing
x - Creates files if not exits
a - Add more content to a file
t - Text mode - Default mode
b - Binary mode 
+ - read and write
"""

f = open("faisal.txt","rt") # return file pointer
content = f.read(3)
# print(content) # fai

f.close()

# Read line by line
filePointer = open("faisal.txt")
# fileContent = filePointer.read()
for line in filePointer:
    # print(line)
    pass

filePointer.close()

# readline function
file1 = open("faisal.txt")
print(file1.readline()) # faisal is a good boy
filePointer.close()

# readlines function return list

fileToList = open("faisal.txt")
lst = fileToList.readlines()
print(lst) # ['faisal is a good boy\n', 'faisal is the king of this universe\n', 'faisal is very smart']
fileToList.close()
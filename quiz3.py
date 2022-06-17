from turtle import st


myList = ["dhaniya","adrak",40,"mirchi",1,7,"paneer",3, 8]

# Mine Solution 
for num in myList:
    if  type(num) == int:
        if num > 6:
            print(num, end=" ")



"""
OUTPUT: 40 7 8
"""

# Book Solution

for items in myList:
    if str(items).isnumeric() and items > 6:
        print(items)

"""
OUTPUT: 40 7 8
"""

# File Write in Python

"""
file = open("faisal.txt", "a") # "w" - write mode; "a" - append mode
a = file.write("faisal bhai bout aache hain\n")
print(a) # how many character it written

file.close()
"""
# Handle read and write both

file = open("faisal.txt","r+")
print(file.read())
file.write("thank you \n")
content = file.read()
print(content)
file.close()
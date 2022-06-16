# String Datatype and its functions

myStr = "Faisal is a good boy"

print(myStr[6]) # a
# myStr[including:exculding]
print(myStr[0:5])# Faisa

# Length
print(len(myStr)) #20

# print(myStr[78]) Error
print(myStr[0:78]) #Faisal is a good boy

print(myStr[0:5:2]) # Fia
print(myStr[0:5:3]) # Fs
print(myStr[0:12:4]) # Fas

# Negative Indexes

print(myStr[-4:-2])
print(myStr[::-1])

# Functions:
"""
1) .isalnum()
2) .isalpha()
3) .endswith("arg")
4) .count("arg")
5) .capatalise()
6) .find("args")
"""

print(myStr.count("o")) # 3
print(myStr.endswith("boy")) #True
print(myStr.find("is"))
print(myStr.replace("is","are")) #Faareal are a good boy

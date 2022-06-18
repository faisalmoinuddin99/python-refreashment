# Operators in Python

"""
1. Arithmetic Operator
2. Comparison Operator
3. Logical Operator
4. Identity Operator
5. Membership Operator
6. Bitwise Operator
"""
#Arithmetic Operator
print(5 + 6)
print(5 * 6)
print(15 / 6) # 2.5
print(5 % 6)
print(5 - 6)
print(15 // 6) # floor division (2.5) = 2
print(2**3) # power 2 * 2 * 2 = 8

# Assignment Operator
print("Assignment Operator")
x = 5 
print(x)

# Comparison Operator
print("Comparison Operator")
i = 8
print(i == 5) # False
print(i > 5) # True
print (i < 5) # False

# Logical Operator
print("Logical Operator")
a = True
b = False
print(a and b) # False
print(a or b) # True
print(a ^ b) # True

# Identity Operator
print("Identity Operator")
print(a is b) # False
print(a is not b) # True


# Membership Operator
print("Membership Operator")
lst = [3,3,2,39,67,24,12]
print(67 in lst) # True
print(67 not in lst) # False

# Bitwise Operator
print("Bitwise Operator")
"""
0 - 00
1 - 01
2 - 10
3 - 11
"""
print(0 & 1) # 0
print(1 | 3) # 3
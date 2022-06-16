# List in Python

grocery = ["harpic","vim bar","adark","lesoon","lollypop",56]

# print(grocery[5])

numbers = [2,7,9,3,11]
numbers.sort()
# numbers.reverse()
print(numbers)

print(numbers[::-1])
print(numbers[::2])

numbers.append(10)
print(numbers)

print(min(numbers)) #2
print(max(numbers)) # 11

numbers.insert(3,90)
print(numbers) # [2, 3, 7, 90, 9, 11, 10]
numbers.remove(90)
print(numbers) #[2, 3, 7, 9, 11, 10]
print(numbers.pop())  


# Tuple in Python

"""
A] Mutuable === List (Can change)
B] Immutuable === Tuple (Cannot change)
"""

tp = (1,2,4)
print(type(tp)) # <class 'tuple'>
print(tp)


# Swap two number

a = 10
b = 20

temp = a
a = b 
b = temp
print(a,b) # 20 10

x = 100
y = 200

x,y = y,x
print(x,y) # 200 100
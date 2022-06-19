# Question 1
lst = ["apple","mango"]
for i in lst:
    # print(lst.append(i.upper())) -- infinite loop
    print(lst.index(i))

# Question 2
x = 0
i = 0
while x<= 18:
    x += 3
    i += 1
    print(f"X: {x} and I:{i}")

# Question 3
a = max(False, -3, -4) 
b = min(a, 2, 7)
print(b) # False
print(f"{int(False)} and {int(True)}") # 0 and 1

# Question 4
def fun():
    x = 100
    return x

result = fun() + 1
print(result) # 101

#Question 5

a = 66
print('[%c]'%a) # Return the ASCII value B

x, y = 1, 2
x, y, z = 10, 20, 30
print(x,y,z)

#Question 6
b = 30
def fun2(a,b=b):
    return a+b
op = fun2(1)
print(f"Result of Question 6: {op}") # 31
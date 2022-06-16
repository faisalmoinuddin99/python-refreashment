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
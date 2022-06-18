# Recursions in Python

def fact(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3 ..... 1
    """
    if n == 1:
        return 1
    return n * fact(n-1)

for i in range(4):
    pass

print(i)


print(fact.__doc__)
userInput = int(input("Enter the number:"))
result = fact(userInput)
print(result)
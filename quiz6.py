# Program for Fibonacci numbers

def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)

userInput = int(input("Enter the number:"))
result = fib(userInput)
print(result)

"""
Enter the number:7
13
"""
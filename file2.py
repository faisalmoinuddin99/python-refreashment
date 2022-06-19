

def greetInFrench(name):
    return f"bonjour!! {name}"

def faultyAdd(num1, num2):
    return num1 + num2 + 5

print(f"and the name is: {__name__}")

if __name__ == '__main__':
    print(greetInFrench("faisal"))
    output = faultyAdd(5,4)
    print(output)


"""
and the name is: __main__
bonjour!! faisal
14
"""
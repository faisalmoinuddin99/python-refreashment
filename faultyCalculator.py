# Problem Statement
"""
Design a calculator which will correctly solve all the problems except the 
following ones:
45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4

Your program should take userOperator and the two numbers as input from user
and then return the result
"""
import operator

numberOne = int(input("Enter the first number:"))
numberTwo = int(input("Enter the second number:"))

userOperator = input("Choose the userOperators:")

ops = { 
    "+": operator.add,
    "-": operator.sub, 
    "/": operator.truediv,
    "*": operator.mul

} 

if userOperator == "*" and numberOne == 45 and numberTwo == 3:
    print(f"{numberOne} * {numberTwo} = 555")

elif userOperator == "+" and numberOne == 56 and numberTwo == 9:
     print(f"{numberOne} + {numberTwo} = 77")

elif userOperator == "/" and numberOne == 56 and numberTwo == 6:
     print(f"{numberOne} / {numberTwo} = 4")

elif userOperator == "+" and numberOne != 56 and numberTwo != 9:
     print(ops["+"](numberOne,numberTwo))
elif userOperator == "-":
    print(numberOne - numberTwo)
elif userOperator == "*" and numberOne != 45 and numberTwo != 3:
    print(ops["*"](numberOne, numberTwo))
elif userOperator == "/" and numberOne != 56 and numberTwo != 6:
    print(ops["/"](numberOne, numberTwo))
else:
    print("Wrong input")
    
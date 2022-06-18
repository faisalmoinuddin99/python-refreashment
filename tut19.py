# Exception Handling in Python


numberOne = int(input("Enter number 1:"))
numberTwo = int(input("Enter number 2:"))
try:
    print(numberOne / numberTwo)

except Exception as e:
    print(f"Not possible {e}")

print("This line is very important")

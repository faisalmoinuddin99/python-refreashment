# Take a input from user until the input is greater than 100


while True:
    userInput = int(input("Enter the number:"))
    if userInput < 100:
        print(userInput)
    else:
        print("User input is greater than 100, hence condition statisfied")
        break
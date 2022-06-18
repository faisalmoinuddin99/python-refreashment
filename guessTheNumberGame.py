# Guess the Number Game with CLI

guessedNumber = 20

while True:
    userChoice = int(input("Guess the Number: \n"))
    if userChoice < guessedNumber:
        print("oh! Increase the number")
        continue
    elif userChoice > guessedNumber:
        print("oops! Decrease the number")
        continue
    else:
        print("Congratulation!!! you are correct")
        break

"""
Guess the Number: 
30
oops! Decrease the number
Guess the Number:
25
oops! Decrease the number
Guess the Number:
22
oops! Decrease the number
Guess the Number:
10
oh! Increase the number
Guess the Number:
15
oh! Increase the number
Guess the Number:
16
oh! Increase the number
Guess the Number:
17
oh! Increase the number
Guess the Number:
19
oh! Increase the number
Guess the Number:
20
Congratulation!!! you are correct
"""
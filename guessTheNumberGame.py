# Guess the Number Game with CLI

"""
Additional feature:
No of guesses = 10
print no of guesses left
print you have taken n no of guesses
"""

guessedNumber = 20
life = 5

while True:
    userChoice = int(input("Guess the Number: \n"))
    if userChoice < guessedNumber:
        print("oh! Increase the number")
        life -= 1
        print(f"You have {life} life left")
        if life == 0:
            print("Game over")
            break
        continue
    elif userChoice > guessedNumber:
        print("oops! Decrease the number")
        life -= 1
        print(f"You have {life} life left")
        if life == 0:
            print("Game over")
            break
        continue
    else:
        print("Congratulation!!! you are correct")
        print(f"You have taken {life} guesses")
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


"""
Guess the Number: 
40
oops! Decrease the number
You have 4 life left
Guess the Number:
10
oh! Increase the number
You have 3 life left
Guess the Number:
30
oops! Decrease the number
You have 2 life left
Guess the Number:
45
oops! Decrease the number
You have 1 life left
Guess the Number:
10
oh! Increase the number
You have 0 life left
Game over
"""


"""
Guess the Number: 
21
You have 9 life left
Guess the Number:
30
oops! Decrease the number
You have 8 life left
Guess the Number:
20
Congratulation!!! you are correct
You have taken 8 guesses
"""
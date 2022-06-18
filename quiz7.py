import random

actors = ["snake","water","gun"]

computer = random.choice(actors)

while True:
    print("Pick your choice:")
    userInput = int(input("1. Snake\t 2. Water\t 3.Gun\n"))
    if computer == "snake" and userInput == 1:
        print("Tie")
        
    elif computer == "snake" and userInput == 2:
        print("user won")
       
    elif computer == "snake" and userInput == 3:
        print("user won")
       
    elif computer == "water" and userInput == 1:
        print("user won")
       
    elif computer == "water" and userInput == 2:
        print("tie")
       
    elif computer == "water" and userInput == 3:
        print("computer won")
      
    elif computer == "gun" and userInput == 1:
        print("computer won")
       
    elif computer == "gun" and userInput == 2:
        print("user won")
        
    elif computer == "gun" and userInput == 3:
        print("tie")
    
    print("Want to play agian:\n")
    want = int(input("1. Play \t 2. Exit"))
    if want == 2:
        break
    else:
        continue


print(f"computer took {computer}")
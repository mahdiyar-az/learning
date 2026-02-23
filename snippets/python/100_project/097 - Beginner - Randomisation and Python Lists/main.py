import random


print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
own_choice = random.choice(['paper', 'rock', 'scissors'])
print("computer chose " + own_choice)
if user_choice == 0:
    if own_choice == 0:
        print("draw")
    elif own_choice == 1:
        print("you lose")
    else:
        print("you win")

elif user_choice == 1:
    if own_choice == 1:
        print("draw")
    elif own_choice == 2:
        print("you lose")
    else:
        print("you win")
else:
    if own_choice == 2:
        print("draw")
    elif own_choice == 0:
        print("you lose")
    else:
        print("you win")

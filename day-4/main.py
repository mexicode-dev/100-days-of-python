from RPS_ASCII_Art import rock
from RPS_ASCII_Art import paper
from RPS_ASCII_Art import scissors

import random


player_choice = int(input("What do you choose? Type 0 for Rock, " \
"1 for Paper or 2 for Scissors.\n"))
if player_choice == 0:
    player_choice = rock
    print(rock)
elif player_choice == 1:
    player_choice = paper
    print(paper)
elif player_choice == 2:
    player_choice = scissors
    print(scissors)


print("Computer chose:\n")

choise_2 = [rock, paper, scissors]
computer_choice = random.choice(choise_2)
print(computer_choice)

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == rock and computer_choice == scissors:
    print("You win! Rock beats Scissors")

elif player_choice == scissors and computer_choice == paper:
    print("You win! Scissors beats Paper")

elif player_choice == paper and computer_choice == rock:
    print("You win! Paper beats Rock")
else:
    print("You lose!")
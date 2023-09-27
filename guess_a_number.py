import random
from colorama import Fore, Back, Style
computer_selection = random.randint(1, 100)

while True:
    player_selection = input("Guess a number between 1 - 100: ")
    if not player_selection.isdigit():
        print("Please select number between 1 - 100")
        continue

    else:
        player_selection = int(player_selection)
    if player_selection > computer_selection:
        print(Fore.RED + "Too high!")

    elif player_selection < computer_selection:
        print(Fore.GREEN + "Too low!")

    else:
        print(Fore.BLUE + "You guess it!")
        exit()
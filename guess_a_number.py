import random

computer_selection = random.randint(1, 100)

while True:
    player_selection = input("Guess a number between 1 - 100: ")
    if not player_selection.isdigit():
        print("Please select number between 1 - 100")
        continue

    else:
        player_selection = int(player_selection)
    if player_selection > computer_selection:
        print("Too high!")

    elif player_selection < computer_selection:
        print("Too low!")

    else:
        print("You guess it!")
        exit()
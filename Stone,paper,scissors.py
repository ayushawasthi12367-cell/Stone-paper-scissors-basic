import random

print("Welcome to the Rock, Paper, scissors game!\n")
print("Winning Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("\nEnter your choice: Rock, Paper, Scissors or Q to quit the game")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("Q - Quit")

    choice_input = input("Enter your choice: ")

    if choice_input.lower() == 'q':
        print("\nThanks for playing the game. Goodbye!")
        break

    try:
        choice = int(choice_input)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'Q' to quit.")
        continue

    while choice < 1 or choice > 3:
        choice = int(input("Please enter a valid choice (1-3): "))

    user_choice = choices[choice - 1]
    print("\nUser choice is:", user_choice)
    print("\nNow its computer turn....... please wait\n")

    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]

    print("Computer choice is:", computer_choice)
    print(user_choice, "V/S", computer_choice)

    if choice == comp_choice:
        print("<== GAME DRAW ==>")
    elif choice == 1 and comp_choice == 2:
        print("<== COMPUTER WINS ==>")
    elif choice == 1 and comp_choice == 3:
        print("<== USER WINS ==>")
    elif choice == 2 and comp_choice == 1:
        print("<== USER WINS ==>")
    elif choice == 2 and comp_choice == 3:
        print("<== COMPUTER WINS ==>")
    elif choice == 3 and comp_choice == 1:
        print("<== COMPUTER WINS ==>")
    elif choice == 3 and comp_choice == 2:
        print("<== USER WINS ==>")
    else:
        print("Invalid input! Please try again.")

    while True:
        ans = input("\nDo you want to play again? (Y/N): ").lower()
        if ans in ['y', 'n']:
            break
        print("Please enter 'Y' for Yes or 'N' for No.")

    if ans == 'n':
        print("\nThanks for playing the game. Goodbye!")
        break

    print()

    print("\nTHANK YOU FOR PLAYING THE GAME. GOODBYE!")


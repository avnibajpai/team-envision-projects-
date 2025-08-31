import random

# STORE COLORS
RESET = "\033[0m" #ANSI COLOUR CODES
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

def game():
    user = 0
    c = 0
    choice = random.randint(1, 100) # RANDOM NUMBER STORE

    print(CYAN + "🎮 Welcome to the Number Guessing Game!" + RESET)

    while user != choice:
        try:
            print(YELLOW + "Guess a number between 1 and 100" + RESET)
            user = int(input())  # input from player
            c += 1

            if user == choice:
                print(GREEN + "🎉 Yayy! You guessed it right!" + RESET)
                print(BLUE + "Number of attempts taken: " + str(c) + RESET)
                break

            diff = abs(user - choice)  # DISTANCE BETWEEN USER NUMBER AND COMP NUMBER

            if user > choice:
                if diff > 20:
                    print(RED + "Too High!" + RESET)
                elif diff > 10:
                    print(YELLOW + "High!" + RESET)
                else:
                    print(GREEN + "Very Close! But still high." + RESET)
            else:
                if diff > 20:
                    print(RED + "Too Low!" + RESET)
                elif diff > 10:
                    print(YELLOW + "Low!" + RESET)
                else:
                    print(GREEN + "Very Close! But still low." + RESET)

        except ValueError:
            print(RED + "Invalid input! Please enter a number only." + RESET)

    print(YELLOW + "Do you want to play again? (yes/no)" + RESET)
    again = input().lower()
    if again == "yes":
        game()

game()

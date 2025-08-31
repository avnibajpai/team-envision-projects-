import random

# STORE COLOURS
RESET = "\u001B[0m"  # PUT IT TO DEFAULT
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
CYAN = "\u001B[36m"

user_points = 0
comp_points = 0
user = ""
comp = ""


def menu():
    
    print("\n===============================")
    print(BLUE + "WELCOME TO ROCK PAPER SCISSORS" + RESET)
    print("===============================\n")
    print("1. Classic mode \n" + "2. Best of Five mode \n" + "3. Quit")  # ADDED TWO GAME MODES
    choice = input("Enter your choice(1-3): ")

    if choice == "1":
        instructions_classic()
    elif choice == "2":
        instructions_best_of_five()
    elif choice == "3":
        exit()
    else:
        print(RED + "invalid input,retry" + RESET) #ERROR HANDLING
        menu()


def instructions_classic():  # INSTRUCTIONS FOR CLASSIC
    print("\nYou selected Classic Mode!")
    print("---------------------------------------------------------")
    print("---INSTRUCTIONS(probably everyone knows them but still:/)---\n")
    print("# the game continues till the user exits\n")
    print(
        "AND yes the basics of all \n \n"
        + BLUE
        + "# ROCK beats SCISSORS \n"
        + "# SCISSORS beats PAPER \n"
        + "# PAPER beats ROCK "
        + RESET
    )
    print("---------------------------------------------------------")
    print("Press 1 to start and 0 to exit")

    start = input()
    if start == "1":
        print("Starting Classic Game....")
        play_classic()
    else:
        menu()


def instructions_best_of_five():  # INSTRUCTIONS FOR BEST OF FIVE
    print("\nYou selected Best of Five Mode!")
    print("---------------------------------------------------------")
    print("---INSTRUCTIONS(probably everyone knows them but still:/)---\n")
    print("# As the name suggests,first to reach five points wins\n")
    print(
        "AND yes the basics of all \n\n"
        + BLUE
        + "# ROCK beats SCISSORS \n"
        + "# SCISSORS beats PAPER \n"
        + "# PAPER beats ROCK "
        + RESET
    )
    print("---------------------------------------------------------")
    print("Press 1 to start and 0 to exit")

    start = input()
    if start == "1":
        print("Starting Best of Five Game....")
        play_best_of_five()
    else:
        menu()


def play_classic():  # CLASSIC GAME PLAY
    global user_points, comp_points, user, comp
    while True:
        user = get_user_choice()
        comp = get_computer_choice()

        if user == "exit":
            print("Exiting classic mode....")
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice.Try again" + RESET)
            continue

        print("-------------------------------")
        print("You chose: " + CYAN + user + RESET)
        print("Computer chose: " + CYAN + comp + RESET)
        decide(user, comp)
        print(BLUE + "Score -> You: " + str(user_points) + " | Computer: " + str(comp_points) + RESET)
        print("-------------------------------")

    print(BLUE + "Final Score -> You: " + str(user_points) + " | Computer: " + str(comp_points) + RESET)
    menu()


def play_best_of_five():  # BEST OF FIVE GAME PLAY
    global user_points, comp_points, user, comp
    user_points = 0
    comp_points = 0

    while user_points < 5 and comp_points < 5:
        user = get_user_choice()
        comp = get_computer_choice()

        if user == "exit":
            print("Exiting Best of five mode....")
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice.Try again")
            continue

        print("-------------------------------")
        print("You chose: " + CYAN + user + RESET)
        print("Computer chose: " + CYAN + comp + RESET)
        decide(user, comp)
        print(BLUE + "Score -> You: " + str(user_points) + " | Computer: " + str(comp_points) + RESET)
        print("-------------------------------")
        print(BLUE + "Final Score -> You: " + str(user_points) + " | Computer: " + str(comp_points) + RESET)
    menu()

    

    menu()


def get_user_choice():  # USER CHOICE
    global user
    user = input("Enter rock, paper, or scissors(or 'exit' to quit): ").strip().lower()
    return user


def get_computer_choice():
    choice = random.randint(0, 2)
    if choice == 0:
        return "rock"
    elif choice == 1:
        return "paper"
    else:
        return "scissors"


def decide(user, computer):
    global user_points, comp_points

    if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (
        user == "scissors" and computer == "paper"
    ):
        user_points += 1
        print(GREEN + "✨You win this round!✨" + RESET)
    elif user == computer:
        print(YELLOW + "Its a tie!😐" + RESET)
    else:
        comp_points += 1
        print(RED + "Computer wins this round!💻" + RESET)


if __name__ == "__main__":  # MAIN MENU
    menu()

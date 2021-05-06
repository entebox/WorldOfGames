# This function has a person name as an input and returns a string in the following layout:
def welcome():
    name = input("please enter your name: \n")
    print(f"\nHello, {name}, and welcome to the World of Games (WoG)\nHere you can find many cool games to play.\n")


# submenu difficulty option
def difficulty():
    while True:
        try:
            var_difficulty = int(input("Please choose game difficulty from 1 to 5: \n"))
        except ValueError:
            print("only numbers allowed\n")
            continue
        if var_difficulty not in range(1, 6):
            print("only numbers in the range allowed\n")
        else:
            return var_difficulty


# This function prints out the main menu to choose the game:
def load_game():
    while True:
        try:
            choice = int(input("Please choose a game to play:\n"
                               "1. Memory Game - a""sequence of numbers will appear for 1 second and you "
                               "have to guess it back\n" 
                               "2. Guess Game - guess a number and see if you chose like the computer\n"
                               "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                               "your choice: \n"))
        except ValueError:
            print("only numbers allowed\n")
            continue
        if choice not in range(1, 4):
            print("only numbers in the range allowed\n")
        else:
            return choice

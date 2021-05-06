from time import sleep
import random
import sys

"""generate_sequence - Will generate a list of random numbers between 1 to 101. The list
length will be difficulty"""


def generate_sequence(arg_diff):
    random_list = []
    for i in range(0, arg_diff):
        n = random.randint(1, 101)
        print(n)
        sleep(0.7)
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sleep(0.7)
        random_list.append(n)
    return random_list


"""get_list_from_user - Will return a list of numbers prompted from the user. The list length
will be in the size of difficulty"""


def get_list_from_user(arg_diff):
    user_list = []
    for i in range(0, arg_diff):
        while True:
            try:
                user_input_test = int(input("numbers showed on display: \n"))
            except ValueError:
                print("only numbers allowed")
                continue
            if user_input_test not in range(1, 101):
                print("only numbers between 0-101 are allowed")
            else:
                user_input = user_input_test
                user_list.append(user_input)
                break
    return user_list


"""is_list_equal - A function to compare two lists if they are equal. The function will return
True / False."""


def is_list_equal(gene_list, list_from_user):
    if gene_list == list_from_user:
        print("you win!\n")
    else:
        print("you lose!\n")


"""play - Will call the functions above and play the game. Will return True / False if the user
lost or won"""


def play(rec_difficulty):
    gene_sec = generate_sequence(rec_difficulty)
    user_list = get_list_from_user(rec_difficulty)
    is_list_equal(gene_sec, user_list)

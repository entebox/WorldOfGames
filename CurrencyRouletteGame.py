from forex_python.converter import CurrencyRates
from decimal import Decimal, ROUND_DOWN
import numpy as np
import random

c = CurrencyRates()

"""This game will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 and will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user’s difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer"""

"""get_money_interval -Will get the current currency rate from USD to ILS and will
generate an interval, for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
(5 - d))"""


def get_money_interval(arg_diff, rand_num):
    d = arg_diff
    conv = c.convert('USD', 'ILS', rand_num)
    t = Decimal(conv).quantize(Decimal('1'), rounding=ROUND_DOWN)
    if d == 5:
        interval = np.arange(t, t + 1)
    else:
        interval = np.arange((t - (5 - d)), (t + (5 - d)))
    return interval


"""get_guess_from_user - A method to prompt a guess from the user to enter a guess of
value to a given amount of USD"""


def get_guess_from_user(random_num):
    while True:
        try:
            guessed_value = int(input(f"what is the conversion of {random_num} USD to ILS nowadays?\n"))
        except ValueError:
            print("only numbers allowed\n")
            continue
        break
    return guessed_value


"""play - Will call the functions above and play the game. Will return True / False if the user
lost or won."""


def play(rec_difficulty):
    r = random.randint(1, 101)
    r = 1
    inter = get_money_interval(rec_difficulty, r)
    guess = get_guess_from_user(r)
    if guess in inter:
        print("you win!")
    else:
        print("you lose!")

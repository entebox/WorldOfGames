from Live import welcome, load_game, difficulty
from MemoryGame import play as play_memory
from GuessGame import play
from CurrencyRouletteGame import play as play_currencyRoullete
"""The purpose of this file is to call the functions from Live.py"""

welcome()
choice = load_game()
var_difficulty = difficulty()


if choice == 1:
    play_memory(var_difficulty)


if choice == 2:
    play(var_difficulty)


if choice == 3:
    play_currencyRoullete(var_difficulty)


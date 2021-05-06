import random


"""generate_number - Will generate number between 1 to difficulty and save it to
secret_number"""
def generate_number(arg_diff):
    secret_number = random.randint(1, arg_diff)
    return secret_number


"""get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
return the number."""
def get_guess_from_user(arg_diff):
    while True:
        try:
            guessed_num = int(input(f"guess a number between 1 to {arg_diff}\n"))
        except ValueError:
            print("only numbers allowed\n")
            continue
        if guessed_num not in range(0, (arg_diff+1)):
            print("only numbers in the range allowed\n")
        else:
            return guessed_num


"""compare_results - Will compare the the secret generated number to the one prompted
by the get_guess_from_user."""
def compare_results(gene_num, guess_from_user):
    if gene_num == guess_from_user:
        print("you win!\n")
    else:
        print("you lose!\n")


"""play - Will call the functions above and play the game. Will return True / False if the user
lost or won."""
def play(rec_difficulty):
    gene_var = generate_number(rec_difficulty)
    user_input = get_guess_from_user(rec_difficulty)
    compare_results(gene_var, user_input)

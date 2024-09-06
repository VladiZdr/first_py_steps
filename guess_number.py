from random import randint


def guess_number_game(x, y):
    number_to_guess = randint(x, y)

    user_input = number_to_guess + 1

    while user_input != number_to_guess:
        user_input = int(input("Make your guess:"))
        if user_input != number_to_guess:
            print("Wrong, make another guess")

    print("well played! you win!")

import os
from random import choice

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


def hangman_game():
    word_to_guess = choice(words)
    cnt = len(word_to_guess)

    lives = 5
    wrong_guesses = ""
    guess = ""
    for x in range(cnt):
        guess += "_"

    while guess != word_to_guess or lives == 0:
        clear_console()
        print("\nYou have {} lives left \nWrong guesses:".format(lives) + wrong_guesses + "\nWord: " + guess)
        curr = input("Make your guess: ")
        in_word = False

        i = 0
        for x in word_to_guess:
            if x == curr:
                in_word = True
                guess = guess[:i] + curr + guess[i + 1:]
            if guess[i] == "_":
                guess = guess[:i] + "_" + guess[i + 1:]
            i = i + 1

        if not in_word:
            wrong_guesses += " " + curr
            lives -= 1
            if lives == 0:
                print("Game Over, no more lives. The word was: " + word_to_guess)
                return 0

    print("You win!")


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

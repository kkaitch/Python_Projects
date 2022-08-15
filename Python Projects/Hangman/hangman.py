"""
File: hangman.py
Name: Kaiting
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program plays Hangman with certain times of chances to guess.
    """
    ans = random_word()
    lives = N_TURNS

    # Use an empty string to collect guessed letters
    guessed = ''

    intro(ans, lives)
    while True:
        guess = input('Your guess: ')

        # Wrong format of user input
        if not guess.isalpha() or len(guess) != 1:
            print('Illegal format.')

        else:
            guess = guess.upper()
            guessed += guess

            if guess in ans:
                print('You are correct!')
            else:
                print('There is no ' + guess + ' in the word.')
                lives -= 1

            current_word = pair_ans(guessed, ans)

            # Breakpoint 1: guess all the letters
            if ans == current_word:
                break

            # Breakpoint 2: no more lives to subtract
            if lives == 0:
                break

            print('The word looks like ' + current_word)
            print('You have ' + str(lives) + ' wrong guesses left.')

            # Show the hangman in console
            hangman(lives)

    ending(lives, ans)


def intro(ans, n):
    """
    :param ans: The word to count the length
    :param n: int, initial lives to guess
    """
    dashes = ''
    for i in range(len(ans)):
        dashes += '-'
    print('--------')
    print('|      |')
    print('|')
    print('|')
    print('|')
    print('|')
    print('The word looks like ' + dashes)
    print('You have ' + str(n) + ' wrong guesses left.')


def pair_ans(guesses, ans):
    """
    The function demos how the current word looks like.
    :param guesses: The letters that have been guessed
    :param ans: The word to compare with
    :return current_word: The current look of the word
    """
    current_word = ''
    for ch in ans:
        if guesses.find(ch) != -1:
            current_word += ch
        else:
            current_word += '-'
    return current_word


def hangman(n):
    """
    The function displays the hangman in the console.
    : param n: int, the lives left to subtract
    """
    if n == 7:
        print('--------')
        print('|      |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('')
    elif n == 6:
        print('--------')
        print('|      |')
        print('|      ○')
        print('|')
        print('|')
        print('|')
        print('')
    elif n == 5:
        print('--------')
        print('|      |')
        print('|      ○')
        print('|      |')
        print('|')
        print('|')
        print('')
    elif n == 4:
        print('--------')
        print('|      |')
        print('|      ○')
        print('|    / |')
        print('|')
        print('|')
        print('')
    elif n == 3:
        print('--------')
        print('|      |')
        print('|      ○')
        print('|    / | \\')
        print('|')
        print('|')
        print('')
    elif n == 2:
        print('--------')
        print('|      |')
        print('|      ○')
        print('|    / | \\')
        print('|     /')
        print('|')
        print('')
    elif n == 1:
        print('--------')
        print('|      |')
        print('|      ○')
        print('|    / | \\')
        print('|     / \\')
        print('|')
        print('')


def ending(n, ans):
    """
    Display the final hangman at the end.
    : param n: int, the lives left in the end
    : param ans: str, shows the answer
    """
    if n != 0:
        print('You win!!')
        print('--------')
        print('|      |    / Yeah!')
        print('|   ๑̵´ ᴗ｀๑  ︎\\ ᵗᑋᵃᐢᵏ ᵞᵒᵘ')
        print('|    ٩ | ۶')
        print('|    ノ  ヽ')
        print('|')
        print('')
    else:
        print('You are completely hung :(')
        print('--------')
        print('|      |')
        print('|     x.x︎')
        print('|    / | \\')
        print('|     | |')
        print('|')
        print('')
    print(f'The word was: {ans}')


def random_word():
    """
    :return: A random word as the answer
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()

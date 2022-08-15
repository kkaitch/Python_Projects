"""
File: anagram.py
Name: Kaiting
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program finds the anagrams for the input word.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        search_word = input('Find anagrams for: ')
        if search_word == EXIT:
            break

        # Start recursion and find anagrams
        start = time.time()

        anagram_lst = find_anagrams(search_word)
        print(f'{len(anagram_lst)} anagrams: {anagram_lst}')

        # Stop the timer
        end = time.time()

    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    This function reads the dictionary file and adds the words to a new list.
    :param s: s, the user input to decide which word to add
    :return: set, stores the same sorted words from the dictionary file
    """
    words_set = set()
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()

            # Filter words with the same length and with char inside
            if len(word) == len(s) and word[0] in s:

                # Sort the word to find anagram and add to the words set
                if sorted(word) == sorted(s):
                    words_set.add(word)

    return words_set


def find_anagrams(s):
    """
    This function reads the dictionary file and uses helper to find anagrams.
    :param s: str, the word to find anagrams
    :return: lst, contains all anagrams
    """
    print('Searching...')
    anagram_lst = []
    words = read_dictionary(s)
    find_anagrams_helper(words, anagram_lst)
    return anagram_lst


def find_anagrams_helper(dictionary, anagram_lst):
    """
    The helper runs recursion until both the lengths are the same to find all anagrams.
    :param dictionary: set, the sorted words from the dictionary
    # :param idx_lst: lst, stores the index of the anagram_lst
    :param anagram_lst: lst, keeps all the anagrams
    :return:
    """
    if len(anagram_lst) == len(dictionary):
        pass

    else:

        # Loop over the words from the dictionary
        for word in dictionary:
            if word not in anagram_lst:

                # Add new anagram to the list
                anagram_lst.append(word)
                print(f'Found: {word}')
                print('Searching...')

                # Recursive call
                find_anagrams_helper(dictionary, anagram_lst)


if __name__ == '__main__':
    main()

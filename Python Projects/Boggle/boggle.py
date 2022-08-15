"""
File: boggle.py
Name: Kaiting
----------------------------------------
The program asks user to enter four rows of alphabets and plays Boggle.
Any letter can be used only once in one turn, and the consecutive letters
must be adjacent to each other horizontally, vertically, or even diagonally.
It will also calculate the total number of words found.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	The program asks for user input to find all the words in Boggle.
	"""
	while True:

		# Ask for inputs and check formats
		letter_lst, illegal = get_letters()
		if illegal:
			break

		start = time.time()

		####################
		words_set = find_words(letter_lst)
		print(f'There are {len(words_set)} words in total.')
		####################

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')
		break


def get_letters():
	"""
	This function gets four rows of alphabets from the user.
	:return: lst, stores 16 alphabets into 4 elements
	:return: bool, illegal switch to detect the viability of inputs
	"""
	illegal = False
	letters_lst = []

	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		row = row.lower()
		letters = row.split()

		# Check if the input is in a correct format
		if check_words(letters) is False:
			illegal = True
			break

		letters_lst.append(letters)

	return letters_lst, illegal


def check_words(letters):
	"""
	This function checks if the user input follows the rule.
	:param letters: lst, stores one row of letters from the input
	:return: bool, shows if it is legit
	"""
	# Check the length in one row only contains 4 elements
	if len(letters) != 4:
		print('Illegal input')
		return False

	# Check if the letters are alphabet letters and each element only contains one letter
	for letter in letters:
		if not letter.isalpha() or len(letter) != 1:
			print('Illegal input')
			return False
	return True


def read_dictionary(letters):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:param letters: str, the input alphabets
	:return: set, a set of possible words from the dictionary
	"""
	dictionary_set = set()
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()

			if len(word) >= 4 and word[0] in letters:
				dictionary_set.add(word)

	return dictionary_set


def convert(letters):
	"""
	Convert the letters to a str to filter words from the dictionary.
	:param letters: lst, stores 16 alphabets in a nested list
	:return: str, concatenate alphabets appeared in the letters lst
	"""
	s = ''

	# Flatten the nested list
	for letter in letters:
		row = ''.join(letter)

		# String manipulation
		for ch in row:

			# Remove duplicate
			if ch not in s:
				s += ch

	return s


def find_words(letters):
	"""
	This function reads the dictionary file and uses helper to play Boggle.
	:param letters: lst, stores 16 alphabets from the user into 4 elements accordingly
	:return: set, a set of words found in the Boggle
	"""
	# Convert the input to a str to read dictionary
	letters_in_str = convert(letters)
	dictionary_set = read_dictionary(letters_in_str)

	words_set = set()

	# Use a nested for loop to run through every letter on a 4x4 square grid
	for x in range(len(letters)):
		for y in range(len(letters[0])):
			s = letters[x][y]
			path = [(x, y)]
			boggle_helper(letters, dictionary_set, s, words_set, path, (x, y))

	return words_set


def boggle_helper(letters, dictionary, current_s, words_set, path, cur_position):
	"""
	The helper finds the words by searching its neighboring letters using recursion.
	:param letters: lst, a nested list stored the letters on a 4x4 square grid
	:param dictionary: set, a set of possible words from the dictionary
	:param current_s: str, stores the current word
	:param words_set: set, a set of words found in the Boggle game
	:param path: lst of tuple, stores the positions that been taken
	:param cur_position: tuple, stores the current position
	"""
	cur_x, cur_y = cur_position
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):

			# Move to the next position
			next_x = cur_x + i
			next_y = cur_y + j

			# Check if next_x and next_y are valid
			if 0 <= next_x < 4 and 0 <= next_y < 4 and (next_x, next_y) not in path:

				# Choose
				current_s += letters[next_x][next_y]
				path.append((next_x, next_y))

				# Explore
				# Check if current s can be found in the dictionary
				if has_prefix(current_s, dictionary):

					# Check if current s matches the word from the dictionary and is not found yet
					if len(current_s) >= 4 and current_s in dictionary and current_s not in words_set:
						words_set.add(current_s)
						print(f'Found "{current_s}"')

					# Recursive call where current position has been moved to (next_x, next_y)
					boggle_helper(letters, dictionary, current_s, words_set, path, (next_x, next_y))

				# Un-choose
				current_s = current_s[:len(current_s)-1]
				path.pop()


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: set, the imported and filtered dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.find(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

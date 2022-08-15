"""
File: weather_master.py
Name: Kaiting
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	The program determines the highest and the lowest temperatures, the average
	and the count of the cold days among inputs.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	temp = int(input('Next Temperature: (or -100 to quit)? '))
	if temp == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = temp
		minimum = temp
		cold_day = 0
		total = temp
		i = 1						# Set a variable to count the inputs
		if temp < 16:
			cold_day += 1
		while True:
			temp = int(input('Next Temperature: (or -100 to quit)? '))
			if temp == EXIT:
				break
			if temp > maximum:
				maximum = temp 		# Reassign maximum if the new temperature is higher
			if temp < minimum:
				minimum = temp 		# Reassign maximum if the new temperature is lower
			if temp < 16:
				cold_day += 1		# Cold day if temperature is lower than 16 degrees c
			total += temp
			i += 1
		average = total / i
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold_day) + ' cold day(s)')


if __name__ == "__main__":
	main()

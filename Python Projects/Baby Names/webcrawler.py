"""
File: webcrawler.py
Name: Kaiting
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    # for year in ['2010s']:
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find('tbody').find_all('tr')

        male_sum = 0
        female_sum = 0

        for tag in tags:

            # Get the male data as a str
            male_number = tag.text.split()[2].replace(',', '')

            # Check if male_number only contains digits
            if male_number.isdigit():
                male_sum += int(male_number)

            # Get the female data as a str
            female_number = tag.text.split()[4].replace(',', '')

            # Check if female_number only contains digits
            if female_number.isdigit():
                female_sum += int(female_number)

        print(f'Male number: {male_sum}')
        print(f'Female number: {female_sum}')


if __name__ == '__main__':
    main()

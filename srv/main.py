"""
The purpose of this program is to find all apartments in a specified radius of a specific climbing gym.

NEEDED API's:
- Google Maps (Distance Matrix) | https://developers.google.com/maps/documentation/distance-matrix/start
- Aparments.com | https://api.apartments.com/v1/
"""

import requests
import os
from dotenv import load_dotenv
from apartments import *
from distance_matrix import *

load_dotenv()
DISTANCE_MATRIX_KEY = os.getenv('DISTANCE_MATRIX_KEY')

def gather_inputs():
    city_state = input("Please enter the city and state you're wanting to find apartments in (eg. Des Moines, IA): ")
    s = city_state.split(', ')
    city = s[0]
    state = s[1]

    if city == '' or state == '' or len(state) > 2 or len(state) < 2:
        print("You didn't enter the city and state in the correct format. Try again.")
        gather_inputs()

    gym_address = input("Please enter the gym address you're wanting to calculate the apartment distance from: ")

    return city, state, gym_address

def main(city, state, gym_address):
    apartments = []
    page_count = 1
    apartment_count = 0

    print(f'Fetching apartments for {city}, {state}...')
    html = query_apartments(city, state)
    apartments, total_pages = parse_apartments(html, apartments)
    print(f'Page 1 of {total_pages} fetched! ({len(apartments) - apartment_count} added)')
    apartment_count = len(apartments)
    page_count += 1
    
    while page_count <= total_pages:
        apartments, _ = parse_apartments(query_apartments(city, state, page_count), apartments)
        print(f'Page {page_count} of {total_pages} fetched! ({len(apartments) - apartment_count} added)')
        apartment_count = len(apartments)
        page_count += 1

    print('All apartments fetched.')

    print(f'Calculating each apartments distance from specified gym address ({gym_address})...')
    rsp = distance_matrix(apartments[:10], gym_address, DISTANCE_MATRIX_KEY)
    print(f'Successfully used distance matrix api. \nResponse: {rsp}')

if __name__ == '__main__':
    # city, state, gym_address = gather_inputs()
    main('Des Moines', 'IA', '150 East 4th Street, Des Moines, IA 50309')
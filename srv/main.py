"""
The purpose of this program is to provide a csv of all apartments in a city, state, 
and order them from least to greatest distance from a specified location.

NEEDED API's:
- Google Maps (Distance Matrix) | https://developers.google.com/maps/documentation/distance-matrix/start
- Aparments.com | https://api.apartments.com/v1/
"""

import requests
import os
import math
import csv
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

    # Climb Iowa: East Village address -> '150 East 4th Street, Des Moines, IA 50309'
    destination_address = input("Please enter the gym address you're wanting to calculate the apartment distance from: ")

    return city, state, destination_address

def main(city, state, destination_address):
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

    print(f'All apartments fetched. (Total: {len(apartments)})')

    print(f'Calculating each apartments distance from specified destination address ({destination_address})...')
    batches = math.floor(len(apartments) / 25) # NOTE: 25 is used because that's the max amount of origin's we can do per request

    for i in range(batches+1):
        batch_amount = 25 # NOTE: 25 is used for the same reason as above

        apartments_batch = apartments[batch_amount * i: batch_amount * (i+1)]
        apartments_batch = distance_matrix(apartments_batch, destination_address, DISTANCE_MATRIX_KEY)
        apartments[batch_amount * i: batch_amount * (i+1)] = apartments_batch
        print(f'Batch {i+1} of {batches+1} calculated!')

    apartments_sorted = sorted(apartments, key=lambda obj: float(obj['distance'].split(' ')[0]))
    with open('./result.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, apartments_sorted[0].keys())
        writer.writeheader()
        writer.writerows(apartments_sorted)

if __name__ == '__main__':
    city, state, destination_address = gather_inputs()
    main(city, state, destination_address)
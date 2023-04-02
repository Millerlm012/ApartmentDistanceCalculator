"""
The purpose of this program is to find all apartments in a specified radius of a specific climbing gym.

NEEDED API's:
- Google Maps (Distance Matrix) | https://developers.google.com/maps/documentation/distance-matrix/start
- Aparments.com | https://api.apartments.com/v1/
"""

import requests
from apartments import *
from distance_matrix import *


def main(city, state):
    apartments = []
    print('Fetching apartments...')
    html = query_apartments(city, state)


def gather_inputs():
    city_state = input("Please enter the city and state you're wanting to find apartments in (eg. Des Moines, IA): ")
    s = city_state.split(', ')
    city = s[0]
    state = s[1]

    if city == '' or state == '' or len(state) > 2 or len(state) < 2:
        print("You didn't enter the city and state in the correct format. Try again.")
        gather_inputs()

    return city, state

if __name__ == '__main__':
    city, state = gather_inputs()
    main(city, state)
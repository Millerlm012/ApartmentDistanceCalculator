"""
apartments.py is used for querying https://apartments.com for apartments in a specfied city, state. 
We're then able to parse the results and calculate the distance from a specified climbing gym.
"""

import requests
from bs4 import BeautifulSoup

def query_apartments(city, state, page=1):
    assert len(state) == 2, 'Please enter state abbreviation instead of the full state.'

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    url = f"https://www.apartments.com/{city.replace(' ', '-').lower()}-{state.lower()}/{page}/"
    req = requests.get(url, headers=headers)
    return req.text

def parse_apartments(html):
    soup = BeautifulSoup(html, 'html.parser')
    total_pages = int(soup.find(class_='searchResults').text.split('Page')[1][1:-1].split(' of ')[1])

    apt_results = soup.find_all(class_='placard-header')
    for result in apt_results:
        apt = {}
        apt['name'] = result.find(class_='property-title').text
        apt['address'] = result.find(class_='property-address').text
        apt['url'] = result.find('a', {'class': 'property-link'}).attrs['href']
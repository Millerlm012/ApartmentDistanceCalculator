import requests
from bs4 import BeautifulSoup

def query_apartments(city, state, page=1):
    assert len(state) == 2, 'Please enter state abbreviation instead of the full state.'

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    url = f"https://www.apartments.com/{city.replace(' ', '-').lower()}-{state.lower()}/{page}/"
    req = requests.get(url, headers=headers)
    return req.text

def parse_apartments(html):
    ...
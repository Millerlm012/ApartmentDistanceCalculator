import requests

def query_apartments(city, state):
    headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    req = requests.get(f'https://www.apartments.com/{city}-{state}/')


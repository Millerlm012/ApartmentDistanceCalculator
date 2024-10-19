"""
apartments.py is used for querying https://apartments.com for apartments in a specfied city, state.
We're then able to parse the results and calculate the distance from a specified climbing gym.
"""

import requests
from bs4 import BeautifulSoup


def query_apartments(city, state, page=1):
    assert len(state) == 2, "Please enter state abbreviation instead of the full state."

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
    }
    url = f"https://www.apartments.com/{city.replace(' ', '-').lower()}-{state.lower()}/{page}/"
    req = requests.get(url, headers=headers, timeout=5)
    assert req.status_code == 200, f"Failed to fetch {url}"

    return req.text


def parse_apartments(html, apartments):
    soup = BeautifulSoup(html, "html.parser")
    total_pages = int(
        soup.find(class_="searchResults").text.split("Page")[1][1:-1].split(" of ")[1]
    )

    # collecting apartment info if displayed via placard-header
    header_results = soup.find_all(class_="placard-header")
    for result in header_results:
        apt = {}
        apt["name"] = result.find(class_="property-title").text
        apt["address"] = result.find(class_="property-address").text
        apt["url"] = result.find("a", {"class": "property-link"}).attrs["href"]
        apartments.append(apt)

    # collecting any missing apartments that didn't have the placard-header
    wrapper_results = soup.find_all(class_="property-title-wrapper")
    for result in wrapper_results:
        try:
            apt = {}
            apt["name"] = result.find(class_="property-title").text
            address_el = result.find(class_="property-address")
            if address_el:
                apt["address"] = address_el["title"]
            else:
                apt["address"] = apt["name"]
            apt["url"] = result.find("a", {"class": "property-link"}).attrs["href"]
            apartments.append(apt)
        except Exception as e:
            print(f"failed to parse html element {wrapper_results}: {e}")
            continue

    return apartments, total_pages

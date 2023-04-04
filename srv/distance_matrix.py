import requests
import json

def add_distance_to_apartments(apartments, distance_rsp):
    rows = distance_rsp["rows"]
    for i, row in enumerate(rows):
        apartments[i]['distance_api_status'] = row['elements'][0]['status']
        apartments[i]['distance'] = row['elements'][0]['distance']['text']
        apartments[i]['drive_duration'] = row['elements'][0]['duration']['text']

    return apartments

def distance_matrix(apartments, destination_address, key):
    # NOTE: you can only pass a max of 25 origins
    origins = ""
    for apart in apartments:
        origins += apart.get("address") + "|"
    origins = origins[:-1]
    
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destination_address}&key={key}&units=imperial"
    rsp = requests.get(url)
    assert rsp.status_code == 200, f'Uff da, we did NOT get a successful request from google apis. \nError: {rsp.text}'

    return add_distance_to_apartments(apartments, rsp.json())
import requests
import json

def distance_matrix(apartments, gym_address, key):
    origins = ""
    for apart in apartments:
        origins += apart.get("address") + "|"
    origins = origins[:-1]
    
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={gym_address}&key={key}"
    response = requests.get(url)
    assert response.status_code == 200, f'Uff da, we did NOT get a successful request from google apis. \nError: {response.text}'

    return response.text

def add_distance_to_apartments(apartments, distance_response):
    matrix = json.loads(distance_response)
    rows = matrix["rows"]
    index = 0
    for entry in aparments:
        entry["dist"] = rows[0].get("elements")

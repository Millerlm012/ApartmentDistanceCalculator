import requests
import json

def distance_matrix(apartments, gym_address, key):
    origins = ""
    for apart in apartments:
        origins += apart.get("address") + "|"
    origns = origns[:-1]
    
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={gym_address}&key={key}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def add_distance_to_apartments(apartments, distance_response):
    matrix = json.loads(distance_response)
    rows = matrix["rows"]
    index = 0
    for entry in aparments:
        ## TODO: LANDON FIX, IDK if this is getting teh distance or not
        entry["dist"] = ((rows[0]).get("elements")[0]).get("distance")


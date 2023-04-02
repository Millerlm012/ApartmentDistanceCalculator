import requests

def distance_matrix(apartments, gym_address, key):
    origins = ""
    for apart in apartments:
        origins += apart.get("address") + "|"
    origns = origns[:-1]
    
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={gym}&key={key}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
import requests


def add_distance_to_apartments(apartments, distance_rsp):
    rows = distance_rsp["rows"]
    for i, row in enumerate(rows):
        apartments[i]["distance_api_status"] = row["elements"][0]["status"]
        apartments[i]["distance"] = row["elements"][0]["distance"]["text"]
        apartments[i]["drive_duration"] = row["elements"][0]["duration"]["text"]

    return apartments


def distance_matrix(apartments, destination_address, key):
    # NOTE: you can only pass a max of 25 origins
    origins = ""
    for apart in apartments:
        origins += apart.get("address").replace("#", "") + "|"
    origins = origins[:-1]

    destination_address = destination_address.replace("#", "")
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={destination_address}&origins={origins}&units=imperial&key={key}"
    rsp = requests.get(url)
    data = rsp.json()
    assert (
        rsp.status_code == 200 and data["status"] != "REQUEST_DENIED"
    ), f"Uff da, we did NOT get a successful request from google apis. \nError: {rsp.text}"

    return add_distance_to_apartments(apartments, data)

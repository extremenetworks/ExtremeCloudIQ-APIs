import json
import getpass
import requests

URL = "https://api.extremecloudiq.com"

print("Enter your XIQ login credentials")
username = input("Email: ")
password = getpass.getpass("Password: ")


headers = {"Accept": "application/json", "Content-Type": "application/json"}

print("Make sure the csv file is in the same folder as the python script.")
filename = input("Please enter csv filename: ")


# get access token
def GetaccessToken(username, password):
    url = URL + "/login"
    payload = json.dumps({"username": username, "password": password})
    response = requests.post(url, headers=headers, data=payload)
    if response is None:
        print("ERROR: Not able to login into ExtremeCloudIQ - no response!")
        return -1
    if response.status_code != 200:
        print(f"Error creating building in XIQ - HTTP Status Code: {str(response.status_code)}")
        raise TypeError(response)
    data = response.json()

    if "access_token" in data:
        print("Logged in and Got access token: " + data["access_token"])
        headers["Authorization"] = "Bearer " + data["access_token"]
        return 0

    else:
        raise TypeError("Unknown Error: Unable to gain access token")

def CreateBuilding(payload):
    #print("Trying to create the new  Building")
    url = URL + "/locations/building"
    response = requests.post(url, headers=headers, data=payload, verify=True)
    if response is None:
        raise TypeError("Error creating building in XIQ - no response!")
    if response.status_code != 200:
        print(f"Error creating building in XIQ - HTTP Status Code: {str(response.status_code)}")
        raise TypeError(response)
    buildingid1 = response.json().get("id")
    return buildingid1
    #print(response)

def CreateFloor(payload):
    # print("trying to create floor")
    url = URL + "/locations/floor"
    response = requests.post(url, headers=headers, data=payload, verify=True)
    if response is None:
        raise TypeError("Error creating building in XIQ - no response!")
    if response.status_code != 200:
        print(f"Error creating building in XIQ - HTTP Status Code: {str(response.status_code)}")
        raise TypeError(response)
    #return response


def csv(filename):
    import csv

    with open(filename, "r",encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=",")
        # remove header line from CSV
        loc_params = next(reader)
        # Build list of location dictionaries
        new_locs = []
        for row in reader:
            #location dictionary
            data={}
            for x in range(len(loc_params)):
                # for each location parameters add key and value to dictionary
                data[loc_params[x]]=str(row[x])
            new_locs.append(data)
        return new_locs

# MAIN
try:
    login = GetaccessToken(username, password)
except TypeError as e:
    print(e)
    raise SystemExit
except:
    print("Unknown Error: Failed to generate token")
    raise SystemExit

loc_id2 = csv(filename)

for loc in loc_id2:
    # Create Building
    building_payload = json.dumps(
        {"parent_id": loc['location_id'],
         "name": loc['building_name'],
         "address": loc['address']}
    )
    #print(building_payload)

    try:
        build_id = CreateBuilding(building_payload)
    except TypeError as e:
        print(e)
        raise SystemExit
    except:
        print("Unknown Error: Failed to creating building")
        raise SystemExit


    floor_payload = json.dumps(
        {
            "parent_id": build_id,
            "name": loc['floor_name'],
            "environment": loc["environment"],
            "db_attenuation": loc['attenuation'],
            "measurement_unit": loc['measurement'],
            "installation_height": loc['height'],
            "map_size_width": loc['map_width'],
            "map_size_height": loc['map_height'],
            "map_name": loc['map_name'],
        }
    )
    #print(floor_payload)

    try:
        location_id = CreateFloor(floor_payload)
    except TypeError as e:
        print(e)
        raise SystemExit
    except:
        print("Unknown Error: Failed to creating floor")
        raise SystemExit
    print(f"Successfully added building {loc['building_name']} and floor {loc['floor_name']}")


    
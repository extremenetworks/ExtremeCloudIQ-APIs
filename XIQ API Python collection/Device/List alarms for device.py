import requests

device_id = 0
myStartTime = "" # epoch time in milliseconds
myEndTime = ""  # epoch time in milliseconds
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/alarms?startTime={myStartTime}&endTime={myEndTime}&page=1&limit=10"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

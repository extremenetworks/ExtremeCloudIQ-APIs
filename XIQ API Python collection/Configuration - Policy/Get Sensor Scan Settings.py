import requests

sensor_scan_id = 0 # The sensor scan settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/sensor-scan/{sensor_scan_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

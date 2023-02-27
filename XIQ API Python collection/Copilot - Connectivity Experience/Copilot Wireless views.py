import requests

view_type = 'SSID' # The type of View Available values : SSID, OS
access_token = '***'

url = f"https://api.extremecloudiq.com/copilot/connectivity/wireless/views?viewType={view_type}"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

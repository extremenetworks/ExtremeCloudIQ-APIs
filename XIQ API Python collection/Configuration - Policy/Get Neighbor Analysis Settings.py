import requests

neigh_analysis_id = 0 # The neighborhood analysis settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/neighborhood-analysis/{neigh_analysis_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

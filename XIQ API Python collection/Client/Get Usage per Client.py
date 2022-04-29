import requests

client_id = 0
myStartTime = "" # epoch time in milliseconds
myEndTime = ""  # epoch time in milliseconds
access_token = '***'

url = f"https://api.extremecloudiq.com/clients/usage?clientIds={client_id}&startTime={myStartTime}&endTime={myEndTime}"

payload = ""
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

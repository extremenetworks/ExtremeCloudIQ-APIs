import requests

app_id = 0
count = 10
myStartTime = "" # epoch time in milliseconds
myEndTime = ""  # epoch time in milliseconds

access_token = '***'

url = f"https://api.extremecloudiq.com/applications/{app_id}/clients/top{count}?startTime={myStartTime}&endTime={myEndTime}"

payload = ""
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

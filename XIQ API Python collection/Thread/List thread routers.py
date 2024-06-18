import requests

thread_router_ids = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/thread/routers?page=1&limit=10&ids={thread_router_ids}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

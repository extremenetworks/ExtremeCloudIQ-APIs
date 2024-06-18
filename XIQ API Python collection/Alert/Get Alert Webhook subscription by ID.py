import requests

webhook_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-subscriptions/webhooks/{str(webhook_id)}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import requests
import json

url = "https://api.extremecloudiq.com/ssids/usergroups/{{group_id}}"

payload = json.dumps({
  "name": "TheUserGroupName",
  "description": "AShortDescription",
  "password_settings": {
    "psk_generation_method": "PSK_GENERATION_METHOD_PASSWORD_ONLY"
  },
  "delivery_settings": {
    "email_template_id": "52004",
    "sms_template_id": "53005"
  }
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

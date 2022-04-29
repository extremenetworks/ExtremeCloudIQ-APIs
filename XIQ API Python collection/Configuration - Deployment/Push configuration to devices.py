import requests

access_token = '***'

url = "https://api.extremecloudiq.com/devices/config/"

payload="{\"devices\":{\"ids\":[***]},\"deploy_policy\":{\"enable_complete_configuration_update\":true,\"firmware_upgrade_policy\":{\"enable_enforce_upgrade\":true,\"enable_distributed_upgrade\":true},\"firmware_activate_option\":{\"enable_activate_at_next_reboot\":true,\"activation_delay_seconds\":0,\"activation_time\":0}}}"
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

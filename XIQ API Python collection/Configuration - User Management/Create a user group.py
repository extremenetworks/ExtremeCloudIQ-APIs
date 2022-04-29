import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/usergroups"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "password_db_location": "CLOUD",
  "ppsk_use_only": True,
  "password_type": "PPSK",
  "enable_max_clients_per_ppsk": True,
  "max_clients_per_ppsk": 0,
  "pcg_use_only": True,
  "pcg_type": "AP_BASED",
  "enable_cwp_reg": True,
  "password_settings": {
    "enable_letters": True,
    "enable_numbers": True,
    "enable_special_characters": True,
    "password_concat_string": "string",
    "psk_generation_method": "PASSWORD_ONLY",
    "password_character_types": "INCLUDE_ALL_CHARACTER_TYPE_ENABLED",
    "password_length": 8
  },
  "expiration_settings": {
    "expiration_type": "NEVER_EXPIRE",
    "valid_during_dates": {
      "start_date_time": {
        "day_of_month": 0,
        "month": 0,
        "year": 0,
        "hour_of_day": 0,
        "minute_of_hour": 0
      },
      "end_date_time": {
        "day_of_month": 0,
        "month": 0,
        "year": 0,
        "hour_of_day": 0,
        "minute_of_hour": 0
      },
      "time_zone": "string"
    },
    "valid_for_time_period": {
      "valid_time_period_after": "ID_CREATION",
      "after_id_creation_settings": {
        "valid_time_period": 0,
        "valid_time_period_unit": "MINUTE"
      },
      "after_first_login_settings": {
        "valid_time_period": 0,
        "valid_time_period_unit": "MINUTE",
        "first_login_within": 0,
        "first_login_within_unit": "MINUTE"
      }
    },
    "valid_daily": {
      "daily_start_hour": 0,
      "daily_start_minute": 0,
      "daily_end_hour": 0,
      "daily_end_minute": 0
    },
    "expiration_action": "SHOW_MESSAGE",
    "post_expiration_action": {
      "enable_credentials_renewal": True,
      "enable_delete_immediately": True,
      "delete_after_value": 0,
      "delete_after_unit": "MINUTE"
    }
  },
  "delivery_settings": {
    "email_template_id": 0,
    "sms_template_id": 0
  }
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

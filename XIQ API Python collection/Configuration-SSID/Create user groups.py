import requests
import json

url = "https://api.extremecloudiq.com/ssids/usergroups"

payload = json.dumps({
  "name": "TheUserGroupName",
  "description": "AShortDescription",
  "password_db_location": "PASSWORD_DB_LOCATION_CLOUD",
  "password_type": "PASSWORD_TYPE_PPSK",
  "enable_max_clients_per_ppsk": "false",
  "max_clients_per_ppsk": "0",
  "pcg_use_only": "false",
  "pcg_type": "PCG_TYPE_AP_BASED",
  "ppsk_use_only": "false",
  "enable_cwp_reg": "false",
  "password_settings": {
    "enable_letters": "true",
    "enable_numbers": "false",
    "enable_special_characters": "false",
    "password_character_types": "PASSWORD_CHARACTER_TYPE_INCLUDE_ALL_CHARACTER_TYPE_ENABLED",
    "psk_generation_method": "PSK_GENERATION_METHOD_USER_STRING_PASSWORD",
    "password_concat_string": "",
    "password_length": "10"
  },
  "expiration_settings": {
    "expiration_type": "EXPIRATION_TYPE_NEVER_EXPIRE",
    "valid_during_dates": {
      "time_zone": "America/Los_Angeles",
      "start_date_time": {
        "day_of_month": "20",
        "month": "4",
        "year": "2021",
        "hour_of_day": "15",
        "minute_of_hour": "30"
      },
      "end_date_time": {
        "day_of_month": "25",
        "month": "4",
        "year": "2021",
        "hour_of_day": "25",
        "minute_of_hour": "30"
      }
    },
    "valid_for_time_period": {
      "valid_time_period_after": "VALID_TIME_PERIOD_TYPE_AFTER_ID_CREATION",
      "after_id_creation_settings": {
        "valid_time_period": "2",
        "valid_time_period_unit": "DATE_TIME_UNIT_TYPE_HOUR"
      },
      "after_first_login_settings": {
        "valid_time_period": "12",
        "valid_time_period_unit": "DATE_TIME_UNIT_TYPE_WEEK",
        "first_login_within": "5",
        "first_login_within_unit": "DATE_TIME_UNIT_TYPE_DAY"
      }
    },
    "valid_daily": {
      "daily_start_hour": "23",
      "daily_start_minute": "59",
      "daily_end_hour": "22",
      "daily_end_minute": "59"
    },
    "expiration_action": "EXPIRATION_ACTION_TYPE_SHOW_MESSAGE",
    "post_expiration_action": {
      "enable_credentials_renewal": "true",
      "enable_delete_immediately": "false",
      "delete_after_value": "30",
      "delete_after_unit": "DATE_TIME_UNIT_TYPE_DAY"
    }
  },
  "delivery_settings": {
    "email_template_id": "52001",
    "sms_template_id": "53001"
  }
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

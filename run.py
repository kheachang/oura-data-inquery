import requests 
from dotenv import load_dotenv
import os

load_dotenv()

token = 'Bearer ' + os.getenv("TOKEN")

url = 'https://api.ouraring.com/v2/usercollection/daily_sleep' 
params={ 
    'start_date': '2023-11-01', 
    'end_date': '2023-11-04' 
}
headers = { 
  'Authorization': token 
}
response = requests.request('GET', url, headers=headers, params=params) 
print(response.text)
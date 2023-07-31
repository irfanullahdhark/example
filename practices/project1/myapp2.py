import json
import requests

URL = 'http://127.0.0.1:8000/myapp2/'

mydata = {
    'name': 'bawar',
    'roll': 786,
    'city': 'jalalabad'
}

res = requests.post(url=URL , data=mydata)
json_data = res.json()
print(json_data)
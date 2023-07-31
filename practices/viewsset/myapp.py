import requests
import json


URL = 'http://127.0.0.1:8000/myapp/'


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)
    res = requests.get(url=URL,headers={'Content-Type': 'application/json'}, data=json_data)
    try:
        data = res.json()
        print("Response Data:", data)
    except json.JSONDecodeError:
        print("Invalid JSON Response:")


# get_data(2)


def save_data():
    mydata = {
        'name': 'ikram',
        'roll': 20,
        'city': 'kunar'
    }
    json_data = json.dumps(mydata)
    res = requests.post(url=URL,headers={'Content-Type':'application/json'},data=json_data)
    try:
        data = res.json()
        print(data)
    except:
        print('error occured ')


# save_data()


def update_data():
    mydata = {
        'id': 4,
        'name': 'maryam',
        'city': 'kandahar',
    }

    json_data = json.dumps(mydata)
    res = requests.put(url=URL, headers={'Content-Type': 'application/json'}, data=json_data)
    data = res.json()
    print(data)


# update_data()


def delete_data():
    mydata = {
        "id": 3
    }

    json_data = json.dumps(mydata)
    res = requests.delete(url=URL, headers={'Content-Type': 'application/json'}, data=json_data)
    data = res.json()
    print(data)


delete_data()



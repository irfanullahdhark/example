import requests
import json


URL = 'http://127.0.0.1:8000/myapp/'


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)
    res = requests.get(url=URL,data=json_data)
    # Check the status code of the response
    print(f"Status Code: {res.status_code}")

    try:
        data = res.json()
        print("Response Data:", data)
    except json.JSONDecodeError:
        print("Invalid JSON Response:")


# get_data()


def save_data():
    mydata = {
        'name': 'ikram',
        'roll': 222,
        'city': 'kabul'
    }
    json_data = json.dumps(mydata)
    res = requests.post(url=URL,data=json_data)
    try:
        data = res.json()
        print(data)
    except:
        print('error occured ')


save_data()


def update_data():
    mydata = {
        'id': 5,
        'name': 'maryam',
        'city': 'kandahar',
    }

    json_data = json.dumps(mydata)
    res = requests.put(url=URL,data=json_data)
    data = res.json()
    print(data)


# update_data()


def delete_data():
    mydata = {
        "id": 3
    }

    json_data = json.dumps(mydata)
    res = requests.delete(url=URL, data=json_data)
    data = res.json()
    print(data)


# delete_data()



import requests
import json
import time
from datetime import datetime
# current date and time
now = datetime.now()
timestamp = str(int(datetime.timestamp(now)))

mainUrl = "http://localhost:8013/"
root = {}
index = 0
#create user nvvuon
url = mainUrl + "user"
data = {
    "username": "user"+timestamp,
    "password": "1",
    "role": "user"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
time.sleep(5)

# authenicationUser

url = mainUrl + "authentication"
data = {
    "username": "user"+timestamp,
    "password": "1"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
respond_json = json.loads(respond.text)
authorizationuser = respond_json['authorization']
#create user nvvuon
url = mainUrl + "user"
data = {
    "username": "staff"+timestamp,
    "password": "1",
    "role": "staff"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
time.sleep(5)

# authenicationUser

url = mainUrl + "authentication"
data = {
    "username": "staff"+timestamp,
    "password": "1"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
respond_json = json.loads(respond.text)
authorizationstaff = respond_json['authorization']


# create product
url = mainUrl + "lc_test/createLc"
headers = {'Accept': 'text/plain', 'Authorization': authorizationuser}
product_data = {
     "content":"string"
    }

files = {
      }
product_create_respond = requests.post(url, data=json.dumps(product_data), headers=headers, files = files)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = product_create_respond.status_code
root[index][url]['response'] = json.loads(product_create_respond.text)
product_create_respond_json = json.loads(product_create_respond.text)

productId = product_create_respond_json["publicKeyUser"]












with open("log_script_result.json", "w") as outfile:
    json.dump(root, outfile)
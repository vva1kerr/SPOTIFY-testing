"""
https://www.dataquest.io/blog/python-api-tutorial/

http://open-notify.org/
"""
import requests 
 

# response = requests.get("https://www.dataquest.io/blog/python-api-tutorial/")
# print("response:", response)

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.json())

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())




parameters = {
    "lat": 40.71,
    "lon": -74
}
response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

jprint(response.json())
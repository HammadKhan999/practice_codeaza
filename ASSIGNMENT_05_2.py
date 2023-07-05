import requests

url = "https://api.github.com/users/HammadKhan999"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error: ", response.status_code)

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "POST verb", "completed": False}
response = requests.post(api_url, json=todo)


if response.status_code == 201: # a new resource was created
   print(response.json())
else:
    print("Error: ", response.status_code)

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()


todo = {"userId": 1, "title": "PUT verb", "completed": True}
response = requests.put(api_url, json=todo)
if response.status_code == 200: # a new resource was created
   print(response.json())
else:
    print("Error: ", response.status_code)

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "PATCHED PUT VERB"}
response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())

print(response.status_code)



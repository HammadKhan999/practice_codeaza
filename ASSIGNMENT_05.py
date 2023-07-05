import requests

# GitHub API endpoint for retrieving repository information
url = "https://api.github.com/repos/HammadKhan999/University-Management-System-using-MySQL-and-Python"

owner = "HammadKhan999"
repo = "University-Management-System-using-MySQL-and-Python"

url = url.format(owner=owner, repo=repo)

# Send a GET request to the GitHub API
response = requests.get(url)
print(response.content)

# Check the response status code
if response.status_code == 200:
    # if Request was successful
    repository_info = response.json()
    print("Repository Name:", repository_info["name"])
    print("Description:", repository_info["description"])
    print("Language:", repository_info["language"])
    print("Stars:", repository_info["stargazers_count"])
else:
    # Request encountered an error
    print("An error occurred:", response.status_code)

import requests

def send_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "Sample Post",
        "body": "This is a sample post.",
        "userId": 1
    }
    response = requests.post(url, json=data)
    print("POST Response:", response.json())

# PUT request example
def send_put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "id": 1,
        "title": "Updated Post",
        "body": "This post has been updated.",
        "userId": 1
    }
    response = requests.put(url, json=data)
    print("PUT Response:", response.json())

# DELETE request example
def send_delete_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    if response.status_code == 200:
        print("DELETE Request Successful")
    else:
        print("DELETE Request Failed")

# HEAD request example
def send_head_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.head(url)
    print("Headers:", response.headers)

# Execute the requests
send_post_request()
send_put_request()
send_delete_request()
send_head_request()

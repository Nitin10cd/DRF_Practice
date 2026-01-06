import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"hi": "nitin saxena"})
print(get_response.text)
import requests

url = "http://127.0.0.1:8000/generate-image/"
data = {
    "txt": "Beautiful sunset"
}

response = requests.post(url, json=data)

# Print the response from the API
print(response.json())

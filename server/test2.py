import requests

# Set the URL of the endpoint you want to test
url = 'http://localhost:8000/api/send-message'

# Set the data to be sent in the request
data = {
    'message': 'hello world',
    'roomName': 'chat107061102355140117'
}

# Send the POST request
response = requests.post(url, json=data)

# Check the response status code
if response.status_code == 200:
    print('Request successful!')
else:
    print('Request failed with status code:', response.status_code)

# Print the response content
print('Response:', response.text)

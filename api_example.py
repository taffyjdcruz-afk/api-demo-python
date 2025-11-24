import requests

url = "https://api.publicapis.org/entries"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API call successful!")
    print(f"Total entries: {len(data['entries'])}")
else:
    print("Something went wrong:", response.status_code)

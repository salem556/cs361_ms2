import requests

pokemon = "Squirtle"
url = f"http://localhost:5000/pokemon-image/{pokemon}"
response = requests.get(url)

try:
    data = response.json()
    if response.status_code == 200:
        print(f"Name: {data['name']}")
        print(f"Image URL: {data['image_url']}")
    else:
        print("Error:", data.get('error', 'Unknown error'))
except Exception as e:
    print("Failed to parse response:", response.text)
    print("Error details:", e)

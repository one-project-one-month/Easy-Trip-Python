import requests


api_url = requests.post("http://127.0.0.1:8000/trip/invoke", json = {"input":{"input":"Trip Planning for this ChaungTharBeach with family within 5/15/2025 to 5/20/2025 with 1000000 MMK"}})

print(api_url.json()['output']['content'])


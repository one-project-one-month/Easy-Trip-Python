import requests


api_url = requests.post("https://bring-45n9.onrender.com/things/invoke", json = {"input":{"input":"Trip Planning for this ChaungTharBeach with family within 5/15/2025 to 5/20/2025 with 1000000 MMK"}})

print(api_url.json()['output']['content'])

api_url = requests.post("https://easy-trip-python-5.onrender.com/trip/invoke", json = {"input":{"input":"Explain with description why we should bring in order to go to ChaungTharBeach with Family within 5/15/2025 to 5/20/2025 with 1500000 MMK"}})

print(api_url.json()['output']['content'])

import requests
import json
base_url = "https://deckofcardsapi.com/"
URL = base_url + "api/deck/new/shuffle/?deck_count=1"
response = requests.get(url = URL)
print(response.status_code)
print(response.text)
res = response.json()
print(res)
print(type(res))
deckid = res['deck_id']
print(deckid)
URL1 = base_url + "api/deck/45opgtuqjted/draw/?count=2"
resp = requests.get(url = URL1)
print(resp.status_code)
print(resp.text)
dic = resp.json()
print(dic['cards'][0]['value'])


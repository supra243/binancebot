import requests
import json

from api_config import API_KEY
BASE_URL = "https://rest.coinapi.io/"

url = BASE_URL + "v1/assets"

payload={}
headers = {
  'Accept': 'text/plain',
  'X-CoinAPI-Key': API_KEY
}

response = requests.request("GET", url, headers=headers, data=payload)

# 200/ sinon afficher l'erreur
if response.status_code == 200:
  data = json.loads(response.text)
  print(response.asset_id)
  
else : 
  print("l'erreur est : {}".format(response.status_code))
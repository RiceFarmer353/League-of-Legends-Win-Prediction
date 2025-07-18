from PARAMS import API_KEY, REGION_ID
import requests

url = f'https://{REGION_ID}.api.riotgames.com//riot/account/v1/accounts/by-riot-id/RiceFarmer/seeds'

headers = {
    'Accept': 'application/json',
    'X-Riot-Token': API_KEY
}

request = requests.get(url, headers=headers)
print(request.json())
import requests


# Match V5

#collect game ids from a puuid
def get_gameids_by_puuid(region, puuid, connection):
    url = f'https://{region}.api.riotgames.com//lol/match/v5/matches/by-puuid/{puuid}/ids?startTime=1704883658&start=0&count=100'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()

#get game info by game id
def get_game_general_info(region, game_id, connection):
    url= f'https://{region}.api.riotgames.com//lol/match/v5/matches/{game_id}'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()

#get game timeline by game id
def get_timeline_by_game_id(region, game_id, connection):
    url = f'https://{region}.api.riotgames.com//lol/match/v5/matches/{game_id}/timeline'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()



# summoner V4

# get puuid by summoner id
def get_puuid_by_summoner_id(region, summoner_id, connection):
    url = f'https://{region}.api.riotgames.com//lol/summoner/v4/summoners/{summoner_id}'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()



# league V4
#collect challenger players
def get_challenger_players_league_v4(region, queue, connection):
    url = f'https://{region}.api.riotgames.com//lol/league/v4/challengerleagues/by-queue/{queue}'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()

#collect grandmaster players
def get_grandmaster_players_league_v4(region, queue, connection):
    url = f'https://{region}.api.riotgames.com//lol/league/v4/grandmasterleagues/by-queue/{queue}'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()

#collect master players
def get_master_players_league_v4(region, queue, connection):
    url = f'https://{region}.api.riotgames.com//lol/league/v4/masterleagues/by-queue/{queue}'
    headers = {
        'Accept': 'application/json',
        'X-Riot-Token': connection
    }
    request = requests.get(url, headers=headers)
    return request.json()


from helpers_match_v5 import get_challenger_players_league_v4, get_grandmaster_players_league_v4, get_puuid_by_summoner_id
from PARAMS import API_KEY, PLATFORM_ID, QUEUE, PLATFORM_IDS
import time


def write_into_txt(match_id_list):
    with(open('gameIdPlatforms/match_ids.txt', 'a')) as f:
        for i in match_id_list:
            f.write(i + '\n')

def main():
    summoner_id_list = []
    puuid_id_list = []
    current_summoner_id_list_length = 0
    previous_summoner_id_list_length = 0

    for current_platform in PLATFORM_IDS:
        print('Challeger players:')
        print('----------------------------------------------------------------------------------------------------------------')
        print(f'Current platform: {current_platform}')
    
        # get challenger summoner ids
        challenger_players = get_challenger_players_league_v4(current_platform, QUEUE, API_KEY)
        for i in challenger_players['entries']:
            summoner_id_list.append(i['summonerId'])
        current_summoner_id_list_length = len(summoner_id_list)
        print(f'summoner_id_list length: {current_summoner_id_list_length}')
        time.sleep(1.2)

        # get puuid by summoner id
        for i in range(previous_summoner_id_list_length, current_summoner_id_list_length):
            puuid = get_puuid_by_summoner_id(current_platform, summoner_id_list[i], API_KEY)['puuid']
            puuid_id_list.append(puuid)
            print(len(puuid_id_list))
            time.sleep(1.2)
        previous_summoner_id_list_length = len(summoner_id_list)
        print(puuid_id_list)
        print(f'puuid_id_list length: {len(puuid_id_list)} \n')
        print('----------------------------------------------------------------------------------------------------------------')

    for current_platform in PLATFORM_IDS:

        print('Grandmaster players:')
        print('----------------------------------------------------------------------------------------------------------------')
        print(f'Current platform: {current_platform}')
    
        # get grandmaster summoner ids
        grandmaster_players = get_grandmaster_players_league_v4(current_platform, QUEUE, API_KEY)
        for i in grandmaster_players['entries']:
            summoner_id_list.append(i['summonerId'])
        current_summoner_id_list_length = len(summoner_id_list)
        print(f'summoner_id_list length: {len(summoner_id_list)}')
        time.sleep(1.2)

        # get puuid by summoner id
        for i in range(previous_summoner_id_list_length, current_summoner_id_list_length):
            puuid = get_puuid_by_summoner_id(current_platform, summoner_id_list[i], API_KEY)['puuid']
            puuid_id_list.append(puuid)
            print(len(puuid_id_list))
            time.sleep(1.2)
            if len(puuid_id_list) >= 1000:
                break
        previous_summoner_id_list_length = len(summoner_id_list)
        print(puuid_id_list)
        print(f'puuid_id_list length: {len(puuid_id_list)}')
        print('----------------------------------------------------------------------------------------------------------------')


    with open('1_puuids.txt', 'w') as f:
        for i in puuid_id_list:
            f.write(i + '\n')



if __name__ == '__main__':
    main()
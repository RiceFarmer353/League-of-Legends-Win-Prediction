from helpers_match_v5 import get_gameids_by_puuid
from PARAMS import API_KEY, REGION_IDS
import time


def main():
    all_game_ids = []

    with(open('1_puuids.txt', 'r')) as f:
        puuids = f.read().splitlines()
        for current_puuid in puuids:
            print(f'Current number: {puuids.index(current_puuid) + 1}')
            print(f'Current puuid: {current_puuid}')
            for current_region in REGION_IDS:
                print(f'Current region: {current_region}')
                game_ids = get_gameids_by_puuid(current_region, current_puuid, API_KEY)
                time.sleep(1.2)
                print(f'Game ids: {game_ids}')
                for i in game_ids:
                    if i not in all_game_ids:
                        all_game_ids.append(i)
            print(f'All game ids: {all_game_ids}')
            print(f'All game ids length: {len(all_game_ids)}')
            print('-----------------------------------')

    with open('2_game_ids.txt', 'w') as f:
        for i in all_game_ids:
            f.write(i + '\n')




if __name__ == '__main__':
    main()
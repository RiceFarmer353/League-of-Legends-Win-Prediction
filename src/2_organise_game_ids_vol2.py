regions = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'TR1', 'RU', 'PH2', 'SG2', 'TH2', 'VN2']

for region in regions:
    with(open(f'./gameIdPlatforms_for_timeStamps/{region}_game_ids.txt', 'r')) as f:
        game_ids = f.read().splitlines()
    
        game_ids_splitted_list = [game_ids[i:i + 500] for i in range(0, len(game_ids), 500)]
        number_of_lists = len(game_ids_splitted_list)

        for i, current_list in enumerate(game_ids_splitted_list):
            with(open(f'./gameIdPlatforms_for_timeStamps/{region}_game_ids/{region}_game_ids_{i + 1}.txt', 'w')) as file:
                for current_game_id in current_list:
                    file.write(current_game_id + '\n')

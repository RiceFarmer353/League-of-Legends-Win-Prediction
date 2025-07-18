BR1_game_ids = []
EUN1_game_ids = []
EUW1_game_ids = []
JP1_game_ids = []
KR_game_ids = []
LA1_game_ids = []
LA2_game_ids = []
NA1_game_ids = []
OC1_game_ids = []
TR1_game_ids = []
RU_game_ids = []
PH2_game_ids = []
SG2_game_ids = []
TH2_game_ids = []
VN2_game_ids = []


with(open('2_game_ids_for_timeStamp.txt', 'r')) as f:
    game_ids = f.read().splitlines()
    print(game_ids)
    print(len(game_ids))

    for current_game_id in game_ids:
        if current_game_id[:3] == 'BR1':
            BR1_game_ids.append(current_game_id)
        elif current_game_id[:4] == 'EUN1':
            EUN1_game_ids.append(current_game_id)
        elif current_game_id[:4] == 'EUW1':
            EUW1_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'JP1':
            JP1_game_ids.append(current_game_id)
        elif current_game_id[:2] == 'KR':
            KR_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'LA1':
            LA1_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'LA2':
            LA2_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'NA1':
            NA1_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'OC1':
            OC1_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'TR1':
            TR1_game_ids.append(current_game_id)
        elif current_game_id[:2] == 'RU':
            RU_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'PH2':
            PH2_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'SG2':
            SG2_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'TH2':
            TH2_game_ids.append(current_game_id)
        elif current_game_id[:3] == 'VN2':
            VN2_game_ids.append(current_game_id)
        
    with open('gameIdPlatforms_for_timeStamps/BR1_game_ids.txt', 'w') as f:
        for i in BR1_game_ids:
            f.write(i + '\n')
    
    with open('gameIdPlatforms_for_timeStamps/EUN1_game_ids.txt', 'w') as f:
        for i in EUN1_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/EUW1_game_ids.txt', 'w') as f:
        for i in EUW1_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/JP1_game_ids.txt', 'w') as f:
        for i in JP1_game_ids:
            f.write(i + '\n')
    
    with open('gameIdPlatforms_for_timeStamps/KR_game_ids.txt', 'w') as f:
        for i in KR_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/LA1_game_ids.txt', 'w') as f:
        for i in LA1_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/LA2_game_ids.txt', 'w') as f:
        for i in LA2_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/NA1_game_ids.txt', 'w') as f:
        for i in NA1_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/OC1_game_ids.txt', 'w') as f:
        for i in OC1_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/TR1_game_ids.txt', 'w') as f:
        for i in TR1_game_ids:
            f.write(i + '\n')
    
    with open('gameIdPlatforms_for_timeStamps/RU_game_ids.txt', 'w') as f:
        for i in RU_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/PH2_game_ids.txt', 'w') as f:
        for i in PH2_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/SG2_game_ids.txt', 'w') as f:
        for i in SG2_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/TH2_game_ids.txt', 'w') as f:
        for i in TH2_game_ids:
            f.write(i + '\n')

    with open('gameIdPlatforms_for_timeStamps/VN2_game_ids.txt', 'w') as f:
        for i in VN2_game_ids:
            f.write(i + '\n')

import time
import csv
import pandas as pd


start_time = time.time()


full_data_new_vol2_list = []

with open('../2_game_ids_for_timeStamp.txt', 'r') as f:
    reader = csv.reader(f)
    game_ids = list(reader)

with open('./full_data_new_timeInterval/full_data_new_100.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

    print(data)

    for i in data:
        if [i[1]] in game_ids:
            full_data_new_vol2_list.append(i)

print(f'Full list: {full_data_new_vol2_list}')

with open('./full_data_new_timeInterval_same_matchIDs_as_timeStamp/full_data_new_100_vol2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    headers = ['matchID', 'fullTimeMS', 'timeStamp', 'blueChampionKill', 'blueFirstBlood', 'blueDragonKill', 'blueDragonHextechKill', 'blueDragonChemtechKill', 'blueDragonFireKill', 'blueDragonAirKill', 'blueDragonEarthKill', 'blueDragonWaterKill', 'blueDragonElderKill', 'blueVoidGrubKill', 'blueRiftHeraldKill', 'blueBaronKill', 'blueTowerKill', 'blueInhibitorKill', 'blueTotalGold', 'blueMinionsKilled', 'blueJungleMinionsKilled', 'blueAvgPlayerLevel', 'blueWin', 'redChampionKill', 'redFirstBlood', 'redDragonKill', 'redDragonHextechKill', 'redDragonChemtechKill', 'redDragonFireKill', 'redDragonAirKill', 'redDragonEarthKill', 'redDragonWaterKill', 'redDragonElderKill', 'redVoidGrubKill', 'redRiftHeraldKill', 'redBaronKill', 'redTowerKill', 'redInhibitorKill', 'redTotalGold', 'redMinionsKilled', 'redJungleMinionsKilled', 'redAvgPlayerLevel', 'redWin']
    writer.writerow(headers)
    for i in full_data_new_vol2_list:
        writer.writerow(i)


end_time = time.time()

print(f'Execution time: {end_time - start_time} seconds')
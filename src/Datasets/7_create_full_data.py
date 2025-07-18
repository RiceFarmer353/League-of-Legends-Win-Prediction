import csv
import time

start_time = time.time()
region_list = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'PH2', 'RU', 'SG2', 'TH2', 'TR1', 'VN2']


# 'timeInterval_', 'timeStamp_'
prefix = 'timeStamp_'

# 4, 5
prefix_associated_number = '5'

# 20, 40, 60, 80, 100, end, min10, min14, min20, min27
file_name_ending_list1 = ['20', '40', '60', '80', '100']
file_name_ending_list2 = ['end', 'min10', 'min14', 'min20', 'min27']

file_name_ending = 'min27'

firstLine = ',matchID,fullTimeMS,timeStamp,blueChampionKill,blueFirstBlood,blueDragonKill,blueDragonHextechKill,blueDragonChemtechKill,blueDragonFireKill,blueDragonAirKill,blueDragonEarthKill,blueDragonWaterKill,blueDragonElderKill,blueVoidGrubKill,blueRiftHeraldKill,blueBaronKill,blueTowerKill,blueInhibitorKill,blueTotalGold,blueMinionsKilled,blueJungleMinionsKilled,blueAvgPlayerLevel,blueWin,redChampionKill,redFirstBlood,redDragonKill,redDragonHextechKill,redDragonChemtechKill,redDragonFireKill,redDragonAirKill,redDragonEarthKill,redDragonWaterKill,redDragonElderKill,redVoidGrubKill,redRiftHeraldKill,redBaronKill,redTowerKill,redInhibitorKill,redTotalGold,redMinionsKilled,redJungleMinionsKilled,redAvgPlayerLevel,redWin'

output_file_name = f'./full_data_new_{prefix[:-1]}/full_data_new_{file_name_ending}.csv'

with open(output_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(firstLine.split(','))

for region in region_list:
    file_name = f'./Platform_Datasets_self_made/{region}/{prefix_associated_number}_new_full_data_{file_name_ending}({region}_game_ids).csv'

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        file_rows = list(csv_reader)
    
        for current_row in file_rows[1:]:
            with open(output_file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(current_row)

end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')
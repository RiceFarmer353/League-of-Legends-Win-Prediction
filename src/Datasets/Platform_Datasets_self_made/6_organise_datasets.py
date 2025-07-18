import csv

first_row = ',matchID,fullTimeMS,timeStamp,blueChampionKill,blueFirstBlood,blueDragonKill,blueDragonHextechKill,blueDragonChemtechKill,blueDragonFireKill,blueDragonAirKill,blueDragonEarthKill,blueDragonWaterKill,blueDragonElderKill,blueVoidGrubKill,blueRiftHeraldKill,blueBaronKill,blueTowerKill,blueInhibitorKill,blueTotalGold,blueMinionsKilled,blueJungleMinionsKilled,blueAvgPlayerLevel,blueWin,redChampionKill,redFirstBlood,redDragonKill,redDragonHextechKill,redDragonChemtechKill,redDragonFireKill,redDragonAirKill,redDragonEarthKill,redDragonWaterKill,redDragonElderKill,redVoidGrubKill,redRiftHeraldKill,redBaronKill,redTowerKill,redInhibitorKill,redTotalGold,redMinionsKilled,redJungleMinionsKilled,redAvgPlayerLevel,redWin\n'

# 20, 40, 60, 80, 100, end, min10, min14, min20, min27
file_name_ending_list1 = ['20', '40', '60', '80', '100']
file_name_ending_list2 = ['end', 'min10', 'min14', 'min20', 'min27']
#file_name_ending = 'min27'
#
region = 'VN2'
# timeInterval, timeStamp_
prefix_list = ['timeStamp_']
#prefix = 'timeStamp_'
# 4, 5
prefix_associated_number_list = ['5']
#prefix_associated_number = '5'

numbers_list = [1, 2]

for i, prefix in enumerate(prefix_list):
    if i == 0:
        file_name_ending_list = file_name_ending_list2
    elif i == 1:
        file_name_ending_list = file_name_ending_list1

    for file_name_ending in file_name_ending_list:

        created_file_name = f'{prefix_associated_number_list[i]}_new_full_data_{file_name_ending}({region}_game_ids).csv'

        with open(f'./{region}/{created_file_name}', 'w') as file:
            file.write(first_row)

        for number in numbers_list:
            searched_file_name = f'{prefix_associated_number_list[i]}_new_dataset_{file_name_ending}({region}_game_ids_{number}).csv'
            with open(f'./{region}/{prefix}{file_name_ending}/{searched_file_name}', 'r') as file:
                csv_reader = csv.reader(file)

                next(csv_reader)

                for row in csv_reader:

                    with open(f'./{region}/{created_file_name}', 'a', newline='') as file_create:
                        writer = csv.writer(file_create)
                        writer.writerow(row)
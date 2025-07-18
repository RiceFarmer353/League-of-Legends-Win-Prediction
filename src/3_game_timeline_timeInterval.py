from helpers_match_v5 import get_timeline_by_game_id
from PARAMS import API_KEY
import time
import csv


def main():
    # Measuring time
    start_time = time.time()

    # Other variables
    region_for_file = 'BR1'
    number = 1

    matchIDs_path = f'./gameIdPlatforms/{region_for_file}_game_ids/{region_for_file}_game_ids_{number}.txt'
    name_for_file_20 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeInterval_20/4_new_dataset_20({region_for_file}_game_ids_{number}).csv'
    name_for_file_40 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeInterval_40/4_new_dataset_40({region_for_file}_game_ids_{number}).csv'
    name_for_file_60 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeInterval_60/4_new_dataset_60({region_for_file}_game_ids_{number}).csv'
    name_for_file_80 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeInterval_80/4_new_dataset_80({region_for_file}_game_ids_{number}).csv'
    name_for_file_100 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeInterval_100/4_new_dataset_100({region_for_file}_game_ids_{number}).csv'
    name_for_file_min10 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min10/5_new_dataset_min10({region_for_file}_game_ids_{number}).csv'
    name_for_file_min14 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min14/5_new_dataset_min14({region_for_file}_game_ids_{number}).csv'
    name_for_file_min20 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min20/5_new_dataset_min20({region_for_file}_game_ids_{number}).csv'
    name_for_file_min27 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min27/5_new_dataset_min27({region_for_file}_game_ids_{number}).csv'
    name_for_file_end = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_end/5_new_dataset_end({region_for_file}_game_ids_{number}).csv'

    # Csv header
    firstLine = ',matchID,fullTimeMS,timeStamp,blueChampionKill,blueFirstBlood,blueDragonKill,blueDragonHextechKill,blueDragonChemtechKill,blueDragonFireKill,blueDragonAirKill,blueDragonEarthKill,blueDragonWaterKill,blueDragonElderKill,blueVoidGrubKill,blueRiftHeraldKill,blueBaronKill,blueTowerKill,blueInhibitorKill,blueTotalGold,blueMinionsKilled,blueJungleMinionsKilled,blueAvgPlayerLevel,blueWin,redChampionKill,redFirstBlood,redDragonKill,redDragonHextechKill,redDragonChemtechKill,redDragonFireKill,redDragonAirKill,redDragonEarthKill,redDragonWaterKill,redDragonElderKill,redVoidGrubKill,redRiftHeraldKill,redBaronKill,redTowerKill,redInhibitorKill,redTotalGold,redMinionsKilled,redJungleMinionsKilled,redAvgPlayerLevel,redWin'

    # Variables for new_dataset_{timeInterval}.csv

    # General variables timeInterval
    Column1_timeInterval = list()
    matchID_timeInterval = list()
    fullTimeMS_timeInterval = list()

    # timeIntervalPercentages at 1 (full time)
    timeStamp = list()
    blueChampionKill = list()
    blueFirstBlood = list()
    blueDragonKill = list()
    blueDragonHextechKill = list()
    blueDragonChemtechKill = list()
    blueDragonFireKill = list()
    blueDragonAirKill = list()
    blueDragonEarthKill = list()
    blueDragonWaterKill = list()
    blueDragonElderKill = list()
    blueVoidGrubKill = list()
    blueRiftHeraldKill = list()
    blueBaronKill = list()
    blueTowerKill = list()
    blueInhibitorKill = list()
    blueTotalGold = list()
    blueMinionsKilled = list()
    blueJungleMinionsKilled = list()
    blueAvgPlayerLevel = list()
    blueWin = list()
    redChampionKill = list()
    redFirstBlood = list()
    redDragonKill = list()
    redDragonHextechKill = list()
    redDragonChemtechKill = list()
    redDragonFireKill = list()
    redDragonAirKill = list()
    redDragonEarthKill = list()
    redDragonWaterKill = list()
    redDragonElderKill = list()
    redVoidGrubKill = list()
    redRiftHeraldKill = list()
    redBaronKill = list()
    redTowerKill = list()
    redInhibitorKill = list()
    redTotalGold = list()
    redMinionsKilled = list()
    redJungleMinionsKilled = list()
    redAvgPlayerLevel = list()
    redWin = list()

    # timeIntervalPercentages at 0.2
    timeStamp_20 = list()
    blueChampionKill_20 = list()
    blueDragonKill_20 = list()
    blueDragonHextechKill_20 = list()
    blueDragonChemtechKill_20 = list()
    blueDragonFireKill_20 = list()
    blueDragonAirKill_20 = list()
    blueDragonEarthKill_20 = list()
    blueDragonWaterKill_20 = list()
    blueDragonElderKill_20 = list()
    blueVoidGrubKill_20 = list()
    blueRiftHeraldKill_20 = list()
    blueBaronKill_20 = list()
    blueTowerKill_20 = list()
    blueInhibitorKill_20 = list()
    blueTotalGold_20 = list()
    blueMinionsKilled_20 = list()
    blueJungleMinionsKilled_20 = list()
    blueAvgPlayerLevel_20 = list()
    redChampionKill_20 = list()
    redDragonKill_20 = list()
    redDragonHextechKill_20 = list()
    redDragonChemtechKill_20 = list()
    redDragonFireKill_20 = list()
    redDragonAirKill_20 = list()
    redDragonEarthKill_20 = list()
    redDragonWaterKill_20 = list()
    redDragonElderKill_20 = list()
    redVoidGrubKill_20 = list()
    redRiftHeraldKill_20 = list()
    redBaronKill_20 = list()
    redTowerKill_20 = list()
    redInhibitorKill_20 = list()
    redTotalGold_20 = list()
    redMinionsKilled_20 = list()
    redJungleMinionsKilled_20 = list()
    redAvgPlayerLevel_20 = list()

    # timeIntervalPercentages at 0.4
    timeStamp_40 = list()
    blueChampionKill_40 = list()
    blueDragonKill_40 = list()
    blueDragonHextechKill_40 = list()
    blueDragonChemtechKill_40 = list()
    blueDragonFireKill_40 = list()
    blueDragonAirKill_40 = list()
    blueDragonEarthKill_40 = list()
    blueDragonWaterKill_40 = list()
    blueDragonElderKill_40 = list()
    blueVoidGrubKill_40 = list()
    blueRiftHeraldKill_40 = list()
    blueBaronKill_40 = list()
    blueTowerKill_40 = list()
    blueInhibitorKill_40 = list()
    blueTotalGold_40 = list()
    blueMinionsKilled_40 = list()
    blueJungleMinionsKilled_40 = list()
    blueAvgPlayerLevel_40 = list()
    redChampionKill_40 = list()
    redDragonKill_40 = list()
    redDragonHextechKill_40 = list()
    redDragonChemtechKill_40 = list()
    redDragonFireKill_40 = list()
    redDragonAirKill_40 = list()
    redDragonEarthKill_40 = list()
    redDragonWaterKill_40 = list()
    redDragonElderKill_40 = list()
    redVoidGrubKill_40 = list()
    redRiftHeraldKill_40 = list()
    redBaronKill_40 = list()
    redTowerKill_40 = list()
    redInhibitorKill_40 = list()
    redTotalGold_40 = list()
    redMinionsKilled_40 = list()
    redJungleMinionsKilled_40 = list()
    redAvgPlayerLevel_40 = list()

    # timeIntervalPercentages at 0.6
    timeStamp_60 = list()
    blueChampionKill_60 = list()
    blueDragonKill_60 = list()
    blueDragonHextechKill_60 = list()
    blueDragonChemtechKill_60 = list()
    blueDragonFireKill_60 = list()
    blueDragonAirKill_60 = list()
    blueDragonEarthKill_60 = list()
    blueDragonWaterKill_60 = list()
    blueDragonElderKill_60 = list()
    blueVoidGrubKill_60 = list()
    blueRiftHeraldKill_60 = list()
    blueBaronKill_60 = list()
    blueTowerKill_60 = list()
    blueInhibitorKill_60 = list()
    blueTotalGold_60 = list()
    blueMinionsKilled_60 = list()
    blueJungleMinionsKilled_60 = list()
    blueAvgPlayerLevel_60 = list()
    redChampionKill_60 = list()
    redDragonKill_60 = list()
    redDragonHextechKill_60 = list()
    redDragonChemtechKill_60 = list()
    redDragonFireKill_60 = list()
    redDragonAirKill_60 = list()
    redDragonEarthKill_60 = list()
    redDragonWaterKill_60 = list()
    redDragonElderKill_60 = list()
    redVoidGrubKill_60 = list()
    redRiftHeraldKill_60 = list()
    redBaronKill_60 = list()
    redTowerKill_60 = list()
    redInhibitorKill_60 = list()
    redTotalGold_60 = list()
    redMinionsKilled_60 = list()
    redJungleMinionsKilled_60 = list()
    redAvgPlayerLevel_60 = list()

    # timeIntervalPercentages at 0.8
    timeStamp_80 = list()
    blueChampionKill_80 = list()
    blueDragonKill_80 = list()
    blueDragonHextechKill_80 = list()
    blueDragonChemtechKill_80 = list()
    blueDragonFireKill_80 = list()
    blueDragonAirKill_80 = list()
    blueDragonEarthKill_80 = list()
    blueDragonWaterKill_80 = list()
    blueDragonElderKill_80 = list()
    blueVoidGrubKill_80 = list()
    blueRiftHeraldKill_80 = list()
    blueBaronKill_80 = list()
    blueTowerKill_80 = list()
    blueInhibitorKill_80 = list()
    blueTotalGold_80 = list()
    blueMinionsKilled_80 = list()
    blueJungleMinionsKilled_80 = list()
    blueAvgPlayerLevel_80 = list()
    redChampionKill_80 = list()
    redDragonKill_80 = list()
    redDragonHextechKill_80 = list()
    redDragonChemtechKill_80 = list()
    redDragonFireKill_80 = list()
    redDragonAirKill_80 = list()
    redDragonEarthKill_80 = list()
    redDragonWaterKill_80 = list()
    redDragonElderKill_80 = list()
    redVoidGrubKill_80 = list()
    redRiftHeraldKill_80 = list()
    redBaronKill_80 = list()
    redTowerKill_80 = list()
    redInhibitorKill_80 = list()
    redTotalGold_80 = list()
    redMinionsKilled_80 = list()
    redJungleMinionsKilled_80 = list()
    redAvgPlayerLevel_80 = list()

    # Variables for new_dataset_min{time}.csv

    # General variables time
    Column1_time = list()
    matchID_time = list()
    fullTimeMS_time = list()

    # fixed time variables
    blueFirstBlood_time = list()
    blueWin_time = list()
    redFirstBlood_time = list()
    redWin_time = list()

    # fullTimeMSVariable at 10
    timeStamp_min10 = list()
    blueChampionKill_min10 = list()
    blueDragonKill_min10 = list()
    blueDragonHextechKill_min10 = list()
    blueDragonChemtechKill_min10 = list()
    blueDragonFireKill_min10 = list()
    blueDragonAirKill_min10 = list()
    blueDragonEarthKill_min10 = list()
    blueDragonWaterKill_min10 = list()
    blueDragonElderKill_min10 = list()
    blueVoidGrubKill_min10 = list()
    blueRiftHeraldKill_min10 = list()
    blueBaronKill_min10 = list()
    blueTowerKill_min10 = list()
    blueInhibitorKill_min10 = list()
    blueTotalGold_min10 = list()
    blueMinionsKilled_min10 = list()
    blueJungleMinionsKilled_min10 = list()
    blueAvgPlayerLevel_min10 = list()
    redChampionKill_min10 = list()
    redDragonKill_min10 = list()
    redDragonHextechKill_min10 = list()
    redDragonChemtechKill_min10 = list()
    redDragonFireKill_min10 = list()
    redDragonAirKill_min10 = list()
    redDragonEarthKill_min10 = list()
    redDragonWaterKill_min10 = list()
    redDragonElderKill_min10 = list()
    redVoidGrubKill_min10 = list()
    redRiftHeraldKill_min10 = list()
    redBaronKill_min10 = list()
    redTowerKill_min10 = list()
    redInhibitorKill_min10 = list()
    redTotalGold_min10 = list()
    redMinionsKilled_min10 = list()
    redJungleMinionsKilled_min10 = list()
    redAvgPlayerLevel_min10 = list()

    # fullTimeMSVariable at 14
    timeStamp_min14 = list()
    blueChampionKill_min14 = list()
    blueDragonKill_min14 = list()
    blueDragonHextechKill_min14 = list()
    blueDragonChemtechKill_min14 = list()
    blueDragonFireKill_min14 = list()
    blueDragonAirKill_min14 = list()
    blueDragonEarthKill_min14 = list()
    blueDragonWaterKill_min14 = list()
    blueDragonElderKill_min14 = list()
    blueVoidGrubKill_min14 = list()
    blueRiftHeraldKill_min14 = list()
    blueBaronKill_min14 = list()
    blueTowerKill_min14 = list()
    blueInhibitorKill_min14 = list()
    blueTotalGold_min14 = list()
    blueMinionsKilled_min14 = list()
    blueJungleMinionsKilled_min14 = list()
    blueAvgPlayerLevel_min14 = list()
    redChampionKill_min14 = list()
    redDragonKill_min14 = list()
    redDragonHextechKill_min14 = list()
    redDragonChemtechKill_min14 = list()
    redDragonFireKill_min14 = list()
    redDragonAirKill_min14 = list()
    redDragonEarthKill_min14 = list()
    redDragonWaterKill_min14 = list()
    redDragonElderKill_min14 = list()
    redVoidGrubKill_min14 = list()
    redRiftHeraldKill_min14 = list()
    redBaronKill_min14 = list()
    redTowerKill_min14 = list()
    redInhibitorKill_min14 = list()
    redTotalGold_min14 = list()
    redMinionsKilled_min14 = list()
    redJungleMinionsKilled_min14 = list()
    redAvgPlayerLevel_min14 = list()

    # fullTimeMSVariable at 20
    timeStamp_min20 = list()
    blueChampionKill_min20 = list()
    blueDragonKill_min20 = list()
    blueDragonHextechKill_min20 = list()
    blueDragonChemtechKill_min20 = list()
    blueDragonFireKill_min20 = list()
    blueDragonAirKill_min20 = list()
    blueDragonEarthKill_min20 = list()
    blueDragonWaterKill_min20 = list()
    blueDragonElderKill_min20 = list()
    blueVoidGrubKill_min20 = list()
    blueRiftHeraldKill_min20 = list()
    blueBaronKill_min20 = list()
    blueTowerKill_min20 = list()
    blueInhibitorKill_min20 = list()
    blueTotalGold_min20 = list()
    blueMinionsKilled_min20 = list()
    blueJungleMinionsKilled_min20 = list()
    blueAvgPlayerLevel_min20 = list()
    redChampionKill_min20 = list()
    redDragonKill_min20 = list()
    redDragonHextechKill_min20 = list()
    redDragonChemtechKill_min20 = list()
    redDragonFireKill_min20 = list()
    redDragonAirKill_min20 = list()
    redDragonEarthKill_min20 = list()
    redDragonWaterKill_min20 = list()
    redDragonElderKill_min20 = list()
    redVoidGrubKill_min20 = list()
    redRiftHeraldKill_min20 = list()
    redBaronKill_min20 = list()
    redTowerKill_min20 = list()
    redInhibitorKill_min20 = list()
    redTotalGold_min20 = list()
    redMinionsKilled_min20 = list()
    redJungleMinionsKilled_min20 = list()
    redAvgPlayerLevel_min20 = list()

    # fullTimeMSVariable at 27
    timeStamp_min27 = list()
    blueChampionKill_min27 = list()
    blueDragonKill_min27 = list()
    blueDragonHextechKill_min27 = list()
    blueDragonChemtechKill_min27 = list()
    blueDragonFireKill_min27 = list()
    blueDragonAirKill_min27 = list()
    blueDragonEarthKill_min27 = list()
    blueDragonWaterKill_min27 = list()
    blueDragonElderKill_min27 = list()
    blueVoidGrubKill_min27 = list()
    blueRiftHeraldKill_min27 = list()
    blueBaronKill_min27 = list()
    blueTowerKill_min27 = list()
    blueInhibitorKill_min27 = list()
    blueTotalGold_min27 = list()
    blueMinionsKilled_min27 = list()
    blueJungleMinionsKilled_min27 = list()
    blueAvgPlayerLevel_min27 = list()
    redChampionKill_min27 = list()
    redDragonKill_min27 = list()
    redDragonHextechKill_min27 = list()
    redDragonChemtechKill_min27 = list()
    redDragonFireKill_min27 = list()
    redDragonAirKill_min27 = list()
    redDragonEarthKill_min27 = list()
    redDragonWaterKill_min27 = list()
    redDragonElderKill_min27 = list()
    redVoidGrubKill_min27 = list()
    redRiftHeraldKill_min27 = list()
    redBaronKill_min27 = list()
    redTowerKill_min27 = list()
    redInhibitorKill_min27 = list()
    redTotalGold_min27 = list()
    redMinionsKilled_min27 = list()
    redJungleMinionsKilled_min27 = list()
    redAvgPlayerLevel_min27 = list()

    #fullTimeMSVariable at end
    timeStamp_end = list()
    blueChampionKill_end = list()
    blueDragonKill_end = list()
    blueDragonHextechKill_end = list()
    blueDragonChemtechKill_end = list()
    blueDragonFireKill_end = list()
    blueDragonAirKill_end = list()
    blueDragonEarthKill_end = list()
    blueDragonWaterKill_end = list()
    blueDragonElderKill_end = list()
    blueVoidGrubKill_end = list()
    blueRiftHeraldKill_end = list()
    blueBaronKill_end = list()
    blueTowerKill_end = list()
    blueInhibitorKill_end = list()
    blueTotalGold_end = list()
    blueMinionsKilled_end = list()
    blueJungleMinionsKilled_end = list()
    blueAvgPlayerLevel_end = list()
    redChampionKill_end = list()
    redDragonKill_end = list()
    redDragonHextechKill_end = list()
    redDragonChemtechKill_end = list()
    redDragonFireKill_end = list()
    redDragonAirKill_end = list()
    redDragonEarthKill_end = list()
    redDragonWaterKill_end = list()
    redDragonElderKill_end = list()
    redVoidGrubKill_end = list()
    redRiftHeraldKill_end = list()
    redBaronKill_end = list()
    redTowerKill_end = list()
    redInhibitorKill_end = list()
    redTotalGold_end = list()
    redMinionsKilled_end = list()
    redJungleMinionsKilled_end = list()
    redAvgPlayerLevel_end = list()


    # defined values
    timeIntervalPercentages = [0.2, 0.4, 0.6, 0.8, 1]
    # minutesPassed at line 891
    blueTeamPlayerIds = [1, 2, 3, 4, 5]
    redTeamPlayerIds = [6, 7, 8, 9, 10]

    with(open(matchIDs_path, 'r')) as f:
        match_ids = f.read().splitlines()
        region = ''
        api_call_start_time = time.time()

        # Code: Column1_timeInterval, matchID_timeInterval
        for column1, current_game_id in enumerate(match_ids):
            
        # Variables default values

            # For both
            blueFirstBloodVariable = False
            redFirstBloodVariable = False

        # For timeInterval
            # blueChampionKill, redChampionKill
            blueChampionKillVariable_20 = 0
            blueChampionKillVariable_40 = 0
            blueChampionKillVariable_60 = 0
            blueChampionKillVariable_80 = 0
            blueChampionKillVariable_100 = 0
            redChampionKillVariable_20 = 0
            redChampionKillVariable_40 = 0
            redChampionKillVariable_60 = 0
            redChampionKillVariable_80 = 0
            redChampionKillVariable_100 = 0

            # blueDragonKill, redDragonKill
            blueDragonKillVariable_20 = 0
            blueDragonKillVariable_40 = 0
            blueDragonKillVariable_60 = 0
            blueDragonKillVariable_80 = 0
            blueDragonKillVariable_100 = 0
            redDragonKillVariable_20 = 0
            redDragonKillVariable_40 = 0
            redDragonKillVariable_60 = 0
            redDragonKillVariable_80 = 0
            redDragonKillVariable_100 = 0

            # blueDragonHextechKill, redDragonHextechKill
            blueDragonHextechKillVariable_20 = 0
            blueDragonHextechKillVariable_40 = 0
            blueDragonHextechKillVariable_60 = 0
            blueDragonHextechKillVariable_80 = 0
            blueDragonHextechKillVariable_100 = 0
            redDragonHextechKillVariable_20 = 0
            redDragonHextechKillVariable_40 = 0
            redDragonHextechKillVariable_60 = 0
            redDragonHextechKillVariable_80 = 0
            redDragonHextechKillVariable_100 = 0

            # blueDragonChemtechKill, redDragonChemtechKill
            blueDragonChemtechKillVariable_20 = 0
            blueDragonChemtechKillVariable_40 = 0
            blueDragonChemtechKillVariable_60 = 0
            blueDragonChemtechKillVariable_80 = 0
            blueDragonChemtechKillVariable_100 = 0
            redDragonChemtechKillVariable_20 = 0
            redDragonChemtechKillVariable_40 = 0
            redDragonChemtechKillVariable_60 = 0
            redDragonChemtechKillVariable_80 = 0
            redDragonChemtechKillVariable_100 = 0

            # blueDragonFireKill, redDragonFireKill
            blueDragonFireKillVariable_20 = 0
            blueDragonFireKillVariable_40 = 0
            blueDragonFireKillVariable_60 = 0
            blueDragonFireKillVariable_80 = 0
            blueDragonFireKillVariable_100 = 0
            redDragonFireKillVariable_20 = 0
            redDragonFireKillVariable_40 = 0
            redDragonFireKillVariable_60 = 0
            redDragonFireKillVariable_80 = 0
            redDragonFireKillVariable_100 = 0

            # blueDragonAirKill, redDragonAirKill
            blueDragonAirKillVariable_20 = 0
            blueDragonAirKillVariable_40 = 0
            blueDragonAirKillVariable_60 = 0
            blueDragonAirKillVariable_80 = 0
            blueDragonAirKillVariable_100 = 0
            redDragonAirKillVariable_20 = 0
            redDragonAirKillVariable_40 = 0
            redDragonAirKillVariable_60 = 0
            redDragonAirKillVariable_80 = 0
            redDragonAirKillVariable_100 = 0

            # blueDragonEarthKill, redDragonEarthKill
            blueDragonEarthKillVariable_20 = 0
            blueDragonEarthKillVariable_40 = 0
            blueDragonEarthKillVariable_60 = 0
            blueDragonEarthKillVariable_80 = 0
            blueDragonEarthKillVariable_100 = 0
            redDragonEarthKillVariable_20 = 0
            redDragonEarthKillVariable_40 = 0
            redDragonEarthKillVariable_60 = 0
            redDragonEarthKillVariable_80 = 0
            redDragonEarthKillVariable_100 = 0

            # blueDragonWaterKill, redDragonWaterKill
            blueDragonWaterKillVariable_20 = 0
            blueDragonWaterKillVariable_40 = 0
            blueDragonWaterKillVariable_60 = 0
            blueDragonWaterKillVariable_80 = 0
            blueDragonWaterKillVariable_100 = 0
            redDragonWaterKillVariable_20 = 0
            redDragonWaterKillVariable_40 = 0
            redDragonWaterKillVariable_60 = 0
            redDragonWaterKillVariable_80 = 0
            redDragonWaterKillVariable_100 = 0

            # blueDragonElderKill, redDragonElderKill
            blueDragonElderKillVariable_20 = 0
            blueDragonElderKillVariable_40 = 0
            blueDragonElderKillVariable_60 = 0
            blueDragonElderKillVariable_80 = 0
            blueDragonElderKillVariable_100 = 0
            redDragonElderKillVariable_20 = 0
            redDragonElderKillVariable_40 = 0
            redDragonElderKillVariable_60 = 0
            redDragonElderKillVariable_80 = 0
            redDragonElderKillVariable_100 = 0

            # blueVoidGrubKill, redVoidGrubKill
            blueVoidGrubKillVariable_20 = 0
            blueVoidGrubKillVariable_40 = 0
            blueVoidGrubKillVariable_60 = 0
            blueVoidGrubKillVariable_80 = 0
            blueVoidGrubKillVariable_100 = 0
            redVoidGrubKillVariable_20 = 0
            redVoidGrubKillVariable_40 = 0
            redVoidGrubKillVariable_60 = 0
            redVoidGrubKillVariable_80 = 0
            redVoidGrubKillVariable_100 = 0

            # blueRiftHeraldKill, redRiftHeraldKill
            blueRiftHeraldKillVariable_20 = 0
            blueRiftHeraldKillVariable_40 = 0
            blueRiftHeraldKillVariable_60 = 0
            blueRiftHeraldKillVariable_80 = 0
            blueRiftHeraldKillVariable_100 = 0
            redRiftHeraldKillVariable_20 = 0
            redRiftHeraldKillVariable_40 = 0
            redRiftHeraldKillVariable_60 = 0
            redRiftHeraldKillVariable_80 = 0
            redRiftHeraldKillVariable_100 = 0

            # blueBaronKill, redBaronKill
            blueBaronKillVariable_20 = 0
            blueBaronKillVariable_40 = 0
            blueBaronKillVariable_60 = 0
            blueBaronKillVariable_80 = 0
            blueBaronKillVariable_100 = 0
            redBaronKillVariable_20 = 0
            redBaronKillVariable_40 = 0
            redBaronKillVariable_60 = 0
            redBaronKillVariable_80 = 0
            redBaronKillVariable_100 = 0

            # blueTowerKill, redTowerKill
            blueTowerKillVariable_20 = 0
            blueTowerKillVariable_40 = 0
            blueTowerKillVariable_60 = 0
            blueTowerKillVariable_80 = 0
            blueTowerKillVariable_100 = 0
            redTowerKillVariable_20 = 0
            redTowerKillVariable_40 = 0
            redTowerKillVariable_60 = 0
            redTowerKillVariable_80 = 0
            redTowerKillVariable_100 = 0

            # blueInhibitorKill, redInhibitorKill
            blueInhibitorKillVariable_20 = 0
            blueInhibitorKillVariable_40 = 0
            blueInhibitorKillVariable_60 = 0
            blueInhibitorKillVariable_80 = 0
            blueInhibitorKillVariable_100 = 0
            redInhibitorKillVariable_20 = 0
            redInhibitorKillVariable_40 = 0
            redInhibitorKillVariable_60 = 0
            redInhibitorKillVariable_80 = 0
            redInhibitorKillVariable_100 = 0

            # blueTotalGold, redTotalGold
            blueTotalGoldVariable_20 = 0
            blueTotalGoldVariable_40 = 0
            blueTotalGoldVariable_60 = 0
            blueTotalGoldVariable_80 = 0
            blueTotalGoldVariable_100 = 0
            redTotalGoldVariable_20 = 0
            redTotalGoldVariable_40 = 0
            redTotalGoldVariable_60 = 0
            redTotalGoldVariable_80 = 0
            redTotalGoldVariable_100 = 0

            # blueMinionsKilled, redMinionsKilled
            blueMinionsKilledVariable_20 = 0
            blueMinionsKilledVariable_40 = 0
            blueMinionsKilledVariable_60 = 0
            blueMinionsKilledVariable_80 = 0
            blueMinionsKilledVariable_100 = 0
            redMinionsKilledVariable_20 = 0
            redMinionsKilledVariable_40 = 0
            redMinionsKilledVariable_60 = 0
            redMinionsKilledVariable_80 = 0
            redMinionsKilledVariable_100 = 0

            # blueJungleMinionsKilled, redJungleMinionsKilled
            blueJungleMinionsKilledVariable_20 = 0
            blueJungleMinionsKilledVariable_40 = 0
            blueJungleMinionsKilledVariable_60 = 0
            blueJungleMinionsKilledVariable_80 = 0
            blueJungleMinionsKilledVariable_100 = 0
            redJungleMinionsKilledVariable_20 = 0
            redJungleMinionsKilledVariable_40 = 0
            redJungleMinionsKilledVariable_60 = 0
            redJungleMinionsKilledVariable_80 = 0
            redJungleMinionsKilledVariable_100 = 0

            # blueAvgPlayerLevel, redAvgPlayerLevel
            blueAvgPlayerLevelVariable_20 = 0
            blueAvgPlayerLevelVariable_40 = 0
            blueAvgPlayerLevelVariable_60 = 0
            blueAvgPlayerLevelVariable_80 = 0
            blueAvgPlayerLevelVariable_100 = 0
            redAvgPlayerLevelVariable_20 = 0
            redAvgPlayerLevelVariable_40 = 0
            redAvgPlayerLevelVariable_60 = 0
            redAvgPlayerLevelVariable_80 = 0
            redAvgPlayerLevelVariable_100 = 0

        # For time
            # blueChampionKill, redChampionKill
            blueChampionKillVariable_min10 = 0
            blueChampionKillVariable_min14 = 0
            blueChampionKillVariable_min20 = 0
            blueChampionKillVariable_min27 = 0
            blueChampionKillVariable_end = 0
            redChampionKillVariable_min10 = 0
            redChampionKillVariable_min14 = 0
            redChampionKillVariable_min20 = 0
            redChampionKillVariable_min27 = 0
            redChampionKillVariable_end = 0

            # blueDragonKill, redDragonKill
            blueDragonKillVariable_min10 = 0
            blueDragonKillVariable_min14 = 0
            blueDragonKillVariable_min20 = 0
            blueDragonKillVariable_min27 = 0
            blueDragonKillVariable_end = 0
            redDragonKillVariable_min10 = 0
            redDragonKillVariable_min14 = 0
            redDragonKillVariable_min20 = 0
            redDragonKillVariable_min27 = 0
            redDragonKillVariable_end = 0

            # blueDragonHextechKill, redDragonHextechKill
            blueDragonHextechKillVariable_min10 = 0
            blueDragonHextechKillVariable_min14 = 0
            blueDragonHextechKillVariable_min20 = 0
            blueDragonHextechKillVariable_min27 = 0
            blueDragonHextechKillVariable_end = 0
            redDragonHextechKillVariable_min10 = 0
            redDragonHextechKillVariable_min14 = 0
            redDragonHextechKillVariable_min20 = 0
            redDragonHextechKillVariable_min27 = 0
            redDragonHextechKillVariable_end = 0

            # blueDragonChemtechKill, redDragonChemtechKill
            blueDragonChemtechKillVariable_min10 = 0
            blueDragonChemtechKillVariable_min14 = 0
            blueDragonChemtechKillVariable_min20 = 0
            blueDragonChemtechKillVariable_min27 = 0
            blueDragonChemtechKillVariable_end = 0
            redDragonChemtechKillVariable_min10 = 0
            redDragonChemtechKillVariable_min14 = 0
            redDragonChemtechKillVariable_min20 = 0
            redDragonChemtechKillVariable_min27 = 0
            redDragonChemtechKillVariable_end = 0

            # blueDragonFireKill, redDragonFireKill
            blueDragonFireKillVariable_min10 = 0
            blueDragonFireKillVariable_min14 = 0
            blueDragonFireKillVariable_min20 = 0
            blueDragonFireKillVariable_min27 = 0
            blueDragonFireKillVariable_end = 0
            redDragonFireKillVariable_min10 = 0
            redDragonFireKillVariable_min14 = 0
            redDragonFireKillVariable_min20 = 0
            redDragonFireKillVariable_min27 = 0
            redDragonFireKillVariable_end = 0

            # blueDragonAirKill, redDragonAirKill
            blueDragonAirKillVariable_min10 = 0
            blueDragonAirKillVariable_min14 = 0
            blueDragonAirKillVariable_min20 = 0
            blueDragonAirKillVariable_min27 = 0
            blueDragonAirKillVariable_end = 0
            redDragonAirKillVariable_min10 = 0
            redDragonAirKillVariable_min14 = 0
            redDragonAirKillVariable_min20 = 0
            redDragonAirKillVariable_min27 = 0
            redDragonAirKillVariable_end = 0

            # blueDragonEarthKill, redDragonEarthKill
            blueDragonEarthKillVariable_min10 = 0
            blueDragonEarthKillVariable_min14 = 0
            blueDragonEarthKillVariable_min20 = 0
            blueDragonEarthKillVariable_min27 = 0
            blueDragonEarthKillVariable_end = 0
            redDragonEarthKillVariable_min10 = 0
            redDragonEarthKillVariable_min14 = 0
            redDragonEarthKillVariable_min20 = 0
            redDragonEarthKillVariable_min27 = 0
            redDragonEarthKillVariable_end = 0

            # blueDragonWaterKill, redDragonWaterKill
            blueDragonWaterKillVariable_min10 = 0
            blueDragonWaterKillVariable_min14 = 0
            blueDragonWaterKillVariable_min20 = 0
            blueDragonWaterKillVariable_min27 = 0
            blueDragonWaterKillVariable_end = 0
            redDragonWaterKillVariable_min10 = 0
            redDragonWaterKillVariable_min14 = 0
            redDragonWaterKillVariable_min20 = 0
            redDragonWaterKillVariable_min27 = 0
            redDragonWaterKillVariable_end = 0

            # blueDragonElderKill, redDragonElderKill
            blueDragonElderKillVariable_min10 = 0
            blueDragonElderKillVariable_min14 = 0
            blueDragonElderKillVariable_min20 = 0
            blueDragonElderKillVariable_min27 = 0
            blueDragonElderKillVariable_end = 0
            redDragonElderKillVariable_min10 = 0
            redDragonElderKillVariable_min14 = 0
            redDragonElderKillVariable_min20 = 0
            redDragonElderKillVariable_min27 = 0
            redDragonElderKillVariable_end = 0

            # blueVoidGrubKill, redVoidGrubKill
            blueVoidGrubKillVariable_min10 = 0
            blueVoidGrubKillVariable_min14 = 0
            blueVoidGrubKillVariable_min20 = 0
            blueVoidGrubKillVariable_min27 = 0
            blueVoidGrubKillVariable_end = 0
            redVoidGrubKillVariable_min10 = 0
            redVoidGrubKillVariable_min14 = 0
            redVoidGrubKillVariable_min20 = 0
            redVoidGrubKillVariable_min27 = 0
            redVoidGrubKillVariable_end = 0

            # blueRiftHeraldKill, redRiftHeraldKill
            blueRiftHeraldKillVariable_min10 = 0
            blueRiftHeraldKillVariable_min14 = 0
            blueRiftHeraldKillVariable_min20 = 0
            blueRiftHeraldKillVariable_min27 = 0
            blueRiftHeraldKillVariable_end = 0
            redRiftHeraldKillVariable_min10 = 0
            redRiftHeraldKillVariable_min14 = 0
            redRiftHeraldKillVariable_min20 = 0
            redRiftHeraldKillVariable_min27 = 0
            redRiftHeraldKillVariable_end = 0

            # blueBaronKill, redBaronKill
            blueBaronKillVariable_min10 = 0
            blueBaronKillVariable_min14 = 0
            blueBaronKillVariable_min20 = 0
            blueBaronKillVariable_min27 = 0
            blueBaronKillVariable_end = 0
            redBaronKillVariable_min10 = 0
            redBaronKillVariable_min14 = 0
            redBaronKillVariable_min20 = 0
            redBaronKillVariable_min27 = 0
            redBaronKillVariable_end = 0

            # blueTowerKill, redTowerKill
            blueTowerKillVariable_min10 = 0
            blueTowerKillVariable_min14 = 0
            blueTowerKillVariable_min20 = 0
            blueTowerKillVariable_min27 = 0
            blueTowerKillVariable_end = 0
            redTowerKillVariable_min10 = 0
            redTowerKillVariable_min14 = 0
            redTowerKillVariable_min20 = 0
            redTowerKillVariable_min27 = 0
            redTowerKillVariable_end = 0

            # blueInhibitorKill, redInhibitorKill
            blueInhibitorKillVariable_min10 = 0
            blueInhibitorKillVariable_min14 = 0
            blueInhibitorKillVariable_min20 = 0
            blueInhibitorKillVariable_min27 = 0
            blueInhibitorKillVariable_end = 0
            redInhibitorKillVariable_min10 = 0
            redInhibitorKillVariable_min14 = 0
            redInhibitorKillVariable_min20 = 0
            redInhibitorKillVariable_min27 = 0
            redInhibitorKillVariable_end = 0

            # blueTotalGold, redTotalGold
            blueTotalGoldVariable_min10 = 0
            blueTotalGoldVariable_min14 = 0
            blueTotalGoldVariable_min20 = 0
            blueTotalGoldVariable_min27 = 0
            blueTotalGoldVariable_end = 0
            redTotalGoldVariable_min10 = 0
            redTotalGoldVariable_min14 = 0
            redTotalGoldVariable_min20 = 0
            redTotalGoldVariable_min27 = 0
            redTotalGoldVariable_end = 0

            # blueMinionsKilled, redMinionsKilled
            blueMinionsKilledVariable_min10 = 0
            blueMinionsKilledVariable_min14 = 0
            blueMinionsKilledVariable_min20 = 0
            blueMinionsKilledVariable_min27 = 0
            blueMinionsKilledVariable_end = 0
            redMinionsKilledVariable_min10 = 0
            redMinionsKilledVariable_min14 = 0
            redMinionsKilledVariable_min20 = 0
            redMinionsKilledVariable_min27 = 0
            redMinionsKilledVariable_end = 0

            # blueJungleMinionsKilled, redJungleMinionsKilled
            blueJungleMinionsKilledVariable_min10 = 0
            blueJungleMinionsKilledVariable_min14 = 0
            blueJungleMinionsKilledVariable_min20 = 0
            blueJungleMinionsKilledVariable_min27 = 0
            blueJungleMinionsKilledVariable_end = 0
            redJungleMinionsKilledVariable_min10 = 0
            redJungleMinionsKilledVariable_min14 = 0
            redJungleMinionsKilledVariable_min20 = 0
            redJungleMinionsKilledVariable_min27 = 0
            redJungleMinionsKilledVariable_end = 0

            # blueAvgPlayerLevel, redAvgPlayerLevel
            blueAvgPlayerLevelVariable_min10 = 0
            blueAvgPlayerLevelVariable_min14 = 0
            blueAvgPlayerLevelVariable_min20 = 0
            blueAvgPlayerLevelVariable_min27 = 0
            blueAvgPlayerLevelVariable_end = 0
            redAvgPlayerLevelVariable_min10 = 0
            redAvgPlayerLevelVariable_min14 = 0
            redAvgPlayerLevelVariable_min20 = 0
            redAvgPlayerLevelVariable_min27 = 0
            redAvgPlayerLevelVariable_end = 0


            print(f'Current number: {match_ids.index(current_game_id) + 1}')
            print(f'Current match id: {current_game_id}')

            if current_game_id[:3] in ['BR1', 'LA1', 'LA2', 'NA1']:
                region = 'americas'
            elif current_game_id[:4] in ['EUN1', 'EUW1'] or current_game_id[:2] in ['RU', 'TR']:
                region = 'europe'
            elif current_game_id[:2] in ['JP', 'KR']:
                region = 'asia'
            elif current_game_id[:3] in ['OC1', 'PH2', 'SG2', 'TH2', 'VN2']:
                region = 'sea'

            print(f'Current region: {region}')
            # Prevent API rate limit
            api_call_end_time = time.time()
            api_call_runtime = api_call_end_time - api_call_start_time
            print(f'API call runtime: {api_call_runtime}')
            if api_call_runtime < 1.2:
                time.sleep(1.25 - api_call_runtime)
                print(f'Sleeping for {1.2 - api_call_runtime} seconds')

            game_timeline = get_timeline_by_game_id(region, current_game_id, API_KEY)
            api_call_start_time = time.time()

        # Code: fullTimeMS_timeInterval
            fullTimeMSVariable = game_timeline['info']['frames'][-1]['events'][-1]['timestamp']
            minutesPassed = [10, 14, 20, 27, fullTimeMSVariable/60000]

        # Code: blueWin, redWin
            winningTeam = game_timeline['info']['frames'][-1]['events'][-1]['winningTeam']
            if winningTeam == 100:
                blueWinVariable = True
                redWinVariable = False
            else:
                blueWinVariable = False
                redWinVariable = True
            
        # Code: blueFirstBlood, redFirstBlood
            found = False
            for i in game_timeline['info']['frames']:
                for j in i['events']:
                    if 'killType' in j:
                        if j['killType'] == 'KILL_FIRST_BLOOD':
                            if j['killerId'] in blueTeamPlayerIds:
                                blueFirstBloodVariable = True
                                redFirstBloodVariable = False
                            if j['killerId'] in redTeamPlayerIds:
                                blueFirstBloodVariable = False
                                redFirstBloodVariable = True
                            found = True
                            break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break

        # Code: rest 36 variables
            for timeInterval in timeIntervalPercentages:
                lastTimeStamp = fullTimeMSVariable * timeInterval

        # Code: timeStamp
                if timeInterval == 0.2:
                    timeStamp_20.append(int(lastTimeStamp))
                elif timeInterval == 0.4:
                    timeStamp_40.append(int(lastTimeStamp))
                elif timeInterval == 0.6:
                    timeStamp_60.append(int(lastTimeStamp))
                elif timeInterval == 0.8:
                    timeStamp_80.append(int(lastTimeStamp))
                elif timeInterval == 1:
                    timeStamp.append(int(lastTimeStamp))
                
                exitLoop = False
                for frame in game_timeline['info']['frames']:
                    for event in frame['events']:

        # Code: blueChampionKill, redChampionKill
                        if event['type'] == 'CHAMPION_KILL' and event['timestamp'] <= lastTimeStamp:
                            if event['killerId'] in blueTeamPlayerIds:
                                if timeInterval == 0.2:
                                    blueChampionKillVariable_20 += 1
                                elif timeInterval == 0.4:
                                    blueChampionKillVariable_40 += 1
                                elif timeInterval == 0.6:
                                    blueChampionKillVariable_60 += 1
                                elif timeInterval == 0.8:
                                    blueChampionKillVariable_80 += 1
                                elif timeInterval == 1:
                                    blueChampionKillVariable_100 += 1
                            elif event['killerId'] in redTeamPlayerIds:
                                if timeInterval == 0.2:
                                    redChampionKillVariable_20 += 1
                                elif timeInterval == 0.4:
                                    redChampionKillVariable_40 += 1
                                elif timeInterval == 0.6:
                                    redChampionKillVariable_60 += 1
                                elif timeInterval == 0.8:
                                    redChampionKillVariable_80 += 1
                                elif timeInterval == 1:
                                    redChampionKillVariable_100 += 1
        # Code: blueDragonKill, redDragonKill, blueDragonHextechKill, redDragonHextechKill, blueDragonChemtechKill, redDragonChemtechKill, blueDragonFireKill, redDragonFireKill, blueDragonAirKill, redDragonAirKill, blueDragonEarthKill, redDragonEarthKill, blueDragonWaterKill, redDragonWaterKill, blueDragonElderKill, redDragonElderKill, blueVoidGrubKill, redVoidGrubKill, blueRiftHeraldKill, redRiftHeraldKill, blueBaronKill, redBaronKill
                        elif event['type'] == 'ELITE_MONSTER_KILL' and event['timestamp'] <= lastTimeStamp:
        # Code: blue team
                            if event['monsterType'] == 'DRAGON':
        # Code: blueDragonKill
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        blueDragonKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        blueDragonKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        blueDragonKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        blueDragonKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        blueDragonKillVariable_100 += 1
        # Code: blueDragonHextechKill
                                    if event['monsterSubType'] == 'HEXTECH_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonHextechKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonHextechKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonHextechKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonHextechKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonHextechKillVariable_100 += 1
        # Code: blueDragonChemtechKill
                                    if event['monsterSubType'] == 'CHEMTECH_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonChemtechKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonChemtechKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonChemtechKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonChemtechKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonChemtechKillVariable_100 += 1
        # Code: blueDragonFireKill
                                    if event['monsterSubType'] == 'FIRE_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonFireKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonFireKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonFireKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonFireKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonFireKillVariable_100 += 1
        # Code: blueDragonAirKill
                                    if event['monsterSubType'] == 'AIR_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonAirKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonAirKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonAirKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonAirKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonAirKillVariable_100 += 1
        # Code: blueDragonEarthKill
                                    if event['monsterSubType'] == 'EARTH_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonEarthKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonEarthKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonEarthKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonEarthKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonEarthKillVariable_100 += 1
        # Code: blueDragonWaterKill
                                    if event['monsterSubType'] == 'WATER_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonWaterKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonWaterKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonWaterKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonWaterKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonWaterKillVariable_100 += 1
        # Code: blueDragonElderKill
                                    if event['monsterSubType'] == 'ELDER_DRAGON':
                                        if timeInterval == 0.2:
                                            blueDragonElderKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            blueDragonElderKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            blueDragonElderKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            blueDragonElderKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            blueDragonElderKillVariable_100 += 1
        # Code: blueVoidGrubKill
                            elif event['monsterType'] == 'HORDE':
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        blueVoidGrubKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        blueVoidGrubKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        blueVoidGrubKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        blueVoidGrubKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        blueVoidGrubKillVariable_100 += 1
        # Code: blueRiftHeraldKill
                            elif event['monsterType'] == 'RIFTHERALD':
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        blueRiftHeraldKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        blueRiftHeraldKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        blueRiftHeraldKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        blueRiftHeraldKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        blueRiftHeraldKillVariable_100 += 1
        # Code: blueBaronKill
                            elif event['monsterType'] == 'BARON_NASHOR':
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        blueBaronKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        blueBaronKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        blueBaronKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        blueBaronKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        blueBaronKillVariable_100 += 1
        # Code: red team
                            if event['monsterType'] == 'DRAGON':
        # Code: redDragonKill
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        redDragonKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        redDragonKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        redDragonKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        redDragonKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        redDragonKillVariable_100 += 1
        # Code: redDragonHextechKill
                                    if event['monsterSubType'] == 'HEXTECH_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonHextechKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonHextechKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonHextechKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonHextechKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonHextechKillVariable_100 += 1
        # Code: redDragonChemtechKill
                                    if event['monsterSubType'] == 'CHEMTECH_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonChemtechKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonChemtechKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonChemtechKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonChemtechKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonChemtechKillVariable_100 += 1
        # Code: redDragonFireKill
                                    if event['monsterSubType'] == 'FIRE_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonFireKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonFireKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonFireKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonFireKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonFireKillVariable_100 += 1
        # Code: redDragonAirKill
                                    if event['monsterSubType'] == 'AIR_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonAirKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonAirKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonAirKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonAirKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonAirKillVariable_100 += 1
        # Code: redDragonEarthKill
                                    if event['monsterSubType'] == 'EARTH_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonEarthKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonEarthKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonEarthKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonEarthKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonEarthKillVariable_100 += 1
        # Code: redDragonWaterKill
                                    if event['monsterSubType'] == 'WATER_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonWaterKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonWaterKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonWaterKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonWaterKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonWaterKillVariable_100 += 1
        # Code: redDragonElderKill
                                    if event['monsterSubType'] == 'ELDER_DRAGON':
                                        if timeInterval == 0.2:
                                            redDragonElderKillVariable_20 += 1
                                        elif timeInterval == 0.4:
                                            redDragonElderKillVariable_40 += 1
                                        elif timeInterval == 0.6:
                                            redDragonElderKillVariable_60 += 1
                                        elif timeInterval == 0.8:
                                            redDragonElderKillVariable_80 += 1
                                        elif timeInterval == 1:
                                            redDragonElderKillVariable_100 += 1
        # Code: redVoidGrubKill
                            elif event['monsterType'] == 'HORDE':
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        redVoidGrubKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        redVoidGrubKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        redVoidGrubKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        redVoidGrubKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        redVoidGrubKillVariable_100 += 1
        # Code: redRiftHeraldKill
                            elif event['monsterType'] == 'RIFTHERALD':
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        redRiftHeraldKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        redRiftHeraldKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        redRiftHeraldKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        redRiftHeraldKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        redRiftHeraldKillVariable_100 += 1
        # Code: redBaronKill
                            elif event['monsterType'] == 'BARON_NASHOR':
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 0.2:
                                        redBaronKillVariable_20 += 1
                                    elif timeInterval == 0.4:
                                        redBaronKillVariable_40 += 1
                                    elif timeInterval == 0.6:
                                        redBaronKillVariable_60 += 1
                                    elif timeInterval == 0.8:
                                        redBaronKillVariable_80 += 1
                                    elif timeInterval == 1:
                                        redBaronKillVariable_100 += 1

        # Code: blueTowerKill, redTowerKill, blueInhibitorKill, redInhibitorKill
                        if event['type'] == 'BUILDING_KILL' and event['timestamp'] <= lastTimeStamp:
        # Code: blueTowerKill, redTowerKill
                            if event['buildingType'] == 'TOWER_BUILDING' and event['teamId'] == 200:
                                if timeInterval == 0.2:
                                    blueTowerKillVariable_20 += 1
                                elif timeInterval == 0.4:
                                    blueTowerKillVariable_40 += 1
                                elif timeInterval == 0.6:
                                    blueTowerKillVariable_60 += 1
                                elif timeInterval == 0.8:
                                    blueTowerKillVariable_80 += 1
                                elif timeInterval == 1:
                                    blueTowerKillVariable_100 += 1

                            elif event['buildingType'] == 'TOWER_BUILDING' and event['teamId'] == 100:
                                if timeInterval == 0.2:
                                    redTowerKillVariable_20 += 1
                                elif timeInterval == 0.4:
                                    redTowerKillVariable_40 += 1
                                elif timeInterval == 0.6:
                                    redTowerKillVariable_60 += 1
                                elif timeInterval == 0.8:
                                    redTowerKillVariable_80 += 1
                                elif timeInterval == 1:
                                    redTowerKillVariable_100 += 1
        # Code: blueInhibitorKill, redInhibitorKill
                            elif event['buildingType'] == 'INHIBITOR_BUILDING' and event['teamId'] == 200:
                                if timeInterval == 0.2:
                                    blueInhibitorKillVariable_20 += 1
                                elif timeInterval == 0.4:
                                    blueInhibitorKillVariable_40 += 1
                                elif timeInterval == 0.6:
                                    blueInhibitorKillVariable_60 += 1
                                elif timeInterval == 0.8:
                                    blueInhibitorKillVariable_80 += 1
                                elif timeInterval == 1:
                                    blueInhibitorKillVariable_100 += 1

                            elif event['buildingType'] == 'INHIBITOR_BUILDING' and event['teamId'] == 100:
                                if timeInterval == 0.2:
                                    redInhibitorKillVariable_20 += 1
                                elif timeInterval == 0.4:
                                    redInhibitorKillVariable_40 += 1
                                elif timeInterval == 0.6:
                                    redInhibitorKillVariable_60 += 1
                                elif timeInterval == 0.8:
                                    redInhibitorKillVariable_80 += 1
                                elif timeInterval == 1:
                                    blueInhibitorKillVariable_100 += 1
        
        # Code: blueTotalGold, redTotalGold, blueMinionsKilled, redMinionsKilled, blueJungleMinionsKilled, redJungleMinionsKilled, blueAvgPlayerLevel, redAvgPlayerLevel
                    currentTimeStamp = frame['timestamp']
                    if currentTimeStamp >= lastTimeStamp:
                        if timeInterval == 0.2:
                            for currentPlayer in frame['participantFrames']:
                                if int(currentPlayer) in blueTeamPlayerIds:
                                    blueTotalGoldVariable_20 += frame['participantFrames'][currentPlayer]['totalGold']
                                    blueMinionsKilledVariable_20 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    blueJungleMinionsKilledVariable_20 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    blueAvgPlayerLevelVariable_20 += frame['participantFrames'][currentPlayer]['level']
                                elif int(currentPlayer) in redTeamPlayerIds:
                                    redTotalGoldVariable_20 += frame['participantFrames'][currentPlayer]['totalGold']
                                    redMinionsKilledVariable_20 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    redJungleMinionsKilledVariable_20 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    redAvgPlayerLevelVariable_20 += frame['participantFrames'][currentPlayer]['level']
                            exitLoop = True
                        elif timeInterval == 0.4:
                            for currentPlayer in frame['participantFrames']:
                                if int(currentPlayer) in blueTeamPlayerIds:
                                    blueTotalGoldVariable_40 += frame['participantFrames'][currentPlayer]['totalGold']
                                    blueMinionsKilledVariable_40 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    blueJungleMinionsKilledVariable_40 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    blueAvgPlayerLevelVariable_40 += frame['participantFrames'][currentPlayer]['level']
                                elif int(currentPlayer) in redTeamPlayerIds:
                                    redTotalGoldVariable_40 += frame['participantFrames'][currentPlayer]['totalGold']
                                    redMinionsKilledVariable_40 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    redJungleMinionsKilledVariable_40 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    redAvgPlayerLevelVariable_40 += frame['participantFrames'][currentPlayer]['level']
                            exitLoop = True
                        elif timeInterval == 0.6:
                            for currentPlayer in frame['participantFrames']:
                                if int(currentPlayer) in blueTeamPlayerIds:
                                    blueTotalGoldVariable_60 += frame['participantFrames'][currentPlayer]['totalGold']
                                    blueMinionsKilledVariable_60 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    blueJungleMinionsKilledVariable_60 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    blueAvgPlayerLevelVariable_60 += frame['participantFrames'][currentPlayer]['level']
                                elif int(currentPlayer) in redTeamPlayerIds:
                                    redTotalGoldVariable_60 += frame['participantFrames'][currentPlayer]['totalGold']
                                    redMinionsKilledVariable_60 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    redJungleMinionsKilledVariable_60 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    redAvgPlayerLevelVariable_60 += frame['participantFrames'][currentPlayer]['level']
                            exitLoop = True
                        elif timeInterval == 0.8:
                            for currentPlayer in frame['participantFrames']:
                                if int(currentPlayer) in blueTeamPlayerIds:
                                    blueTotalGoldVariable_80 += frame['participantFrames'][currentPlayer]['totalGold']
                                    blueMinionsKilledVariable_80 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    blueJungleMinionsKilledVariable_80 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    blueAvgPlayerLevelVariable_80 += frame['participantFrames'][currentPlayer]['level']
                                elif int(currentPlayer) in redTeamPlayerIds:
                                    redTotalGoldVariable_80 += frame['participantFrames'][currentPlayer]['totalGold']
                                    redMinionsKilledVariable_80 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    redJungleMinionsKilledVariable_80 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    redAvgPlayerLevelVariable_80 += frame['participantFrames'][currentPlayer]['level']
                            exitLoop = True
                        elif timeInterval == 1:
                            for currentPlayer in frame['participantFrames']:
                                if int(currentPlayer) in blueTeamPlayerIds:
                                    blueTotalGoldVariable_end += frame['participantFrames'][currentPlayer]['totalGold']
                                    blueMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    blueJungleMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    blueAvgPlayerLevelVariable_end += frame['participantFrames'][currentPlayer]['level']
                                elif int(currentPlayer) in redTeamPlayerIds:
                                    redTotalGoldVariable_end += frame['participantFrames'][currentPlayer]['totalGold']
                                    redMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['minionsKilled']
                                    redJungleMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                    redAvgPlayerLevelVariable_end += frame['participantFrames'][currentPlayer]['level']
                            exitLoop = True
                    if exitLoop:
                        break



    # Variablemodification for new_dataset_{timeInterval}.csv

        # General variables for new_dataset_{timeInterval}.csv

            # Column1_timeInterval (fixed)
            Column1_timeInterval.append(column1)

            # matchID_timeInterval (fixed)
            matchID_timeInterval.append(current_game_id)

            # fullTimeMS_timeInterval (fixed)
            fullTimeMS_timeInterval.append(fullTimeMSVariable)

        # Variables for new_dataset_{timeInterval}.csv

            # blueChampionKill_timeInterval
            blueChampionKill.append(blueChampionKillVariable_100)
            blueChampionKill_20.append(blueChampionKillVariable_20)
            blueChampionKill_40.append(blueChampionKillVariable_40)
            blueChampionKill_60.append(blueChampionKillVariable_60)
            blueChampionKill_80.append(blueChampionKillVariable_80)

            # blueFirstBlood_timeInterval (fixed)
            blueFirstBlood.append(blueFirstBloodVariable)

            # blueDragonKill_timeInterval
            blueDragonKill.append(blueDragonKillVariable_100)
            blueDragonKill_20.append(blueDragonKillVariable_20)
            blueDragonKill_40.append(blueDragonKillVariable_40)
            blueDragonKill_60.append(blueDragonKillVariable_60)
            blueDragonKill_80.append(blueDragonKillVariable_80)

            # blueDragonHextechKill_timeInterval
            blueDragonHextechKill.append(blueDragonHextechKillVariable_100)
            blueDragonHextechKill_20.append(blueDragonHextechKillVariable_20)
            blueDragonHextechKill_40.append(blueDragonHextechKillVariable_40)
            blueDragonHextechKill_60.append(blueDragonHextechKillVariable_60)
            blueDragonHextechKill_80.append(blueDragonHextechKillVariable_80)

            # blueDragonChemtechKill_timeInterval
            blueDragonChemtechKill.append(blueDragonChemtechKillVariable_100)
            blueDragonChemtechKill_20.append(blueDragonChemtechKillVariable_20)
            blueDragonChemtechKill_40.append(blueDragonChemtechKillVariable_40)
            blueDragonChemtechKill_60.append(blueDragonChemtechKillVariable_60)
            blueDragonChemtechKill_80.append(blueDragonChemtechKillVariable_80)

            # blueDragonFireKill_timeInterval
            blueDragonFireKill.append(blueDragonFireKillVariable_100)
            blueDragonFireKill_20.append(blueDragonFireKillVariable_20)
            blueDragonFireKill_40.append(blueDragonFireKillVariable_40)
            blueDragonFireKill_60.append(blueDragonFireKillVariable_60)
            blueDragonFireKill_80.append(blueDragonFireKillVariable_80)

            # blueDragonAirKill_timeInterval
            blueDragonAirKill.append(blueDragonAirKillVariable_100)
            blueDragonAirKill_20.append(blueDragonAirKillVariable_20)
            blueDragonAirKill_40.append(blueDragonAirKillVariable_40)
            blueDragonAirKill_60.append(blueDragonAirKillVariable_60)
            blueDragonAirKill_80.append(blueDragonAirKillVariable_80)

            # blueDragonEarthKill_timeInterval
            blueDragonEarthKill.append(blueDragonEarthKillVariable_100)
            blueDragonEarthKill_20.append(blueDragonEarthKillVariable_20)
            blueDragonEarthKill_40.append(blueDragonEarthKillVariable_40)
            blueDragonEarthKill_60.append(blueDragonEarthKillVariable_60)
            blueDragonEarthKill_80.append(blueDragonEarthKillVariable_80)

            # blueDragonWaterKill_timeInterval
            blueDragonWaterKill.append(blueDragonWaterKillVariable_100)
            blueDragonWaterKill_20.append(blueDragonWaterKillVariable_20)
            blueDragonWaterKill_40.append(blueDragonWaterKillVariable_40)
            blueDragonWaterKill_60.append(blueDragonWaterKillVariable_60)
            blueDragonWaterKill_80.append(blueDragonWaterKillVariable_80)

            # blueDragonElderKill_timeInterval
            blueDragonElderKill.append(blueDragonElderKillVariable_100)
            blueDragonElderKill_20.append(blueDragonElderKillVariable_20)
            blueDragonElderKill_40.append(blueDragonElderKillVariable_40)
            blueDragonElderKill_60.append(blueDragonElderKillVariable_60)
            blueDragonElderKill_80.append(blueDragonElderKillVariable_80)

            # blueVoidGrubKill_timeInterval
            blueVoidGrubKill.append(blueVoidGrubKillVariable_100)
            blueVoidGrubKill_20.append(blueVoidGrubKillVariable_20)
            blueVoidGrubKill_40.append(blueVoidGrubKillVariable_40)
            blueVoidGrubKill_60.append(blueVoidGrubKillVariable_60)
            blueVoidGrubKill_80.append(blueVoidGrubKillVariable_80)

            # blueRiftHeraldKill_timeInterval
            blueRiftHeraldKill.append(blueRiftHeraldKillVariable_100)
            blueRiftHeraldKill_20.append(blueRiftHeraldKillVariable_20)
            blueRiftHeraldKill_40.append(blueRiftHeraldKillVariable_40)
            blueRiftHeraldKill_60.append(blueRiftHeraldKillVariable_60)
            blueRiftHeraldKill_80.append(blueRiftHeraldKillVariable_80)

            # blueBaronKill_timeInterval
            blueBaronKill.append(blueBaronKillVariable_100)
            blueBaronKill_20.append(blueBaronKillVariable_20)
            blueBaronKill_40.append(blueBaronKillVariable_40)
            blueBaronKill_60.append(blueBaronKillVariable_60)
            blueBaronKill_80.append(blueBaronKillVariable_80)

            # blueTowerKill_timeInterval
            blueTowerKill.append(blueTowerKillVariable_100)
            blueTowerKill_20.append(blueTowerKillVariable_20)
            blueTowerKill_40.append(blueTowerKillVariable_40)
            blueTowerKill_60.append(blueTowerKillVariable_60)
            blueTowerKill_80.append(blueTowerKillVariable_80)

            # blueInhibitorKill_timeInterval
            blueInhibitorKill.append(blueInhibitorKillVariable_100)
            blueInhibitorKill_20.append(blueInhibitorKillVariable_20)
            blueInhibitorKill_40.append(blueInhibitorKillVariable_40)
            blueInhibitorKill_60.append(blueInhibitorKillVariable_60)
            blueInhibitorKill_80.append(blueInhibitorKillVariable_80)

            # blueTotalGold_timeInterval
            blueTotalGold.append(blueTotalGoldVariable_end)
            blueTotalGold_20.append(blueTotalGoldVariable_20)
            blueTotalGold_40.append(blueTotalGoldVariable_40)
            blueTotalGold_60.append(blueTotalGoldVariable_60)
            blueTotalGold_80.append(blueTotalGoldVariable_80)

            # blueMinionsKilled_timeInterval
            blueMinionsKilled.append(blueMinionsKilledVariable_end)
            blueMinionsKilled_20.append(blueMinionsKilledVariable_20)
            blueMinionsKilled_40.append(blueMinionsKilledVariable_40)
            blueMinionsKilled_60.append(blueMinionsKilledVariable_60)
            blueMinionsKilled_80.append(blueMinionsKilledVariable_80)

            # blueJungleMinionsKilled_timeInterval
            blueJungleMinionsKilled.append(blueJungleMinionsKilledVariable_end)
            blueJungleMinionsKilled_20.append(blueJungleMinionsKilledVariable_20)
            blueJungleMinionsKilled_40.append(blueJungleMinionsKilledVariable_40)
            blueJungleMinionsKilled_60.append(blueJungleMinionsKilledVariable_60)
            blueJungleMinionsKilled_80.append(blueJungleMinionsKilledVariable_80)

            # blueAvgPlayerLevel_timeInterval
            blueAvgPlayerLevel.append(blueAvgPlayerLevelVariable_end)
            blueAvgPlayerLevel_20.append(blueAvgPlayerLevelVariable_20)
            blueAvgPlayerLevel_40.append(blueAvgPlayerLevelVariable_40)
            blueAvgPlayerLevel_60.append(blueAvgPlayerLevelVariable_60)
            blueAvgPlayerLevel_80.append(blueAvgPlayerLevelVariable_80)

            # blueWin_timeInterval (fixed)
            blueWin.append(blueWinVariable)

            # redChampionKill_timeInterval
            redChampionKill.append(redChampionKillVariable_100)
            redChampionKill_20.append(redChampionKillVariable_20)
            redChampionKill_40.append(redChampionKillVariable_40)
            redChampionKill_60.append(redChampionKillVariable_60)
            redChampionKill_80.append(redChampionKillVariable_80)

            # redFirstBlood_timeInterval (fixed)
            redFirstBlood.append(redFirstBloodVariable)

            # redDragonKill_timeInterval
            redDragonKill.append(redDragonKillVariable_100)
            redDragonKill_20.append(redDragonKillVariable_20)
            redDragonKill_40.append(redDragonKillVariable_40)
            redDragonKill_60.append(redDragonKillVariable_60)
            redDragonKill_80.append(redDragonKillVariable_80)

            # redDragonHextechKill_timeInterval
            redDragonHextechKill.append(redDragonHextechKillVariable_100)
            redDragonHextechKill_20.append(redDragonHextechKillVariable_20)
            redDragonHextechKill_40.append(redDragonHextechKillVariable_40)
            redDragonHextechKill_60.append(redDragonHextechKillVariable_60)
            redDragonHextechKill_80.append(redDragonHextechKillVariable_80)

            # redDragonChemtechKill_timeInterval
            redDragonChemtechKill.append(redDragonChemtechKillVariable_100)
            redDragonChemtechKill_20.append(redDragonChemtechKillVariable_20)
            redDragonChemtechKill_40.append(redDragonChemtechKillVariable_40)
            redDragonChemtechKill_60.append(redDragonChemtechKillVariable_60)
            redDragonChemtechKill_80.append(redDragonChemtechKillVariable_80)

            # redDragonFireKill_timeInterval
            redDragonFireKill.append(redDragonFireKillVariable_100)
            redDragonFireKill_20.append(redDragonFireKillVariable_20)
            redDragonFireKill_40.append(redDragonFireKillVariable_40)
            redDragonFireKill_60.append(redDragonFireKillVariable_60)
            redDragonFireKill_80.append(redDragonFireKillVariable_80)

            # redDragonAirKill_timeInterval
            redDragonAirKill.append(redDragonAirKillVariable_100)
            redDragonAirKill_20.append(redDragonAirKillVariable_20)
            redDragonAirKill_40.append(redDragonAirKillVariable_40)
            redDragonAirKill_60.append(redDragonAirKillVariable_60)
            redDragonAirKill_80.append(redDragonAirKillVariable_80)

            # redDragonEarthKill_timeInterval
            redDragonEarthKill.append(redDragonEarthKillVariable_100)
            redDragonEarthKill_20.append(redDragonEarthKillVariable_20)
            redDragonEarthKill_40.append(redDragonEarthKillVariable_40)
            redDragonEarthKill_60.append(redDragonEarthKillVariable_60)
            redDragonEarthKill_80.append(redDragonEarthKillVariable_80)

            # redDragonWaterKill_timeInterval
            redDragonWaterKill.append(redDragonWaterKillVariable_100)
            redDragonWaterKill_20.append(redDragonWaterKillVariable_20)
            redDragonWaterKill_40.append(redDragonWaterKillVariable_40)
            redDragonWaterKill_60.append(redDragonWaterKillVariable_60)
            redDragonWaterKill_80.append(redDragonWaterKillVariable_80)

            # redDragonElderKill_timeInterval
            redDragonElderKill.append(redDragonElderKillVariable_100)
            redDragonElderKill_20.append(redDragonElderKillVariable_20)
            redDragonElderKill_40.append(redDragonElderKillVariable_40)
            redDragonElderKill_60.append(redDragonElderKillVariable_60)
            redDragonElderKill_80.append(redDragonElderKillVariable_80)

            # redVoidGrubKill_timeInterval
            redVoidGrubKill.append(redVoidGrubKillVariable_100)
            redVoidGrubKill_20.append(redVoidGrubKillVariable_20)
            redVoidGrubKill_40.append(redVoidGrubKillVariable_40)
            redVoidGrubKill_60.append(redVoidGrubKillVariable_60)
            redVoidGrubKill_80.append(redVoidGrubKillVariable_80)

            # redRiftHeraldKill_timeInterval
            redRiftHeraldKill.append(redRiftHeraldKillVariable_100)
            redRiftHeraldKill_20.append(redRiftHeraldKillVariable_20)
            redRiftHeraldKill_40.append(redRiftHeraldKillVariable_40)
            redRiftHeraldKill_60.append(redRiftHeraldKillVariable_60)
            redRiftHeraldKill_80.append(redRiftHeraldKillVariable_80)

            # redBaronKill_timeInterval
            redBaronKill.append(redBaronKillVariable_100)
            redBaronKill_20.append(redBaronKillVariable_20)
            redBaronKill_40.append(redBaronKillVariable_40)
            redBaronKill_60.append(redBaronKillVariable_60)
            redBaronKill_80.append(redBaronKillVariable_80)

            # redTowerKill_timeInterval
            redTowerKill.append(redTowerKillVariable_100)
            redTowerKill_20.append(redTowerKillVariable_20)
            redTowerKill_40.append(redTowerKillVariable_40)
            redTowerKill_60.append(redTowerKillVariable_60)
            redTowerKill_80.append(redTowerKillVariable_80)

            # redInhibitorKill_timeInterval
            redInhibitorKill.append(redInhibitorKillVariable_100)
            redInhibitorKill_20.append(redInhibitorKillVariable_20)
            redInhibitorKill_40.append(redInhibitorKillVariable_40)
            redInhibitorKill_60.append(redInhibitorKillVariable_60)
            redInhibitorKill_80.append(redInhibitorKillVariable_80)

            # redTotalGold_timeInterval
            redTotalGold.append(redTotalGoldVariable_end)
            redTotalGold_20.append(redTotalGoldVariable_20)
            redTotalGold_40.append(redTotalGoldVariable_40)
            redTotalGold_60.append(redTotalGoldVariable_60)
            redTotalGold_80.append(redTotalGoldVariable_80)

            # redMinionsKilled_timeInterval
            redMinionsKilled.append(redMinionsKilledVariable_end)
            redMinionsKilled_20.append(redMinionsKilledVariable_20)
            redMinionsKilled_40.append(redMinionsKilledVariable_40)
            redMinionsKilled_60.append(redMinionsKilledVariable_60)
            redMinionsKilled_80.append(redMinionsKilledVariable_80)

            # redJungleMinionsKilled_timeInterval
            redJungleMinionsKilled.append(redJungleMinionsKilledVariable_end)
            redJungleMinionsKilled_20.append(redJungleMinionsKilledVariable_20)
            redJungleMinionsKilled_40.append(redJungleMinionsKilledVariable_40)
            redJungleMinionsKilled_60.append(redJungleMinionsKilledVariable_60)
            redJungleMinionsKilled_80.append(redJungleMinionsKilledVariable_80)

            # redAvgPlayerLevel_timeInterval
            redAvgPlayerLevel.append(redAvgPlayerLevelVariable_end)
            redAvgPlayerLevel_20.append(redAvgPlayerLevelVariable_20)
            redAvgPlayerLevel_40.append(redAvgPlayerLevelVariable_40)
            redAvgPlayerLevel_60.append(redAvgPlayerLevelVariable_60)
            redAvgPlayerLevel_80.append(redAvgPlayerLevelVariable_80)

            # redWin_timeInterval (fixed)
            redWin.append(redWinVariable)



    # Variablemodification for new_dataset_min{time}.csv
            if fullTimeMSVariable > 1620000:

                # Code: rest 36 variables
                for minuteLimit in minutesPassed:
                    # minutesPassed = [10, 14, 20, 27, fullTimeMSVariable/60000]
                    lastMinute = minuteLimit * 60000

                # Code: timeStamp
                    if minuteLimit == 10:
                        timeStamp_min10.append(int(lastMinute))
                    elif minuteLimit == 14:
                        timeStamp_min14.append(int(lastMinute))
                    elif minuteLimit == 20:
                        timeStamp_min20.append(int(lastMinute))
                    elif minuteLimit == 27:
                        timeStamp_min27.append(int(lastMinute))
                    elif minuteLimit == fullTimeMSVariable/60000:
                        timeStamp_end.append(int(lastMinute))

                    exitLoop_time = False
                    for frame in game_timeline['info']['frames']:
                        for event in frame['events']:

                            # Code: blueChampionKill_time, redChampionKill_time
                            if event['type'] == 'CHAMPION_KILL' and event['timestamp'] <= lastMinute:
                                if event['killerId'] in blueTeamPlayerIds:
                                    if minuteLimit == 10:
                                        blueChampionKillVariable_min10 += 1
                                    elif minuteLimit == 14:
                                        blueChampionKillVariable_min14 += 1
                                    elif minuteLimit == 20:
                                        blueChampionKillVariable_min20 += 1
                                    elif minuteLimit == 27:
                                        blueChampionKillVariable_min27 += 1
                                    elif minuteLimit == fullTimeMSVariable/60000:
                                        blueChampionKillVariable_end += 1
                                elif event['killerId'] in redTeamPlayerIds:
                                    if lastMinute == 10:
                                        redChampionKillVariable_min10 += 1
                                    elif minuteLimit == 14:
                                        redChampionKillVariable_min14 += 1
                                    elif minuteLimit == 20:
                                        redChampionKillVariable_min20 += 1
                                    elif minuteLimit == 27:
                                        redChampionKillVariable_min27 += 1
                                    elif minuteLimit == fullTimeMSVariable/60000:
                                        redChampionKillVariable_end += 1
                            
                            # Code: ELITE_MONSTER_KILL
                            elif event['type'] == 'ELITE_MONSTER_KILL' and event['timestamp'] <= lastMinute:
                            # Code: blue team
                                if event['monsterType'] == 'DRAGON':
                            # Code: blueDragonKill_time
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            blueDragonKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            blueDragonKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            blueDragonKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            blueDragonKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            blueDragonKillVariable_end += 1
                            # Code: blueDragonHextechKill_time
                                        if event['monsterSubType'] == 'HEXTECH_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonHextechKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonHextechKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonHextechKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonHextechKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonHextechKillVariable_end += 1
                            # Code: blueDragonChemtechKill_time
                                        if event['monsterSubType'] == 'CHEMTECH_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonChemtechKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonChemtechKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonChemtechKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonChemtechKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonChemtechKillVariable_end += 1
                            # Code: blueDragonFireKill_time
                                        if event['monsterSubType'] == 'FIRE_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonFireKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonFireKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonFireKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonFireKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonFireKillVariable_end += 1
                            # Code: blueDragonAirKill_time
                                        if event['monsterSubType'] == 'AIR_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonAirKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonAirKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonAirKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonAirKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonAirKillVariable_end += 1
                            # Code: blueDragonEarthKill_time
                                        if event['monsterSubType'] == 'EARTH_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonEarthKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonEarthKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonEarthKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonEarthKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonEarthKillVariable_end += 1
                            # Code: blueDragonWaterKill_time
                                        if event['monsterSubType'] == 'WATER_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonWaterKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonWaterKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonWaterKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonWaterKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonWaterKillVariable_end += 1
                            # Code: blueDragonElderKill_time
                                        if event['monsterSubType'] == 'ELDER_DRAGON':
                                            if minuteLimit == 10:
                                                blueDragonElderKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                blueDragonElderKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                blueDragonElderKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                blueDragonElderKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                blueDragonElderKillVariable_end += 1
                            # Code: blueVoidGrubKill_time
                                elif event['monsterType'] == 'HORDE':
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            blueVoidGrubKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            blueVoidGrubKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            blueVoidGrubKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            blueVoidGrubKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            blueVoidGrubKillVariable_end += 1
                            # Code: blueRiftHeraldKill_time
                                elif event['monsterType'] == 'RIFTHERALD':
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            blueRiftHeraldKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            blueRiftHeraldKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            blueRiftHeraldKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            blueRiftHeraldKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            blueRiftHeraldKillVariable_end += 1
                            # Code: blueBaronKill_time
                                elif event['monsterType'] == 'BARON_NASHOR':
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            blueBaronKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            blueBaronKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            blueBaronKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            blueBaronKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            blueBaronKillVariable_end += 1
                            # Code: red team
                                if event['monsterType'] == 'DRAGON':
                            # Code: redDragonKill_time
                                    if event['killerId'] in redTeamPlayerIds:
                                        if minuteLimit == 10:
                                            redDragonKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            redDragonKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            redDragonKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            redDragonKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            redDragonKillVariable_end += 1
                            # Code: redDragonHextechKill_time
                                        if event['monsterSubType'] == 'HEXTECH_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonHextechKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonHextechKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonHextechKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonHextechKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonHextechKillVariable_end += 1
                            # Code: redDragonChemtechKill_time
                                        if event['monsterSubType'] == 'CHEMTECH_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonChemtechKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonChemtechKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonChemtechKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonChemtechKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonChemtechKillVariable_end += 1
                            # Code: redDragonFireKill_time
                                        if event['monsterSubType'] == 'FIRE_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonFireKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonFireKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonFireKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonFireKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonFireKillVariable_end += 1
                            # Code: redDragonAirKill_time
                                        if event['monsterSubType'] == 'AIR_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonAirKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonAirKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonAirKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonAirKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonAirKillVariable_end += 1
                            # Code: redDragonEarthKill_time
                                        if event['monsterSubType'] == 'EARTH_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonEarthKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonEarthKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonEarthKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonEarthKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonEarthKillVariable_end += 1
                            # Code: redDragonWaterKill_time
                                        if event['monsterSubType'] == 'WATER_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonWaterKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonWaterKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonWaterKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonWaterKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonWaterKillVariable_end += 1
                            # Code: redDragonElderKill_time
                                        if event['monsterSubType'] == 'ELDER_DRAGON':
                                            if minuteLimit == 10:
                                                redDragonElderKillVariable_min10 += 1
                                            elif minuteLimit == 14:
                                                redDragonElderKillVariable_min14 += 1
                                            elif minuteLimit == 20:
                                                redDragonElderKillVariable_min20 += 1
                                            elif minuteLimit == 27:
                                                redDragonElderKillVariable_min27 += 1
                                            elif minuteLimit == fullTimeMSVariable/60000:
                                                redDragonElderKillVariable_end += 1
                            # Code: redVoidGrubKill_time
                                elif event['monsterType'] == 'HORDE':
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            redVoidGrubKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            redVoidGrubKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            redVoidGrubKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            redVoidGrubKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            redVoidGrubKillVariable_end += 1
                            # Code: redRiftHeraldKill_time
                                elif event['monsterType'] == 'RIFTHERALD':
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            redRiftHeraldKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            redRiftHeraldKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            redRiftHeraldKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            redRiftHeraldKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            redRiftHeraldKillVariable_end += 1
                            # Code: redBaronKill_time
                                elif event['monsterType'] == 'BARON_NASHOR':
                                    if event['killerId'] in blueTeamPlayerIds:
                                        if minuteLimit == 10:
                                            redBaronKillVariable_min10 += 1
                                        elif minuteLimit == 14:
                                            redBaronKillVariable_min14 += 1
                                        elif minuteLimit == 20:
                                            redBaronKillVariable_min20 += 1
                                        elif minuteLimit == 27:
                                            redBaronKillVariable_min27 += 1
                                        elif minuteLimit == fullTimeMSVariable/60000:
                                            redBaronKillVariable_end += 1

                            # Code: BUILDING_KILL
                            elif event['type'] == 'BUILDING_KILL' and event['timestamp'] <= lastMinute:
                            # Code: blueTowerKill_time, redTowerKill_time
                                if event['buildingType'] == 'TOWER_BUILDING' and event['teamId'] == 200:
                                    if minuteLimit == 10:
                                        blueTowerKillVariable_min10 += 1
                                    elif minuteLimit == 14:
                                        blueTowerKillVariable_min14 += 1
                                    elif minuteLimit == 20:
                                        blueTowerKillVariable_min20 += 1
                                    elif minuteLimit == 27:
                                        blueTowerKillVariable_min27 += 1
                                    elif minuteLimit == fullTimeMSVariable/60000:
                                        blueTowerKillVariable_end += 1

                                elif event['buildingType'] == 'TOWER_BUILDING' and event['teamId'] == 100:
                                    if minuteLimit == 10:
                                        redTowerKillVariable_min10 += 1
                                    elif minuteLimit == 14:
                                        redTowerKillVariable_min14 += 1
                                    elif minuteLimit == 20:
                                        redTowerKillVariable_min20 += 1
                                    elif minuteLimit == 27:
                                        redTowerKillVariable_min27 += 1
                                    elif minuteLimit == fullTimeMSVariable/60000:
                                        redTowerKillVariable_end += 1
                            # Code: blueTowerInhibitorKill_time, redInhibitorKill_time
                                elif event['buildingType'] == 'INHIBITOR_BUILDING' and event['teamId'] == 200:
                                    if minuteLimit == 10:
                                        blueInhibitorKillVariable_min10 += 1
                                    elif minuteLimit == 14:
                                        blueInhibitorKillVariable_min14 += 1
                                    elif minuteLimit == 20:
                                        blueInhibitorKillVariable_min20 += 1
                                    elif minuteLimit == 27:
                                        blueInhibitorKillVariable_min27 += 1
                                    elif minuteLimit == fullTimeMSVariable/60000:
                                        blueInhibitorKillVariable_end += 1
                                
                                elif event['buildingType'] == 'INHIBITOR_BUILDING' and event['teamId'] == 100:
                                    if minuteLimit == 10:
                                        redInhibitorKillVariable_min10 += 1
                                    elif minuteLimit == 14:
                                        redInhibitorKillVariable_min14 += 1
                                    elif minuteLimit == 20:
                                        redInhibitorKillVariable_min20 += 1
                                    elif minuteLimit == 27:
                                        redInhibitorKillVariable_min27 += 1
                                    elif minuteLimit == fullTimeMSVariable/60000:
                                        redInhibitorKillVariable_end += 1

                            # Code: participantFrames
                        currentTimeStamp = frame['timestamp']
                        if currentTimeStamp >= lastMinute:
                            if minuteLimit == 10:
                                for currentPlayer in frame['participantFrames']:
                                    if int(currentPlayer) in blueTeamPlayerIds:
                                        blueTotalGoldVariable_min10 += frame['participantFrames'][currentPlayer]['totalGold']
                                        blueMinionsKilledVariable_min10 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        blueJungleMinionsKilledVariable_min10 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        blueAvgPlayerLevelVariable_min10 += frame['participantFrames'][currentPlayer]['level']
                                    elif int(currentPlayer) in redTeamPlayerIds:
                                        redTotalGoldVariable_min10 += frame['participantFrames'][currentPlayer]['totalGold']
                                        redMinionsKilledVariable_min10 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        redJungleMinionsKilledVariable_min10 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        redAvgPlayerLevelVariable_min10 += frame['participantFrames'][currentPlayer]['level']
                                exitLoop_time = True
                            elif minuteLimit == 14:
                                for currentPlayer in frame['participantFrames']:
                                    if int(currentPlayer) in blueTeamPlayerIds:
                                        blueTotalGoldVariable_min14 += frame['participantFrames'][currentPlayer]['totalGold']
                                        blueMinionsKilledVariable_min14 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        blueJungleMinionsKilledVariable_min14 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        blueAvgPlayerLevelVariable_min14 += frame['participantFrames'][currentPlayer]['level']
                                    elif int(currentPlayer) in redTeamPlayerIds:
                                        redTotalGoldVariable_min14 += frame['participantFrames'][currentPlayer]['totalGold']
                                        redMinionsKilledVariable_min14 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        redJungleMinionsKilledVariable_min14 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        redAvgPlayerLevelVariable_min14 += frame['participantFrames'][currentPlayer]['level']
                                exitLoop_time = True
                            elif minuteLimit == 20:
                                for currentPlayer in frame['participantFrames']:
                                    if int(currentPlayer) in blueTeamPlayerIds:
                                        blueTotalGoldVariable_min20 += frame['participantFrames'][currentPlayer]['totalGold']
                                        blueMinionsKilledVariable_min20 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        blueJungleMinionsKilledVariable_min20 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        blueAvgPlayerLevelVariable_min20 += frame['participantFrames'][currentPlayer]['level']
                                    elif int(currentPlayer) in redTeamPlayerIds:
                                        redTotalGoldVariable_min20 += frame['participantFrames'][currentPlayer]['totalGold']
                                        redMinionsKilledVariable_min20 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        redJungleMinionsKilledVariable_min20 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        redAvgPlayerLevelVariable_min20 += frame['participantFrames'][currentPlayer]['level']
                                exitLoop_time = True
                            elif minuteLimit == 27:
                                for currentPlayer in frame['participantFrames']:
                                    if int(currentPlayer) in blueTeamPlayerIds:
                                        blueTotalGoldVariable_min27 += frame['participantFrames'][currentPlayer]['totalGold']
                                        blueMinionsKilledVariable_min27 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        blueJungleMinionsKilledVariable_min27 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        blueAvgPlayerLevelVariable_min27 += frame['participantFrames'][currentPlayer]['level']
                                    elif int(currentPlayer) in redTeamPlayerIds:
                                        redTotalGoldVariable_min27 += frame['participantFrames'][currentPlayer]['totalGold']
                                        redMinionsKilledVariable_min27 += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        redJungleMinionsKilledVariable_min27 += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        redAvgPlayerLevelVariable_min27 += frame['participantFrames'][currentPlayer]['level']
                                exitLoop_time = True
                            elif minuteLimit == fullTimeMSVariable/60000:
                                for currentPlayer in frame['participantFrames']:
                                    if int(currentPlayer) in blueTeamPlayerIds:
                                        blueTotalGoldVariable_end += frame['participantFrames'][currentPlayer]['totalGold']
                                        blueMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        blueJungleMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        blueAvgPlayerLevelVariable_end += frame['participantFrames'][currentPlayer]['level']
                                    elif int(currentPlayer) in redTeamPlayerIds:
                                        redTotalGoldVariable_end += frame['participantFrames'][currentPlayer]['totalGold']
                                        redMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['minionsKilled']
                                        redJungleMinionsKilledVariable_end += frame['participantFrames'][currentPlayer]['jungleMinionsKilled']
                                        redAvgPlayerLevelVariable_end += frame['participantFrames'][currentPlayer]['level']
                                exitLoop_time = True
                        if exitLoop_time:
                            break

                                        


        # General variables for new_dataset_min{time}.csv

                # Column1_time (fixed)
                Column1_time.append(column1)

                # matchID_time (fixed)
                matchID_time.append(current_game_id)

                # fullTimeMS_time (fixed)
                fullTimeMS_time.append(fullTimeMSVariable)

        # Variables for new_dataset_min{time}.csv

                # blueChampionKill_time
                blueChampionKill_min10.append(blueChampionKillVariable_min10)
                blueChampionKill_min14.append(blueChampionKillVariable_min14)
                blueChampionKill_min20.append(blueChampionKillVariable_min20)
                blueChampionKill_min27.append(blueChampionKillVariable_min27)
                blueChampionKill_end.append(blueChampionKillVariable_end)

                # blueFirstBlood_time (fixed)
                blueFirstBlood_time.append(blueFirstBloodVariable)

                # blueDragonKill_time
                blueDragonKill_min10.append(blueDragonKillVariable_min10)
                blueDragonKill_min14.append(blueDragonKillVariable_min14)
                blueDragonKill_min20.append(blueDragonKillVariable_min20)
                blueDragonKill_min27.append(blueDragonKillVariable_min27)
                blueDragonKill_end.append(blueDragonKillVariable_end)

                # blueDragonHextechKill_time
                blueDragonHextechKill_min10.append(blueDragonHextechKillVariable_min10)
                blueDragonHextechKill_min14.append(blueDragonHextechKillVariable_min14)
                blueDragonHextechKill_min20.append(blueDragonHextechKillVariable_min20)
                blueDragonHextechKill_min27.append(blueDragonHextechKillVariable_min27)
                blueDragonHextechKill_end.append(blueDragonHextechKillVariable_end)

                # blueDragonChemtechKill_time
                blueDragonChemtechKill_min10.append(blueDragonChemtechKillVariable_min10)
                blueDragonChemtechKill_min14.append(blueDragonChemtechKillVariable_min14)
                blueDragonChemtechKill_min20.append(blueDragonChemtechKillVariable_min20)
                blueDragonChemtechKill_min27.append(blueDragonChemtechKillVariable_min27)
                blueDragonChemtechKill_end.append(blueDragonChemtechKillVariable_end)

                # blueDragonFireKill_time
                blueDragonFireKill_min10.append(blueDragonFireKillVariable_min10)
                blueDragonFireKill_min14.append(blueDragonFireKillVariable_min14)
                blueDragonFireKill_min20.append(blueDragonFireKillVariable_min20)
                blueDragonFireKill_min27.append(blueDragonFireKillVariable_min27)
                blueDragonFireKill_end.append(blueDragonFireKillVariable_end)

                # blueDragonAirKill_time
                blueDragonAirKill_min10.append(blueDragonAirKillVariable_min10)
                blueDragonAirKill_min14.append(blueDragonAirKillVariable_min14)
                blueDragonAirKill_min20.append(blueDragonAirKillVariable_min20)
                blueDragonAirKill_min27.append(blueDragonAirKillVariable_min27)
                blueDragonAirKill_end.append(blueDragonAirKillVariable_end)

                # blueDragonEarthKill_time
                blueDragonEarthKill_min10.append(blueDragonEarthKillVariable_min10)
                blueDragonEarthKill_min14.append(blueDragonEarthKillVariable_min14)
                blueDragonEarthKill_min20.append(blueDragonEarthKillVariable_min20)
                blueDragonEarthKill_min27.append(blueDragonEarthKillVariable_min27)
                blueDragonEarthKill_end.append(blueDragonEarthKillVariable_end)

                # blueDragonWaterKill_time
                blueDragonWaterKill_min10.append(blueDragonWaterKillVariable_min10)
                blueDragonWaterKill_min14.append(blueDragonWaterKillVariable_min14)
                blueDragonWaterKill_min20.append(blueDragonWaterKillVariable_min20)
                blueDragonWaterKill_min27.append(blueDragonWaterKillVariable_min27)
                blueDragonWaterKill_end.append(blueDragonWaterKillVariable_end)

                # blueDragonElderKill_time
                blueDragonElderKill_min10.append(blueDragonElderKillVariable_min10)
                blueDragonElderKill_min14.append(blueDragonElderKillVariable_min14)
                blueDragonElderKill_min20.append(blueDragonElderKillVariable_min20)
                blueDragonElderKill_min27.append(blueDragonElderKillVariable_min27)
                blueDragonElderKill_end.append(blueDragonElderKillVariable_end)

                # blueVoidGrubKill_time
                blueVoidGrubKill_min10.append(blueVoidGrubKillVariable_min10)
                blueVoidGrubKill_min14.append(blueVoidGrubKillVariable_min14)
                blueVoidGrubKill_min20.append(blueVoidGrubKillVariable_min20)
                blueVoidGrubKill_min27.append(blueVoidGrubKillVariable_min27)
                blueVoidGrubKill_end.append(blueVoidGrubKillVariable_end)

                # blueRiftHeraldKill_time
                blueRiftHeraldKill_min10.append(blueRiftHeraldKillVariable_min10)
                blueRiftHeraldKill_min14.append(blueRiftHeraldKillVariable_min14)
                blueRiftHeraldKill_min20.append(blueRiftHeraldKillVariable_min20)
                blueRiftHeraldKill_min27.append(blueRiftHeraldKillVariable_min27)
                blueRiftHeraldKill_end.append(blueRiftHeraldKillVariable_end)

                # blueBaronKill_time
                blueBaronKill_min10.append(blueBaronKillVariable_min10)
                blueBaronKill_min14.append(blueBaronKillVariable_min14)
                blueBaronKill_min20.append(blueBaronKillVariable_min20)
                blueBaronKill_min27.append(blueBaronKillVariable_min27)
                blueBaronKill_end.append(blueBaronKillVariable_end)

                # blueTowerKill_time
                blueTowerKill_min10.append(blueTowerKillVariable_min10)
                blueTowerKill_min14.append(blueTowerKillVariable_min14)
                blueTowerKill_min20.append(blueTowerKillVariable_min20)
                blueTowerKill_min27.append(blueTowerKillVariable_min27)
                blueTowerKill_end.append(blueTowerKillVariable_end)

                # blueInhibitorKill_time
                blueInhibitorKill_min10.append(blueInhibitorKillVariable_min10)
                blueInhibitorKill_min14.append(blueInhibitorKillVariable_min14)
                blueInhibitorKill_min20.append(blueInhibitorKillVariable_min20)
                blueInhibitorKill_min27.append(blueInhibitorKillVariable_min27)
                blueInhibitorKill_end.append(blueInhibitorKillVariable_end)

                # blueTotalGold_time
                blueTotalGold_min10.append(blueTotalGoldVariable_min10)
                blueTotalGold_min14.append(blueTotalGoldVariable_min14)
                blueTotalGold_min20.append(blueTotalGoldVariable_min20)
                blueTotalGold_min27.append(blueTotalGoldVariable_min27)
                blueTotalGold_end.append(blueTotalGoldVariable_end)

                # blueMinionsKilled_time
                blueMinionsKilled_min10.append(blueMinionsKilledVariable_min10)
                blueMinionsKilled_min14.append(blueMinionsKilledVariable_min14)
                blueMinionsKilled_min20.append(blueMinionsKilledVariable_min20)
                blueMinionsKilled_min27.append(blueMinionsKilledVariable_min27)
                blueMinionsKilled_end.append(blueMinionsKilledVariable_end)

                # blueJungleMinionsKilled_time
                blueJungleMinionsKilled_min10.append(blueJungleMinionsKilledVariable_min10)
                blueJungleMinionsKilled_min14.append(blueJungleMinionsKilledVariable_min14)
                blueJungleMinionsKilled_min20.append(blueJungleMinionsKilledVariable_min20)
                blueJungleMinionsKilled_min27.append(blueJungleMinionsKilledVariable_min27)
                blueJungleMinionsKilled_end.append(blueJungleMinionsKilledVariable_end)

                # blueAvgPlayerLevel_time
                blueAvgPlayerLevel_min10.append(blueAvgPlayerLevelVariable_min10)
                blueAvgPlayerLevel_min14.append(blueAvgPlayerLevelVariable_min14)
                blueAvgPlayerLevel_min20.append(blueAvgPlayerLevelVariable_min20)
                blueAvgPlayerLevel_min27.append(blueAvgPlayerLevelVariable_min27)
                blueAvgPlayerLevel_end.append(blueAvgPlayerLevelVariable_end)

                # blueWin_time (fixed)
                blueWin_time.append(blueWinVariable)

                # redChampionKill_time
                redChampionKill_min10.append(redChampionKillVariable_min10)
                redChampionKill_min14.append(redChampionKillVariable_min14)
                redChampionKill_min20.append(redChampionKillVariable_min20)
                redChampionKill_min27.append(redChampionKillVariable_min27)
                redChampionKill_end.append(redChampionKillVariable_end)

                # redFirstBlood_time (fixed)
                redFirstBlood_time.append(redFirstBloodVariable)

                # redDragonKill_time
                redDragonKill_min10.append(redDragonKillVariable_min10)
                redDragonKill_min14.append(redDragonKillVariable_min14)
                redDragonKill_min20.append(redDragonKillVariable_min20)
                redDragonKill_min27.append(redDragonKillVariable_min27)
                redDragonKill_end.append(redDragonKillVariable_end)

                # redDragonHextechKill_time
                redDragonHextechKill_min10.append(redDragonHextechKillVariable_min10)
                redDragonHextechKill_min14.append(redDragonHextechKillVariable_min14)
                redDragonHextechKill_min20.append(redDragonHextechKillVariable_min20)
                redDragonHextechKill_min27.append(redDragonHextechKillVariable_min27)
                redDragonHextechKill_end.append(redDragonHextechKillVariable_end)

                # redDragonChemtechKill_time
                redDragonChemtechKill_min10.append(redDragonChemtechKillVariable_min10)
                redDragonChemtechKill_min14.append(redDragonChemtechKillVariable_min14)
                redDragonChemtechKill_min20.append(redDragonChemtechKillVariable_min20)
                redDragonChemtechKill_min27.append(redDragonChemtechKillVariable_min27)
                redDragonChemtechKill_end.append(redDragonChemtechKillVariable_end)

                # redDragonFireKill_time
                redDragonFireKill_min10.append(redDragonFireKillVariable_min10)
                redDragonFireKill_min14.append(redDragonFireKillVariable_min14)
                redDragonFireKill_min20.append(redDragonFireKillVariable_min20)
                redDragonFireKill_min27.append(redDragonFireKillVariable_min27)
                redDragonFireKill_end.append(redDragonFireKillVariable_end)

                # redDragonAirKill_time
                redDragonAirKill_min10.append(redDragonAirKillVariable_min10)
                redDragonAirKill_min14.append(redDragonAirKillVariable_min14)
                redDragonAirKill_min20.append(redDragonAirKillVariable_min20)
                redDragonAirKill_min27.append(redDragonAirKillVariable_min27)
                redDragonAirKill_end.append(redDragonAirKillVariable_end)

                # redDragonEarthKill_time
                redDragonEarthKill_min10.append(redDragonEarthKillVariable_min10)
                redDragonEarthKill_min14.append(redDragonEarthKillVariable_min14)
                redDragonEarthKill_min20.append(redDragonEarthKillVariable_min20)
                redDragonEarthKill_min27.append(redDragonEarthKillVariable_min27)
                redDragonEarthKill_end.append(redDragonEarthKillVariable_end)

                # redDragonWaterKill_time
                redDragonWaterKill_min10.append(redDragonWaterKillVariable_min10)
                redDragonWaterKill_min14.append(redDragonWaterKillVariable_min14)
                redDragonWaterKill_min20.append(redDragonWaterKillVariable_min20)
                redDragonWaterKill_min27.append(redDragonWaterKillVariable_min27)
                redDragonWaterKill_end.append(redDragonWaterKillVariable_end)

                # redDragonElderKill_time
                redDragonElderKill_min10.append(redDragonElderKillVariable_min10)
                redDragonElderKill_min14.append(redDragonElderKillVariable_min14)
                redDragonElderKill_min20.append(redDragonElderKillVariable_min20)
                redDragonElderKill_min27.append(redDragonElderKillVariable_min27)
                redDragonElderKill_end.append(redDragonElderKillVariable_end)

                # redVoidGrubKill_time
                redVoidGrubKill_min10.append(redVoidGrubKillVariable_min10)
                redVoidGrubKill_min14.append(redVoidGrubKillVariable_min14)
                redVoidGrubKill_min20.append(redVoidGrubKillVariable_min20)
                redVoidGrubKill_min27.append(redVoidGrubKillVariable_min27)
                redVoidGrubKill_end.append(redVoidGrubKillVariable_end)

                # redRiftHeraldKill_time
                redRiftHeraldKill_min10.append(redRiftHeraldKillVariable_min10)
                redRiftHeraldKill_min14.append(redRiftHeraldKillVariable_min14)
                redRiftHeraldKill_min20.append(redRiftHeraldKillVariable_min20)
                redRiftHeraldKill_min27.append(redRiftHeraldKillVariable_min27)
                redRiftHeraldKill_end.append(redRiftHeraldKillVariable_end)

                # redBaronKill_time
                redBaronKill_min10.append(redBaronKillVariable_min10)
                redBaronKill_min14.append(redBaronKillVariable_min14)
                redBaronKill_min20.append(redBaronKillVariable_min20)
                redBaronKill_min27.append(redBaronKillVariable_min27)
                redBaronKill_end.append(redBaronKillVariable_end)

                # redTowerKill_time
                redTowerKill_min10.append(redTowerKillVariable_min10)
                redTowerKill_min14.append(redTowerKillVariable_min14)
                redTowerKill_min20.append(redTowerKillVariable_min20)
                redTowerKill_min27.append(redTowerKillVariable_min27)
                redTowerKill_end.append(redTowerKillVariable_end)

                # redInhibitorKill_time
                redInhibitorKill_min10.append(redInhibitorKillVariable_min10)
                redInhibitorKill_min14.append(redInhibitorKillVariable_min14)
                redInhibitorKill_min20.append(redInhibitorKillVariable_min20)
                redInhibitorKill_min27.append(redInhibitorKillVariable_min27)
                redInhibitorKill_end.append(redInhibitorKillVariable_end)

                # redTotalGold_time
                redTotalGold_min10.append(redTotalGoldVariable_min10)
                redTotalGold_min14.append(redTotalGoldVariable_min14)
                redTotalGold_min20.append(redTotalGoldVariable_min20)
                redTotalGold_min27.append(redTotalGoldVariable_min27)
                redTotalGold_end.append(redTotalGoldVariable_end)

                # redMinionsKilled_time
                redMinionsKilled_min10.append(redMinionsKilledVariable_min10)
                redMinionsKilled_min14.append(redMinionsKilledVariable_min14)
                redMinionsKilled_min20.append(redMinionsKilledVariable_min20)
                redMinionsKilled_min27.append(redMinionsKilledVariable_min27)
                redMinionsKilled_end.append(redMinionsKilledVariable_end)

                # redJungleMinionsKilled_time
                redJungleMinionsKilled_min10.append(redJungleMinionsKilledVariable_min10)
                redJungleMinionsKilled_min14.append(redJungleMinionsKilledVariable_min14)
                redJungleMinionsKilled_min20.append(redJungleMinionsKilledVariable_min20)
                redJungleMinionsKilled_min27.append(redJungleMinionsKilledVariable_min27)
                redJungleMinionsKilled_end.append(redJungleMinionsKilledVariable_end)

                # redAvgPlayerLevel_time
                redAvgPlayerLevel_min10.append(redAvgPlayerLevelVariable_min10)
                redAvgPlayerLevel_min14.append(redAvgPlayerLevelVariable_min14)
                redAvgPlayerLevel_min20.append(redAvgPlayerLevelVariable_min20)
                redAvgPlayerLevel_min27.append(redAvgPlayerLevelVariable_min27)
                redAvgPlayerLevel_end.append(redAvgPlayerLevelVariable_end)

                # redWin_time (fixed)
                redWin_time.append(redWinVariable)


    # Write firstLine into csv
    # Game interval csv files
        with(open(name_for_file_20, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_40, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_60, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_80, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_100, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

    # Time stamp csv files
        with(open(name_for_file_min10, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_min14, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_min20, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_min27, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_end, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

    # Game interval csv files
    for i in range(len(Column1_timeInterval)):
        line_20 = [
            Column1_timeInterval[i],
            matchID_timeInterval[i],
            fullTimeMS_timeInterval[i],
            timeStamp_20[i],
            blueChampionKill_20[i],
            blueFirstBlood[i],
            blueDragonKill_20[i],
            blueDragonHextechKill_20[i],
            blueDragonChemtechKill_20[i],
            blueDragonFireKill_20[i],
            blueDragonAirKill_20[i],
            blueDragonEarthKill_20[i],
            blueDragonWaterKill_20[i],
            blueDragonElderKill_20[i],
            blueVoidGrubKill_20[i],
            blueRiftHeraldKill_20[i],
            blueBaronKill_20[i],
            blueTowerKill_20[i],
            blueInhibitorKill_20[i],
            blueTotalGold_20[i],
            blueMinionsKilled_20[i],
            blueJungleMinionsKilled_20[i],
            blueAvgPlayerLevel_20[i],
            blueWin[i],
            redChampionKill_20[i],
            redFirstBlood[i],
            redDragonKill_20[i],
            redDragonHextechKill_20[i],
            redDragonChemtechKill_20[i],
            redDragonFireKill_20[i],
            redDragonAirKill_20[i],
            redDragonEarthKill_20[i],
            redDragonWaterKill_20[i],
            redDragonElderKill_20[i],
            redVoidGrubKill_20[i],
            redRiftHeraldKill_20[i],
            redBaronKill_20[i],
            redTowerKill_20[i],
            redInhibitorKill_20[i],
            redTotalGold_20[i],
            redMinionsKilled_20[i],
            redJungleMinionsKilled_20[i],
            redAvgPlayerLevel_20[i],
            redWin[i]
        ]
        line_40 = [
            Column1_timeInterval[i],
            matchID_timeInterval[i],
            fullTimeMS_timeInterval[i],
            timeStamp_40[i],
            blueChampionKill_40[i],
            blueFirstBlood[i],
            blueDragonKill_40[i],
            blueDragonHextechKill_40[i],
            blueDragonChemtechKill_40[i],
            blueDragonFireKill_40[i],
            blueDragonAirKill_40[i],
            blueDragonEarthKill_40[i],
            blueDragonWaterKill_40[i],
            blueDragonElderKill_40[i],
            blueVoidGrubKill_40[i],
            blueRiftHeraldKill_40[i],
            blueBaronKill_40[i],
            blueTowerKill_40[i],
            blueInhibitorKill_40[i],
            blueTotalGold_40[i],
            blueMinionsKilled_40[i],
            blueJungleMinionsKilled_40[i],
            blueAvgPlayerLevel_40[i],
            blueWin[i],
            redChampionKill_40[i],
            redFirstBlood[i],
            redDragonKill_40[i],
            redDragonHextechKill_40[i],
            redDragonChemtechKill_40[i],
            redDragonFireKill_40[i],
            redDragonAirKill_40[i],
            redDragonEarthKill_40[i],
            redDragonWaterKill_40[i],
            redDragonElderKill_40[i],
            redVoidGrubKill_40[i],
            redRiftHeraldKill_40[i],
            redBaronKill_40[i],
            redTowerKill_40[i],
            redInhibitorKill_40[i],
            redTotalGold_40[i],
            redMinionsKilled_40[i],
            redJungleMinionsKilled_40[i],
            redAvgPlayerLevel_40[i],
            redWin[i]
        ]
        line_60 = [
            Column1_timeInterval[i],
            matchID_timeInterval[i],
            fullTimeMS_timeInterval[i],
            timeStamp_60[i],
            blueChampionKill_60[i],
            blueFirstBlood[i],
            blueDragonKill_60[i],
            blueDragonHextechKill_60[i],
            blueDragonChemtechKill_60[i],
            blueDragonFireKill_60[i],
            blueDragonAirKill_60[i],
            blueDragonEarthKill_60[i],
            blueDragonWaterKill_60[i],
            blueDragonElderKill_60[i],
            blueVoidGrubKill_60[i],
            blueRiftHeraldKill_60[i],
            blueBaronKill_60[i],
            blueTowerKill_60[i],
            blueInhibitorKill_60[i],
            blueTotalGold_60[i],
            blueMinionsKilled_60[i],
            blueJungleMinionsKilled_60[i],
            blueAvgPlayerLevel_60[i],
            blueWin[i],
            redChampionKill_60[i],
            redFirstBlood[i],
            redDragonKill_60[i],
            redDragonHextechKill_60[i],
            redDragonChemtechKill_60[i],
            redDragonFireKill_60[i],
            redDragonAirKill_60[i],
            redDragonEarthKill_60[i],
            redDragonWaterKill_60[i],
            redDragonElderKill_60[i],
            redVoidGrubKill_60[i],
            redRiftHeraldKill_60[i],
            redBaronKill_60[i],
            redTowerKill_60[i],
            redInhibitorKill_60[i],
            redTotalGold_60[i],
            redMinionsKilled_60[i],
            redJungleMinionsKilled_60[i],
            redAvgPlayerLevel_60[i],
            redWin[i]
        ]
        line_80 = [
            Column1_timeInterval[i],
            matchID_timeInterval[i],
            fullTimeMS_timeInterval[i],
            timeStamp_80[i],
            blueChampionKill_80[i],
            blueFirstBlood[i],
            blueDragonKill_80[i],
            blueDragonHextechKill_80[i],
            blueDragonChemtechKill_80[i],
            blueDragonFireKill_80[i],
            blueDragonAirKill_80[i],
            blueDragonEarthKill_80[i],
            blueDragonWaterKill_80[i],
            blueDragonElderKill_80[i],
            blueVoidGrubKill_80[i],
            blueRiftHeraldKill_80[i],
            blueBaronKill_80[i],
            blueTowerKill_80[i],
            blueInhibitorKill_80[i],
            blueTotalGold_80[i],
            blueMinionsKilled_80[i],
            blueJungleMinionsKilled_80[i],
            blueAvgPlayerLevel_80[i],
            blueWin[i],
            redChampionKill_80[i],
            redFirstBlood[i],
            redDragonKill_80[i],
            redDragonHextechKill_80[i],
            redDragonChemtechKill_80[i],
            redDragonFireKill_80[i],
            redDragonAirKill_80[i],
            redDragonEarthKill_80[i],
            redDragonWaterKill_80[i],
            redDragonElderKill_80[i],
            redVoidGrubKill_80[i],
            redRiftHeraldKill_80[i],
            redBaronKill_80[i],
            redTowerKill_80[i],
            redInhibitorKill_80[i],
            redTotalGold_80[i],
            redMinionsKilled_80[i],
            redJungleMinionsKilled_80[i],
            redAvgPlayerLevel_80[i],
            redWin[i]
        ]
        line_100 = [
            Column1_timeInterval[i],
            matchID_timeInterval[i],
            fullTimeMS_timeInterval[i],
            timeStamp[i],
            blueChampionKill[i],
            blueFirstBlood[i],
            blueDragonKill[i],
            blueDragonHextechKill[i],
            blueDragonChemtechKill[i],
            blueDragonFireKill[i],
            blueDragonAirKill[i],
            blueDragonEarthKill[i],
            blueDragonWaterKill[i],
            blueDragonElderKill[i],
            blueVoidGrubKill[i],
            blueRiftHeraldKill[i],
            blueBaronKill[i],
            blueTowerKill[i],
            blueInhibitorKill[i],
            blueTotalGold[i],
            blueMinionsKilled[i],
            blueJungleMinionsKilled[i],
            blueAvgPlayerLevel[i],
            blueWin[i],
            redChampionKill[i],
            redFirstBlood[i],
            redDragonKill[i],
            redDragonHextechKill[i],
            redDragonChemtechKill[i],
            redDragonFireKill[i],
            redDragonAirKill[i],
            redDragonEarthKill[i],
            redDragonWaterKill[i],
            redDragonElderKill[i],
            redVoidGrubKill[i],
            redRiftHeraldKill[i],
            redBaronKill[i],
            redTowerKill[i],
            redInhibitorKill[i],
            redTotalGold[i],
            redMinionsKilled[i],
            redJungleMinionsKilled[i],
            redAvgPlayerLevel[i],
            redWin[i]
        ]
        with(open(name_for_file_20, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_20)

        with(open(name_for_file_40, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_40)

        with(open(name_for_file_60, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_60)

        with(open(name_for_file_80, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_80)

        with(open(name_for_file_100, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_100)

    # Time stamp csv files
    for j in range(len(Column1_time)):
        line_min10 = [
            Column1_time[j],
            matchID_time[j],
            fullTimeMS_time[j],
            timeStamp_min10[j],
            blueChampionKill_min10[j],
            blueFirstBlood_time[j],
            blueDragonKill_min10[j],
            blueDragonHextechKill_min10[j],
            blueDragonChemtechKill_min10[j],
            blueDragonFireKill_min10[j],
            blueDragonAirKill_min10[j],
            blueDragonEarthKill_min10[j],
            blueDragonWaterKill_min10[j],
            blueDragonElderKill_min10[j],
            blueVoidGrubKill_min10[j],
            blueRiftHeraldKill_min10[j],
            blueBaronKill_min10[j],
            blueTowerKill_min10[j],
            blueInhibitorKill_min10[j],
            blueTotalGold_min10[j],
            blueMinionsKilled_min10[j],
            blueJungleMinionsKilled_min10[j],
            blueAvgPlayerLevel_min10[j],
            blueWin_time[j],
            redChampionKill_min10[j],
            redFirstBlood_time[j],
            redDragonKill_min10[j],
            redDragonHextechKill_min10[j],
            redDragonChemtechKill_min10[j],
            redDragonFireKill_min10[j],
            redDragonAirKill_min10[j],
            redDragonEarthKill_min10[j],
            redDragonWaterKill_min10[j],
            redDragonElderKill_min10[j],
            redVoidGrubKill_min10[j],
            redRiftHeraldKill_min10[j],
            redBaronKill_min10[j],
            redTowerKill_min10[j],
            redInhibitorKill_min10[j],
            redTotalGold_min10[j],
            redMinionsKilled_min10[j],
            redJungleMinionsKilled_min10[j],
            redAvgPlayerLevel_min10[j],
            redWin_time[j]
        ]
        line_min14 = [
            Column1_time[j],
            matchID_time[j],
            fullTimeMS_time[j],
            timeStamp_min14[j],
            blueChampionKill_min14[j],
            blueFirstBlood_time[j],
            blueDragonKill_min14[j],
            blueDragonHextechKill_min14[j],
            blueDragonChemtechKill_min14[j],
            blueDragonFireKill_min14[j],
            blueDragonAirKill_min14[j],
            blueDragonEarthKill_min14[j],
            blueDragonWaterKill_min14[j],
            blueDragonElderKill_min14[j],
            blueVoidGrubKill_min14[j],
            blueRiftHeraldKill_min14[j],
            blueBaronKill_min14[j],
            blueTowerKill_min14[j],
            blueInhibitorKill_min14[j],
            blueTotalGold_min14[j],
            blueMinionsKilled_min14[j],
            blueJungleMinionsKilled_min14[j],
            blueAvgPlayerLevel_min14[j],
            blueWin_time[j],
            redChampionKill_min14[j],
            redFirstBlood_time[j],
            redDragonKill_min14[j],
            redDragonHextechKill_min14[j],
            redDragonChemtechKill_min14[j],
            redDragonFireKill_min14[j],
            redDragonAirKill_min14[j],
            redDragonEarthKill_min14[j],
            redDragonWaterKill_min14[j],
            redDragonElderKill_min14[j],
            redVoidGrubKill_min14[j],
            redRiftHeraldKill_min14[j],
            redBaronKill_min14[j],
            redTowerKill_min14[j],
            redInhibitorKill_min14[j],
            redTotalGold_min14[j],
            redMinionsKilled_min14[j],
            redJungleMinionsKilled_min14[j],
            redAvgPlayerLevel_min14[j],
            redWin_time[j]
        ]
        line_min20 = [
            Column1_time[j],
            matchID_time[j],
            fullTimeMS_time[j],
            timeStamp_min20[j],
            blueChampionKill_min20[j],
            blueFirstBlood_time[j],
            blueDragonKill_min20[j],
            blueDragonHextechKill_min20[j],
            blueDragonChemtechKill_min20[j],
            blueDragonFireKill_min20[j],
            blueDragonAirKill_min20[j],
            blueDragonEarthKill_min20[j],
            blueDragonWaterKill_min20[j],
            blueDragonElderKill_min20[j],
            blueVoidGrubKill_min20[j],
            blueRiftHeraldKill_min20[j],
            blueBaronKill_min20[j],
            blueTowerKill_min20[j],
            blueInhibitorKill_min20[j],
            blueTotalGold_min20[j],
            blueMinionsKilled_min20[j],
            blueJungleMinionsKilled_min20[j],
            blueAvgPlayerLevel_min20[j],
            blueWin_time[j],
            redChampionKill_min20[j],
            redFirstBlood_time[j],
            redDragonKill_min20[j],
            redDragonHextechKill_min20[j],
            redDragonChemtechKill_min20[j],
            redDragonFireKill_min20[j],
            redDragonAirKill_min20[j],
            redDragonEarthKill_min20[j],
            redDragonWaterKill_min20[j],
            redDragonElderKill_min20[j],
            redVoidGrubKill_min20[j],
            redRiftHeraldKill_min20[j],
            redBaronKill_min20[j],
            redTowerKill_min20[j],
            redInhibitorKill_min20[j],
            redTotalGold_min20[j],
            redMinionsKilled_min20[j],
            redJungleMinionsKilled_min20[j],
            redAvgPlayerLevel_min20[j],
            redWin_time[j]
        ]
        line_min27 = [
            Column1_time[j],
            matchID_time[j],
            fullTimeMS_time[j],
            timeStamp_min27[j],
            blueChampionKill_min27[j],
            blueFirstBlood_time[j],
            blueDragonKill_min27[j],
            blueDragonHextechKill_min27[j],
            blueDragonChemtechKill_min27[j],
            blueDragonFireKill_min27[j],
            blueDragonAirKill_min27[j],
            blueDragonEarthKill_min27[j],
            blueDragonWaterKill_min27[j],
            blueDragonElderKill_min27[j],
            blueVoidGrubKill_min27[j],
            blueRiftHeraldKill_min27[j],
            blueBaronKill_min27[j],
            blueTowerKill_min27[j],
            blueInhibitorKill_min27[j],
            blueTotalGold_min27[j],
            blueMinionsKilled_min27[j],
            blueJungleMinionsKilled_min27[j],
            blueAvgPlayerLevel_min27[j],
            blueWin_time[j],
            redChampionKill_min27[j],
            redFirstBlood_time[j],
            redDragonKill_min27[j],
            redDragonHextechKill_min27[j],
            redDragonChemtechKill_min27[j],
            redDragonFireKill_min27[j],
            redDragonAirKill_min27[j],
            redDragonEarthKill_min27[j],
            redDragonWaterKill_min27[j],
            redDragonElderKill_min27[j],
            redVoidGrubKill_min27[j],
            redRiftHeraldKill_min27[j],
            redBaronKill_min27[j],
            redTowerKill_min27[j],
            redInhibitorKill_min27[j],
            redTotalGold_min27[j],
            redMinionsKilled_min27[j],
            redJungleMinionsKilled_min27[j],
            redAvgPlayerLevel_min27[j],
            redWin_time[j]
        ]
        line_end = [
            Column1_time[j],
            matchID_time[j],
            fullTimeMS_time[j],
            timeStamp_end[j],
            blueChampionKill_end[j],
            blueFirstBlood[j],
            blueDragonKill_end[j],
            blueDragonHextechKill_end[j],
            blueDragonChemtechKill_end[j],
            blueDragonFireKill_end[j],
            blueDragonAirKill_end[j],
            blueDragonEarthKill_end[j],
            blueDragonWaterKill_end[j],
            blueDragonElderKill_end[j],
            blueVoidGrubKill_end[j],
            blueRiftHeraldKill_end[j],
            blueBaronKill_end[j],
            blueTowerKill_end[j],
            blueInhibitorKill_end[j],
            blueTotalGold_end[j],
            blueMinionsKilled_end[j],
            blueJungleMinionsKilled_end[j],
            blueAvgPlayerLevel_end[j],
            blueWin[j],
            redChampionKill_end[j],
            redFirstBlood[j],
            redDragonKill_end[j],
            redDragonHextechKill_end[j],
            redDragonChemtechKill_end[j],
            redDragonFireKill_end[j],
            redDragonAirKill_end[j],
            redDragonEarthKill_end[j],
            redDragonWaterKill_end[j],
            redDragonElderKill_end[j],
            redVoidGrubKill_end[j],
            redRiftHeraldKill_end[j],
            redBaronKill_end[j],
            redTowerKill_end[j],
            redInhibitorKill_end[j],
            redTotalGold_end[j],
            redMinionsKilled_end[j],
            redJungleMinionsKilled_end[j],
            redAvgPlayerLevel_end[j],
            redWin[j]
        ]
        with(open(name_for_file_min10, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_min10)

        with(open(name_for_file_min14, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_min14)

        with(open(name_for_file_min20, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_min20)

        with(open(name_for_file_min27, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_min27)

        with(open(name_for_file_end, mode='a', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(line_end)
        
    end_time = time.time()
    runtime = end_time - start_time
    print(f'Runtime: {runtime}')
            
if __name__ == '__main__':
    main()
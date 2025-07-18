from helpers_match_v5 import get_timeline_by_game_id
from PARAMS import API_KEY
import time
import csv


def main():
    # Measuring time
    start_time = time.time()

    # Other variables
    region_for_file = 'NA1'
    number = 1

    matchIDs_path = f'./gameIdPlatforms_for_timeStamps/{region_for_file}_game_ids/{region_for_file}_game_ids_{number}.txt'
    name_for_file_20 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min10/5_new_dataset_min10({region_for_file}_game_ids_{number}).csv'
    name_for_file_40 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min14/5_new_dataset_min14({region_for_file}_game_ids_{number}).csv'
    name_for_file_60 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min20/5_new_dataset_min20({region_for_file}_game_ids_{number}).csv'
    name_for_file_80 = f'./Datasets/Platform_Datasets_self_made/{region_for_file}/timeStamp_min27/5_new_dataset_min27({region_for_file}_game_ids_{number}).csv'
    
    # Csv header
    firstLine = ',matchID,fullTimeMS,timeStamp,blueChampionKill,blueFirstBlood,blueDragonKill,blueDragonHextechKill,blueDragonChemtechKill,blueDragonFireKill,blueDragonAirKill,blueDragonEarthKill,blueDragonWaterKill,blueDragonElderKill,blueVoidGrubKill,blueRiftHeraldKill,blueBaronKill,blueTowerKill,blueInhibitorKill,blueTotalGold,blueMinionsKilled,blueJungleMinionsKilled,blueAvgPlayerLevel,blueWin,redChampionKill,redFirstBlood,redDragonKill,redDragonHextechKill,redDragonChemtechKill,redDragonFireKill,redDragonAirKill,redDragonEarthKill,redDragonWaterKill,redDragonElderKill,redVoidGrubKill,redRiftHeraldKill,redBaronKill,redTowerKill,redInhibitorKill,redTotalGold,redMinionsKilled,redJungleMinionsKilled,redAvgPlayerLevel,redWin'

    # Variables for new_dataset_{timeInterval}.csv

    # General variables timeInterval
    Column1_timeInterval = list()
    matchID_timeInterval = list()
    fullTimeMS_timeInterval = list()


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

   


    # defined values

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
            redChampionKillVariable_20 = 0
            redChampionKillVariable_40 = 0
            redChampionKillVariable_60 = 0
            redChampionKillVariable_80 = 0

            # blueDragonKill, redDragonKill
            blueDragonKillVariable_20 = 0
            blueDragonKillVariable_40 = 0
            blueDragonKillVariable_60 = 0
            blueDragonKillVariable_80 = 0
            redDragonKillVariable_20 = 0
            redDragonKillVariable_40 = 0
            redDragonKillVariable_60 = 0
            redDragonKillVariable_80 = 0

            # blueDragonHextechKill, redDragonHextechKill
            blueDragonHextechKillVariable_20 = 0
            blueDragonHextechKillVariable_40 = 0
            blueDragonHextechKillVariable_60 = 0
            blueDragonHextechKillVariable_80 = 0
            redDragonHextechKillVariable_20 = 0
            redDragonHextechKillVariable_40 = 0
            redDragonHextechKillVariable_60 = 0
            redDragonHextechKillVariable_80 = 0

            # blueDragonChemtechKill, redDragonChemtechKill
            blueDragonChemtechKillVariable_20 = 0
            blueDragonChemtechKillVariable_40 = 0
            blueDragonChemtechKillVariable_60 = 0
            blueDragonChemtechKillVariable_80 = 0
            redDragonChemtechKillVariable_20 = 0
            redDragonChemtechKillVariable_40 = 0
            redDragonChemtechKillVariable_60 = 0
            redDragonChemtechKillVariable_80 = 0

            # blueDragonFireKill, redDragonFireKill
            blueDragonFireKillVariable_20 = 0
            blueDragonFireKillVariable_40 = 0
            blueDragonFireKillVariable_60 = 0
            blueDragonFireKillVariable_80 = 0
            redDragonFireKillVariable_20 = 0
            redDragonFireKillVariable_40 = 0
            redDragonFireKillVariable_60 = 0
            redDragonFireKillVariable_80 = 0

            # blueDragonAirKill, redDragonAirKill
            blueDragonAirKillVariable_20 = 0
            blueDragonAirKillVariable_40 = 0
            blueDragonAirKillVariable_60 = 0
            blueDragonAirKillVariable_80 = 0
            redDragonAirKillVariable_20 = 0
            redDragonAirKillVariable_40 = 0
            redDragonAirKillVariable_60 = 0
            redDragonAirKillVariable_80 = 0

            # blueDragonEarthKill, redDragonEarthKill
            blueDragonEarthKillVariable_20 = 0
            blueDragonEarthKillVariable_40 = 0
            blueDragonEarthKillVariable_60 = 0
            blueDragonEarthKillVariable_80 = 0
            redDragonEarthKillVariable_20 = 0
            redDragonEarthKillVariable_40 = 0
            redDragonEarthKillVariable_60 = 0
            redDragonEarthKillVariable_80 = 0

            # blueDragonWaterKill, redDragonWaterKill
            blueDragonWaterKillVariable_20 = 0
            blueDragonWaterKillVariable_40 = 0
            blueDragonWaterKillVariable_60 = 0
            blueDragonWaterKillVariable_80 = 0
            redDragonWaterKillVariable_20 = 0
            redDragonWaterKillVariable_40 = 0
            redDragonWaterKillVariable_60 = 0
            redDragonWaterKillVariable_80 = 0

            # blueDragonElderKill, redDragonElderKill
            blueDragonElderKillVariable_20 = 0
            blueDragonElderKillVariable_40 = 0
            blueDragonElderKillVariable_60 = 0
            blueDragonElderKillVariable_80 = 0
            redDragonElderKillVariable_20 = 0
            redDragonElderKillVariable_40 = 0
            redDragonElderKillVariable_60 = 0
            redDragonElderKillVariable_80 = 0

            # blueVoidGrubKill, redVoidGrubKill
            blueVoidGrubKillVariable_20 = 0
            blueVoidGrubKillVariable_40 = 0
            blueVoidGrubKillVariable_60 = 0
            blueVoidGrubKillVariable_80 = 0
            redVoidGrubKillVariable_20 = 0
            redVoidGrubKillVariable_40 = 0
            redVoidGrubKillVariable_60 = 0
            redVoidGrubKillVariable_80 = 0

            # blueRiftHeraldKill, redRiftHeraldKill
            blueRiftHeraldKillVariable_20 = 0
            blueRiftHeraldKillVariable_40 = 0
            blueRiftHeraldKillVariable_60 = 0
            blueRiftHeraldKillVariable_80 = 0
            redRiftHeraldKillVariable_20 = 0
            redRiftHeraldKillVariable_40 = 0
            redRiftHeraldKillVariable_60 = 0
            redRiftHeraldKillVariable_80 = 0

            # blueBaronKill, redBaronKill
            blueBaronKillVariable_20 = 0
            blueBaronKillVariable_40 = 0
            blueBaronKillVariable_60 = 0
            blueBaronKillVariable_80 = 0
            redBaronKillVariable_20 = 0
            redBaronKillVariable_40 = 0
            redBaronKillVariable_60 = 0
            redBaronKillVariable_80 = 0

            # blueTowerKill, redTowerKill
            blueTowerKillVariable_20 = 0
            blueTowerKillVariable_40 = 0
            blueTowerKillVariable_60 = 0
            blueTowerKillVariable_80 = 0
            redTowerKillVariable_20 = 0
            redTowerKillVariable_40 = 0
            redTowerKillVariable_60 = 0
            redTowerKillVariable_80 = 0

            # blueInhibitorKill, redInhibitorKill
            blueInhibitorKillVariable_20 = 0
            blueInhibitorKillVariable_40 = 0
            blueInhibitorKillVariable_60 = 0
            blueInhibitorKillVariable_80 = 0
            redInhibitorKillVariable_20 = 0
            redInhibitorKillVariable_40 = 0
            redInhibitorKillVariable_60 = 0
            redInhibitorKillVariable_80 = 0

            # blueTotalGold, redTotalGold
            blueTotalGoldVariable_20 = 0
            blueTotalGoldVariable_40 = 0
            blueTotalGoldVariable_60 = 0
            blueTotalGoldVariable_80 = 0
            redTotalGoldVariable_20 = 0
            redTotalGoldVariable_40 = 0
            redTotalGoldVariable_60 = 0
            redTotalGoldVariable_80 = 0

            # blueMinionsKilled, redMinionsKilled
            blueMinionsKilledVariable_20 = 0
            blueMinionsKilledVariable_40 = 0
            blueMinionsKilledVariable_60 = 0
            blueMinionsKilledVariable_80 = 0
            redMinionsKilledVariable_20 = 0
            redMinionsKilledVariable_40 = 0
            redMinionsKilledVariable_60 = 0
            redMinionsKilledVariable_80 = 0

            # blueJungleMinionsKilled, redJungleMinionsKilled
            blueJungleMinionsKilledVariable_20 = 0
            blueJungleMinionsKilledVariable_40 = 0
            blueJungleMinionsKilledVariable_60 = 0
            blueJungleMinionsKilledVariable_80 = 0
            redJungleMinionsKilledVariable_20 = 0
            redJungleMinionsKilledVariable_40 = 0
            redJungleMinionsKilledVariable_60 = 0
            redJungleMinionsKilledVariable_80 = 0

            # blueAvgPlayerLevel, redAvgPlayerLevel
            blueAvgPlayerLevelVariable_20 = 0
            blueAvgPlayerLevelVariable_40 = 0
            blueAvgPlayerLevelVariable_60 = 0
            blueAvgPlayerLevelVariable_80 = 0
            redAvgPlayerLevelVariable_20 = 0
            redAvgPlayerLevelVariable_40 = 0
            redAvgPlayerLevelVariable_60 = 0
            redAvgPlayerLevelVariable_80 = 0

        # For time
            # blueChampionKill, redChampionKill
            blueChampionKillVariable_min10 = 0
            blueChampionKillVariable_min14 = 0
            blueChampionKillVariable_min20 = 0
            blueChampionKillVariable_min27 = 0
            redChampionKillVariable_min10 = 0
            redChampionKillVariable_min14 = 0
            redChampionKillVariable_min20 = 0
            redChampionKillVariable_min27 = 0

            # blueDragonKill, redDragonKill
            blueDragonKillVariable_min10 = 0
            blueDragonKillVariable_min14 = 0
            blueDragonKillVariable_min20 = 0
            blueDragonKillVariable_min27 = 0
            redDragonKillVariable_min10 = 0
            redDragonKillVariable_min14 = 0
            redDragonKillVariable_min20 = 0
            redDragonKillVariable_min27 = 0

            # blueDragonHextechKill, redDragonHextechKill
            blueDragonHextechKillVariable_min10 = 0
            blueDragonHextechKillVariable_min14 = 0
            blueDragonHextechKillVariable_min20 = 0
            blueDragonHextechKillVariable_min27 = 0
            redDragonHextechKillVariable_min10 = 0
            redDragonHextechKillVariable_min14 = 0
            redDragonHextechKillVariable_min20 = 0
            redDragonHextechKillVariable_min27 = 0

            # blueDragonChemtechKill, redDragonChemtechKill
            blueDragonChemtechKillVariable_min10 = 0
            blueDragonChemtechKillVariable_min14 = 0
            blueDragonChemtechKillVariable_min20 = 0
            blueDragonChemtechKillVariable_min27 = 0
            redDragonChemtechKillVariable_min10 = 0
            redDragonChemtechKillVariable_min14 = 0
            redDragonChemtechKillVariable_min20 = 0
            redDragonChemtechKillVariable_min27 = 0

            # blueDragonFireKill, redDragonFireKill
            blueDragonFireKillVariable_min10 = 0
            blueDragonFireKillVariable_min14 = 0
            blueDragonFireKillVariable_min20 = 0
            blueDragonFireKillVariable_min27 = 0
            redDragonFireKillVariable_min10 = 0
            redDragonFireKillVariable_min14 = 0
            redDragonFireKillVariable_min20 = 0
            redDragonFireKillVariable_min27 = 0

            # blueDragonAirKill, redDragonAirKill
            blueDragonAirKillVariable_min10 = 0
            blueDragonAirKillVariable_min14 = 0
            blueDragonAirKillVariable_min20 = 0
            blueDragonAirKillVariable_min27 = 0
            redDragonAirKillVariable_min10 = 0
            redDragonAirKillVariable_min14 = 0
            redDragonAirKillVariable_min20 = 0
            redDragonAirKillVariable_min27 = 0

            # blueDragonEarthKill, redDragonEarthKill
            blueDragonEarthKillVariable_min10 = 0
            blueDragonEarthKillVariable_min14 = 0
            blueDragonEarthKillVariable_min20 = 0
            blueDragonEarthKillVariable_min27 = 0
            redDragonEarthKillVariable_min10 = 0
            redDragonEarthKillVariable_min14 = 0
            redDragonEarthKillVariable_min20 = 0
            redDragonEarthKillVariable_min27 = 0

            # blueDragonWaterKill, redDragonWaterKill
            blueDragonWaterKillVariable_min10 = 0
            blueDragonWaterKillVariable_min14 = 0
            blueDragonWaterKillVariable_min20 = 0
            blueDragonWaterKillVariable_min27 = 0
            redDragonWaterKillVariable_min10 = 0
            redDragonWaterKillVariable_min14 = 0
            redDragonWaterKillVariable_min20 = 0
            redDragonWaterKillVariable_min27 = 0

            # blueDragonElderKill, redDragonElderKill
            blueDragonElderKillVariable_min10 = 0
            blueDragonElderKillVariable_min14 = 0
            blueDragonElderKillVariable_min20 = 0
            blueDragonElderKillVariable_min27 = 0
            redDragonElderKillVariable_min10 = 0
            redDragonElderKillVariable_min14 = 0
            redDragonElderKillVariable_min20 = 0
            redDragonElderKillVariable_min27 = 0

            # blueVoidGrubKill, redVoidGrubKill
            blueVoidGrubKillVariable_min10 = 0
            blueVoidGrubKillVariable_min14 = 0
            blueVoidGrubKillVariable_min20 = 0
            blueVoidGrubKillVariable_min27 = 0
            redVoidGrubKillVariable_min10 = 0
            redVoidGrubKillVariable_min14 = 0
            redVoidGrubKillVariable_min20 = 0
            redVoidGrubKillVariable_min27 = 0

            # blueRiftHeraldKill, redRiftHeraldKill
            blueRiftHeraldKillVariable_min10 = 0
            blueRiftHeraldKillVariable_min14 = 0
            blueRiftHeraldKillVariable_min20 = 0
            blueRiftHeraldKillVariable_min27 = 0
            redRiftHeraldKillVariable_min10 = 0
            redRiftHeraldKillVariable_min14 = 0
            redRiftHeraldKillVariable_min20 = 0
            redRiftHeraldKillVariable_min27 = 0

            # blueBaronKill, redBaronKill
            blueBaronKillVariable_min10 = 0
            blueBaronKillVariable_min14 = 0
            blueBaronKillVariable_min20 = 0
            blueBaronKillVariable_min27 = 0
            redBaronKillVariable_min10 = 0
            redBaronKillVariable_min14 = 0
            redBaronKillVariable_min20 = 0
            redBaronKillVariable_min27 = 0

            # blueTowerKill, redTowerKill
            blueTowerKillVariable_min10 = 0
            blueTowerKillVariable_min14 = 0
            blueTowerKillVariable_min20 = 0
            blueTowerKillVariable_min27 = 0
            redTowerKillVariable_min10 = 0
            redTowerKillVariable_min14 = 0
            redTowerKillVariable_min20 = 0
            redTowerKillVariable_min27 = 0

            # blueInhibitorKill, redInhibitorKill
            blueInhibitorKillVariable_min10 = 0
            blueInhibitorKillVariable_min14 = 0
            blueInhibitorKillVariable_min20 = 0
            blueInhibitorKillVariable_min27 = 0
            redInhibitorKillVariable_min10 = 0
            redInhibitorKillVariable_min14 = 0
            redInhibitorKillVariable_min20 = 0
            redInhibitorKillVariable_min27 = 0

            # blueTotalGold, redTotalGold
            blueTotalGoldVariable_min10 = 0
            blueTotalGoldVariable_min14 = 0
            blueTotalGoldVariable_min20 = 0
            blueTotalGoldVariable_min27 = 0
            redTotalGoldVariable_min10 = 0
            redTotalGoldVariable_min14 = 0
            redTotalGoldVariable_min20 = 0
            redTotalGoldVariable_min27 = 0

            # blueMinionsKilled, redMinionsKilled
            blueMinionsKilledVariable_min10 = 0
            blueMinionsKilledVariable_min14 = 0
            blueMinionsKilledVariable_min20 = 0
            blueMinionsKilledVariable_min27 = 0
            redMinionsKilledVariable_min10 = 0
            redMinionsKilledVariable_min14 = 0
            redMinionsKilledVariable_min20 = 0
            redMinionsKilledVariable_min27 = 0

            # blueJungleMinionsKilled, redJungleMinionsKilled
            blueJungleMinionsKilledVariable_min10 = 0
            blueJungleMinionsKilledVariable_min14 = 0
            blueJungleMinionsKilledVariable_min20 = 0
            blueJungleMinionsKilledVariable_min27 = 0
            redJungleMinionsKilledVariable_min10 = 0
            redJungleMinionsKilledVariable_min14 = 0
            redJungleMinionsKilledVariable_min20 = 0
            redJungleMinionsKilledVariable_min27 = 0

            # blueAvgPlayerLevel, redAvgPlayerLevel
            blueAvgPlayerLevelVariable_min10 = 0
            blueAvgPlayerLevelVariable_min14 = 0
            blueAvgPlayerLevelVariable_min20 = 0
            blueAvgPlayerLevelVariable_min27 = 0
            redAvgPlayerLevelVariable_min10 = 0
            redAvgPlayerLevelVariable_min14 = 0
            redAvgPlayerLevelVariable_min20 = 0
            redAvgPlayerLevelVariable_min27 = 0

        


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
            timeIntervalPercentages = [10, 14, 20, 27]

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
                lastTimeStamp = 60000 * timeInterval

        # Code: timeStamp
                if timeInterval == 10:
                    timeStamp_20.append(int(lastTimeStamp))
                elif timeInterval == 14:
                    timeStamp_40.append(int(lastTimeStamp))
                elif timeInterval == 20:
                    timeStamp_60.append(int(lastTimeStamp))
                elif timeInterval == 27:
                    timeStamp_80.append(int(lastTimeStamp))
                
                exitLoop = False
                for frame in game_timeline['info']['frames']:
                    for event in frame['events']:

        # Code: blueChampionKill, redChampionKill
                        if event['type'] == 'CHAMPION_KILL' and event['timestamp'] <= lastTimeStamp:
                            if event['killerId'] in blueTeamPlayerIds:
                                if timeInterval == 10:
                                    blueChampionKillVariable_20 += 1
                                elif timeInterval == 14:
                                    blueChampionKillVariable_40 += 1
                                elif timeInterval == 20:
                                    blueChampionKillVariable_60 += 1
                                elif timeInterval == 27:
                                    blueChampionKillVariable_80 += 1
                            elif event['killerId'] in redTeamPlayerIds:
                                if timeInterval == 10:
                                    redChampionKillVariable_20 += 1
                                elif timeInterval == 14:
                                    redChampionKillVariable_40 += 1
                                elif timeInterval == 20:
                                    redChampionKillVariable_60 += 1
                                elif timeInterval == 27:
                                    redChampionKillVariable_80 += 1
        # Code: blueDragonKill, redDragonKill, blueDragonHextechKill, redDragonHextechKill, blueDragonChemtechKill, redDragonChemtechKill, blueDragonFireKill, redDragonFireKill, blueDragonAirKill, redDragonAirKill, blueDragonEarthKill, redDragonEarthKill, blueDragonWaterKill, redDragonWaterKill, blueDragonElderKill, redDragonElderKill, blueVoidGrubKill, redVoidGrubKill, blueRiftHeraldKill, redRiftHeraldKill, blueBaronKill, redBaronKill
                        elif event['type'] == 'ELITE_MONSTER_KILL' and event['timestamp'] <= lastTimeStamp:
        # Code: blue team
                            if event['monsterType'] == 'DRAGON':
        # Code: blueDragonKill
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 10:
                                        blueDragonKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        blueDragonKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        blueDragonKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        blueDragonKillVariable_80 += 1
        # Code: blueDragonHextechKill
                                    if event['monsterSubType'] == 'HEXTECH_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonHextechKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonHextechKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonHextechKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonHextechKillVariable_80 += 1
        # Code: blueDragonChemtechKill
                                    if event['monsterSubType'] == 'CHEMTECH_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonChemtechKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonChemtechKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonChemtechKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonChemtechKillVariable_80 += 1
        # Code: blueDragonFireKill
                                    if event['monsterSubType'] == 'FIRE_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonFireKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonFireKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonFireKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonFireKillVariable_80 += 1
        # Code: blueDragonAirKill
                                    if event['monsterSubType'] == 'AIR_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonAirKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonAirKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonAirKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonAirKillVariable_80 += 1
        # Code: blueDragonEarthKill
                                    if event['monsterSubType'] == 'EARTH_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonEarthKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonEarthKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonEarthKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonEarthKillVariable_80 += 1
        # Code: blueDragonWaterKill
                                    if event['monsterSubType'] == 'WATER_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonWaterKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonWaterKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonWaterKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonWaterKillVariable_80 += 1
        # Code: blueDragonElderKill
                                    if event['monsterSubType'] == 'ELDER_DRAGON':
                                        if timeInterval == 10:
                                            blueDragonElderKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            blueDragonElderKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            blueDragonElderKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            blueDragonElderKillVariable_80 += 1
        # Code: blueVoidGrubKill
                            elif event['monsterType'] == 'HORDE':
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 10:
                                        blueVoidGrubKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        blueVoidGrubKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        blueVoidGrubKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        blueVoidGrubKillVariable_80 += 1
        # Code: blueRiftHeraldKill
                            elif event['monsterType'] == 'RIFTHERALD':
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 10:
                                        blueRiftHeraldKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        blueRiftHeraldKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        blueRiftHeraldKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        blueRiftHeraldKillVariable_80 += 1
        # Code: blueBaronKill
                            elif event['monsterType'] == 'BARON_NASHOR':
                                if event['killerId'] in blueTeamPlayerIds:
                                    if timeInterval == 10:
                                        blueBaronKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        blueBaronKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        blueBaronKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        blueBaronKillVariable_80 += 1
        # Code: red team
                            if event['monsterType'] == 'DRAGON':
        # Code: redDragonKill
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 10:
                                        redDragonKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        redDragonKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        redDragonKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        redDragonKillVariable_80 += 1
        # Code: redDragonHextechKill
                                    if event['monsterSubType'] == 'HEXTECH_DRAGON':
                                        if timeInterval == 10:
                                            redDragonHextechKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonHextechKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonHextechKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonHextechKillVariable_80 += 1
        # Code: redDragonChemtechKill
                                    if event['monsterSubType'] == 'CHEMTECH_DRAGON':
                                        if timeInterval == 10:
                                            redDragonChemtechKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonChemtechKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonChemtechKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonChemtechKillVariable_80 += 1
        # Code: redDragonFireKill
                                    if event['monsterSubType'] == 'FIRE_DRAGON':
                                        if timeInterval == 10:
                                            redDragonFireKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonFireKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonFireKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonFireKillVariable_80 += 1
        # Code: redDragonAirKill
                                    if event['monsterSubType'] == 'AIR_DRAGON':
                                        if timeInterval == 10:
                                            redDragonAirKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonAirKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonAirKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonAirKillVariable_80 += 1
        # Code: redDragonEarthKill
                                    if event['monsterSubType'] == 'EARTH_DRAGON':
                                        if timeInterval == 10:
                                            redDragonEarthKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonEarthKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonEarthKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonEarthKillVariable_80 += 1
        # Code: redDragonWaterKill
                                    if event['monsterSubType'] == 'WATER_DRAGON':
                                        if timeInterval == 10:
                                            redDragonWaterKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonWaterKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonWaterKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonWaterKillVariable_80 += 1
        # Code: redDragonElderKill
                                    if event['monsterSubType'] == 'ELDER_DRAGON':
                                        if timeInterval == 10:
                                            redDragonElderKillVariable_20 += 1
                                        elif timeInterval == 14:
                                            redDragonElderKillVariable_40 += 1
                                        elif timeInterval == 20:
                                            redDragonElderKillVariable_60 += 1
                                        elif timeInterval == 27:
                                            redDragonElderKillVariable_80 += 1
        # Code: redVoidGrubKill
                            elif event['monsterType'] == 'HORDE':
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 10:
                                        redVoidGrubKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        redVoidGrubKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        redVoidGrubKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        redVoidGrubKillVariable_80 += 1
        # Code: redRiftHeraldKill
                            elif event['monsterType'] == 'RIFTHERALD':
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 10:
                                        redRiftHeraldKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        redRiftHeraldKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        redRiftHeraldKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        redRiftHeraldKillVariable_80 += 1
        # Code: redBaronKill
                            elif event['monsterType'] == 'BARON_NASHOR':
                                if event['killerId'] in redTeamPlayerIds:
                                    if timeInterval == 10:
                                        redBaronKillVariable_20 += 1
                                    elif timeInterval == 14:
                                        redBaronKillVariable_40 += 1
                                    elif timeInterval == 20:
                                        redBaronKillVariable_60 += 1
                                    elif timeInterval == 27:
                                        redBaronKillVariable_80 += 1

        # Code: blueTowerKill, redTowerKill, blueInhibitorKill, redInhibitorKill
                        if event['type'] == 'BUILDING_KILL' and event['timestamp'] <= lastTimeStamp:
        # Code: blueTowerKill, redTowerKill
                            if event['buildingType'] == 'TOWER_BUILDING' and event['teamId'] == 200:
                                if timeInterval == 10:
                                    blueTowerKillVariable_20 += 1
                                elif timeInterval == 14:
                                    blueTowerKillVariable_40 += 1
                                elif timeInterval == 20:
                                    blueTowerKillVariable_60 += 1
                                elif timeInterval == 27:
                                    blueTowerKillVariable_80 += 1

                            elif event['buildingType'] == 'TOWER_BUILDING' and event['teamId'] == 100:
                                if timeInterval == 10:
                                    redTowerKillVariable_20 += 1
                                elif timeInterval == 14:
                                    redTowerKillVariable_40 += 1
                                elif timeInterval == 20:
                                    redTowerKillVariable_60 += 1
                                elif timeInterval == 27:
                                    redTowerKillVariable_80 += 1
        # Code: blueInhibitorKill, redInhibitorKill
                            elif event['buildingType'] == 'INHIBITOR_BUILDING' and event['teamId'] == 200:
                                if timeInterval == 10:
                                    blueInhibitorKillVariable_20 += 1
                                elif timeInterval == 14:
                                    blueInhibitorKillVariable_40 += 1
                                elif timeInterval == 20:
                                    blueInhibitorKillVariable_60 += 1
                                elif timeInterval == 27:
                                    blueInhibitorKillVariable_80 += 1

                            elif event['buildingType'] == 'INHIBITOR_BUILDING' and event['teamId'] == 100:
                                if timeInterval == 10:
                                    redInhibitorKillVariable_20 += 1
                                elif timeInterval == 14:
                                    redInhibitorKillVariable_40 += 1
                                elif timeInterval == 20:
                                    redInhibitorKillVariable_60 += 1
                                elif timeInterval == 27:
                                    redInhibitorKillVariable_80 += 1
        
        # Code: blueTotalGold, redTotalGold, blueMinionsKilled, redMinionsKilled, blueJungleMinionsKilled, redJungleMinionsKilled, blueAvgPlayerLevel, redAvgPlayerLevel
                    currentTimeStamp = frame['timestamp']
                    if currentTimeStamp >= lastTimeStamp:
                        if timeInterval == 10:
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
                        elif timeInterval == 14:
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
                        elif timeInterval == 20:
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
                        elif timeInterval == 27:
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
            blueChampionKill_20.append(blueChampionKillVariable_20)
            blueChampionKill_40.append(blueChampionKillVariable_40)
            blueChampionKill_60.append(blueChampionKillVariable_60)
            blueChampionKill_80.append(blueChampionKillVariable_80)

            # blueFirstBlood_timeInterval (fixed)
            blueFirstBlood.append(blueFirstBloodVariable)

            # blueDragonKill_timeInterval
            blueDragonKill_20.append(blueDragonKillVariable_20)
            blueDragonKill_40.append(blueDragonKillVariable_40)
            blueDragonKill_60.append(blueDragonKillVariable_60)
            blueDragonKill_80.append(blueDragonKillVariable_80)

            # blueDragonHextechKill_timeInterval
            blueDragonHextechKill_20.append(blueDragonHextechKillVariable_20)
            blueDragonHextechKill_40.append(blueDragonHextechKillVariable_40)
            blueDragonHextechKill_60.append(blueDragonHextechKillVariable_60)
            blueDragonHextechKill_80.append(blueDragonHextechKillVariable_80)

            # blueDragonChemtechKill_timeInterval
            blueDragonChemtechKill_20.append(blueDragonChemtechKillVariable_20)
            blueDragonChemtechKill_40.append(blueDragonChemtechKillVariable_40)
            blueDragonChemtechKill_60.append(blueDragonChemtechKillVariable_60)
            blueDragonChemtechKill_80.append(blueDragonChemtechKillVariable_80)

            # blueDragonFireKill_timeInterval
            blueDragonFireKill_20.append(blueDragonFireKillVariable_20)
            blueDragonFireKill_40.append(blueDragonFireKillVariable_40)
            blueDragonFireKill_60.append(blueDragonFireKillVariable_60)
            blueDragonFireKill_80.append(blueDragonFireKillVariable_80)

            # blueDragonAirKill_timeInterval
            blueDragonAirKill_20.append(blueDragonAirKillVariable_20)
            blueDragonAirKill_40.append(blueDragonAirKillVariable_40)
            blueDragonAirKill_60.append(blueDragonAirKillVariable_60)
            blueDragonAirKill_80.append(blueDragonAirKillVariable_80)

            # blueDragonEarthKill_timeInterval
            blueDragonEarthKill_20.append(blueDragonEarthKillVariable_20)
            blueDragonEarthKill_40.append(blueDragonEarthKillVariable_40)
            blueDragonEarthKill_60.append(blueDragonEarthKillVariable_60)
            blueDragonEarthKill_80.append(blueDragonEarthKillVariable_80)

            # blueDragonWaterKill_timeInterval
            blueDragonWaterKill_20.append(blueDragonWaterKillVariable_20)
            blueDragonWaterKill_40.append(blueDragonWaterKillVariable_40)
            blueDragonWaterKill_60.append(blueDragonWaterKillVariable_60)
            blueDragonWaterKill_80.append(blueDragonWaterKillVariable_80)

            # blueDragonElderKill_timeInterval
            blueDragonElderKill_20.append(blueDragonElderKillVariable_20)
            blueDragonElderKill_40.append(blueDragonElderKillVariable_40)
            blueDragonElderKill_60.append(blueDragonElderKillVariable_60)
            blueDragonElderKill_80.append(blueDragonElderKillVariable_80)

            # blueVoidGrubKill_timeInterval
            blueVoidGrubKill_20.append(blueVoidGrubKillVariable_20)
            blueVoidGrubKill_40.append(blueVoidGrubKillVariable_40)
            blueVoidGrubKill_60.append(blueVoidGrubKillVariable_60)
            blueVoidGrubKill_80.append(blueVoidGrubKillVariable_80)

            # blueRiftHeraldKill_timeInterval
            blueRiftHeraldKill_20.append(blueRiftHeraldKillVariable_20)
            blueRiftHeraldKill_40.append(blueRiftHeraldKillVariable_40)
            blueRiftHeraldKill_60.append(blueRiftHeraldKillVariable_60)
            blueRiftHeraldKill_80.append(blueRiftHeraldKillVariable_80)

            # blueBaronKill_timeInterval
            blueBaronKill_20.append(blueBaronKillVariable_20)
            blueBaronKill_40.append(blueBaronKillVariable_40)
            blueBaronKill_60.append(blueBaronKillVariable_60)
            blueBaronKill_80.append(blueBaronKillVariable_80)

            # blueTowerKill_timeInterval
            blueTowerKill_20.append(blueTowerKillVariable_20)
            blueTowerKill_40.append(blueTowerKillVariable_40)
            blueTowerKill_60.append(blueTowerKillVariable_60)
            blueTowerKill_80.append(blueTowerKillVariable_80)

            # blueInhibitorKill_timeInterval
            blueInhibitorKill_20.append(blueInhibitorKillVariable_20)
            blueInhibitorKill_40.append(blueInhibitorKillVariable_40)
            blueInhibitorKill_60.append(blueInhibitorKillVariable_60)
            blueInhibitorKill_80.append(blueInhibitorKillVariable_80)

            # blueTotalGold_timeInterval
            blueTotalGold_20.append(blueTotalGoldVariable_20)
            blueTotalGold_40.append(blueTotalGoldVariable_40)
            blueTotalGold_60.append(blueTotalGoldVariable_60)
            blueTotalGold_80.append(blueTotalGoldVariable_80)

            # blueMinionsKilled_timeInterval
            blueMinionsKilled_20.append(blueMinionsKilledVariable_20)
            blueMinionsKilled_40.append(blueMinionsKilledVariable_40)
            blueMinionsKilled_60.append(blueMinionsKilledVariable_60)
            blueMinionsKilled_80.append(blueMinionsKilledVariable_80)

            # blueJungleMinionsKilled_timeInterval
            blueJungleMinionsKilled_20.append(blueJungleMinionsKilledVariable_20)
            blueJungleMinionsKilled_40.append(blueJungleMinionsKilledVariable_40)
            blueJungleMinionsKilled_60.append(blueJungleMinionsKilledVariable_60)
            blueJungleMinionsKilled_80.append(blueJungleMinionsKilledVariable_80)

            # blueAvgPlayerLevel_timeInterval
            blueAvgPlayerLevel_20.append(blueAvgPlayerLevelVariable_20)
            blueAvgPlayerLevel_40.append(blueAvgPlayerLevelVariable_40)
            blueAvgPlayerLevel_60.append(blueAvgPlayerLevelVariable_60)
            blueAvgPlayerLevel_80.append(blueAvgPlayerLevelVariable_80)

            # blueWin_timeInterval (fixed)
            blueWin.append(blueWinVariable)

            # redChampionKill_timeInterval
            redChampionKill_20.append(redChampionKillVariable_20)
            redChampionKill_40.append(redChampionKillVariable_40)
            redChampionKill_60.append(redChampionKillVariable_60)
            redChampionKill_80.append(redChampionKillVariable_80)

            # redFirstBlood_timeInterval (fixed)
            redFirstBlood.append(redFirstBloodVariable)

            # redDragonKill_timeInterval
            redDragonKill_20.append(redDragonKillVariable_20)
            redDragonKill_40.append(redDragonKillVariable_40)
            redDragonKill_60.append(redDragonKillVariable_60)
            redDragonKill_80.append(redDragonKillVariable_80)

            # redDragonHextechKill_timeInterval
            redDragonHextechKill_20.append(redDragonHextechKillVariable_20)
            redDragonHextechKill_40.append(redDragonHextechKillVariable_40)
            redDragonHextechKill_60.append(redDragonHextechKillVariable_60)
            redDragonHextechKill_80.append(redDragonHextechKillVariable_80)

            # redDragonChemtechKill_timeInterval
            redDragonChemtechKill_20.append(redDragonChemtechKillVariable_20)
            redDragonChemtechKill_40.append(redDragonChemtechKillVariable_40)
            redDragonChemtechKill_60.append(redDragonChemtechKillVariable_60)
            redDragonChemtechKill_80.append(redDragonChemtechKillVariable_80)

            # redDragonFireKill_timeInterval
            redDragonFireKill_20.append(redDragonFireKillVariable_20)
            redDragonFireKill_40.append(redDragonFireKillVariable_40)
            redDragonFireKill_60.append(redDragonFireKillVariable_60)
            redDragonFireKill_80.append(redDragonFireKillVariable_80)

            # redDragonAirKill_timeInterval
            redDragonAirKill_20.append(redDragonAirKillVariable_20)
            redDragonAirKill_40.append(redDragonAirKillVariable_40)
            redDragonAirKill_60.append(redDragonAirKillVariable_60)
            redDragonAirKill_80.append(redDragonAirKillVariable_80)

            # redDragonEarthKill_timeInterval
            redDragonEarthKill_20.append(redDragonEarthKillVariable_20)
            redDragonEarthKill_40.append(redDragonEarthKillVariable_40)
            redDragonEarthKill_60.append(redDragonEarthKillVariable_60)
            redDragonEarthKill_80.append(redDragonEarthKillVariable_80)

            # redDragonWaterKill_timeInterval
            redDragonWaterKill_20.append(redDragonWaterKillVariable_20)
            redDragonWaterKill_40.append(redDragonWaterKillVariable_40)
            redDragonWaterKill_60.append(redDragonWaterKillVariable_60)
            redDragonWaterKill_80.append(redDragonWaterKillVariable_80)

            # redDragonElderKill_timeInterval
            redDragonElderKill_20.append(redDragonElderKillVariable_20)
            redDragonElderKill_40.append(redDragonElderKillVariable_40)
            redDragonElderKill_60.append(redDragonElderKillVariable_60)
            redDragonElderKill_80.append(redDragonElderKillVariable_80)

            # redVoidGrubKill_timeInterval
            redVoidGrubKill_20.append(redVoidGrubKillVariable_20)
            redVoidGrubKill_40.append(redVoidGrubKillVariable_40)
            redVoidGrubKill_60.append(redVoidGrubKillVariable_60)
            redVoidGrubKill_80.append(redVoidGrubKillVariable_80)

            # redRiftHeraldKill_timeInterval
            redRiftHeraldKill_20.append(redRiftHeraldKillVariable_20)
            redRiftHeraldKill_40.append(redRiftHeraldKillVariable_40)
            redRiftHeraldKill_60.append(redRiftHeraldKillVariable_60)
            redRiftHeraldKill_80.append(redRiftHeraldKillVariable_80)

            # redBaronKill_timeInterval
            redBaronKill_20.append(redBaronKillVariable_20)
            redBaronKill_40.append(redBaronKillVariable_40)
            redBaronKill_60.append(redBaronKillVariable_60)
            redBaronKill_80.append(redBaronKillVariable_80)

            # redTowerKill_timeInterval
            redTowerKill_20.append(redTowerKillVariable_20)
            redTowerKill_40.append(redTowerKillVariable_40)
            redTowerKill_60.append(redTowerKillVariable_60)
            redTowerKill_80.append(redTowerKillVariable_80)

            # redInhibitorKill_timeInterval
            redInhibitorKill_20.append(redInhibitorKillVariable_20)
            redInhibitorKill_40.append(redInhibitorKillVariable_40)
            redInhibitorKill_60.append(redInhibitorKillVariable_60)
            redInhibitorKill_80.append(redInhibitorKillVariable_80)

            # redTotalGold_timeInterval
            redTotalGold_20.append(redTotalGoldVariable_20)
            redTotalGold_40.append(redTotalGoldVariable_40)
            redTotalGold_60.append(redTotalGoldVariable_60)
            redTotalGold_80.append(redTotalGoldVariable_80)

            # redMinionsKilled_timeInterval
            redMinionsKilled_20.append(redMinionsKilledVariable_20)
            redMinionsKilled_40.append(redMinionsKilledVariable_40)
            redMinionsKilled_60.append(redMinionsKilledVariable_60)
            redMinionsKilled_80.append(redMinionsKilledVariable_80)

            # redJungleMinionsKilled_timeInterval
            redJungleMinionsKilled_20.append(redJungleMinionsKilledVariable_20)
            redJungleMinionsKilled_40.append(redJungleMinionsKilledVariable_40)
            redJungleMinionsKilled_60.append(redJungleMinionsKilledVariable_60)
            redJungleMinionsKilled_80.append(redJungleMinionsKilledVariable_80)

            # redAvgPlayerLevel_timeInterval
            redAvgPlayerLevel_20.append(redAvgPlayerLevelVariable_20)
            redAvgPlayerLevel_40.append(redAvgPlayerLevelVariable_40)
            redAvgPlayerLevel_60.append(redAvgPlayerLevelVariable_60)
            redAvgPlayerLevel_80.append(redAvgPlayerLevelVariable_80)

            # redWin_timeInterval (fixed)
            redWin.append(redWinVariable)





    # Write firstLine into csv
    # Game interval csv files
        with(open(name_for_file_20, mode='w', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_40, mode='w', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_60, mode='w', newline='')) as f:
            writer = csv.writer(f)
            writer.writerow(firstLine.split(','))

        with(open(name_for_file_80, mode='w', newline='')) as f:
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

    
    end_time = time.time()
    runtime = end_time - start_time
    print(f'Runtime: {runtime}')
            
if __name__ == '__main__':
    main()
import csv

# 20, 40, 60, 80, 100, end, min10, min14, min20, min27
file_name_ending_list1 = ['20', '40', '60', '80', '100']
file_name_ending_list2 = ['end', 'min10', 'min14', 'min20', 'min27']
#file_name_ending = '20'
# BR1, EUN1, EUW1, JP1, KR, LA1, LA2, NA1, OC1, PH2, RU, SG2, TH2, TR1, VN2
region = 'VN2'
region_associated_number = '15'
# timeInterval, timeStamp_
prefix_list = ['timeStamp_']
#prefix = 'timeStamp_'
# 4, 5
prefix_associated_number_list = ['5']
#prefix_associated_number = '4'

numbers_list = [1, 2]

for i2, prefix in enumerate(prefix_list):
    if i2 == 0:
        file_name_ending_list = file_name_ending_list2 # end, min10, min14, min20, min27
    elif i2 == 1:
        file_name_ending_list = file_name_ending_list1 # 20, 40, 60, 80, 100
        
    for file_name_ending in file_name_ending_list:
        for number in numbers_list:
            print(i2)
            input_file_name = f'{prefix_associated_number_list[i2]}_new_dataset_{file_name_ending}({region}_game_ids_{number}).csv'
            output_file_name = f'test{number}.csv'
            size_over_500 = f'./{region}/{prefix}{file_name_ending}/{input_file_name}'
            size_under_500 = f'./{region}/{input_file_name}'
    
            # Reading file
            with open(size_over_500, 'r') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
    
            # Modify rows
            for i, row in enumerate(rows):
                if i == 0:
                    pass
    
                elif i != 0:
                    if len(rows[i][0]) == 1:
                        rows[i][0] = f'00{rows[i][0]}'
    
                    elif len(rows[i][0]) == 2:
                        rows[i][0] = f'0{rows[i][0]}'
    
    
                    if number < 10:
                        number_for_region_subclass = f'0{number}'
                        rows[i][0] = f'{region_associated_number}{number_for_region_subclass}{rows[i][0]}'
    
                    elif number >= 10:
                        number_for_region_subclass = f'{number}'
                        rows[i][0] = f'{region_associated_number}{number_for_region_subclass}{rows[i][0]}'
    
            # Writing file
            with open(size_over_500, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
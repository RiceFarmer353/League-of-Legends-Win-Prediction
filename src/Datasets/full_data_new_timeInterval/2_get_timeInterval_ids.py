import csv

with open('full_data_new_100.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)[1:]

    for i in data:
        if int(i[2]) > 1620000:
            with open('2_game_ids_for_timeStamp.txt', 'a', newline='') as file:
                file.write(i[1] + '\n')
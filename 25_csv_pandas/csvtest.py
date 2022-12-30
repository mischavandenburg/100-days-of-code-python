# list = []
#
# with open("weather_data.csv") as f:
#     for line in f:
#         list.append(f.readline())
#
# print(list)

import csv

temperatures = []

with open("weather_data.csv") as f:
    data = csv.reader(f)
    for row in data:
        if "temp" not in row:
            temperatures.append(int(row[1]))

print(temperatures)

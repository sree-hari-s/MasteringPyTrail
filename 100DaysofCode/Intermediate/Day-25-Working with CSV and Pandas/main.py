# with open('weather_data.csv', 'r') as file:
#     data=file.readlines()
    
# print(data)

import csv

with open('weather_data.csv', 'r') as data_file:
    data= csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1]!='temp':
            temperature.append(int(row[1]))
    print(temperature)
    
"""
Pandas library
"""

import pandas as pd

new_data = pd.read_csv('weather_data.csv')
print(type(new_data))
print(new_data['temp'])

"""
2 type of datatypes in Pandas
Data frame and Series

Series is a single column of data.
Whole table is a Dataframe
"""

data_dict = new_data.to_dict()
print(data_dict)

temp_list = new_data['temp'].to_list()
print(len(temp_list))
print(sum(temp_list)/len(temp_list))
print(new_data['temp'].mean())
print(new_data['temp'].max())

# Get data in columns

print(new_data['condition'])
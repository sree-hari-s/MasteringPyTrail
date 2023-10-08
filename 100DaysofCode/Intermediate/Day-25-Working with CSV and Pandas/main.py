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
    print('temperature',temperature)
    
"""
Pandas library
"""

import pandas as pd

new_data = pd.read_csv('weather_data.csv')
print(type(new_data))
print("temperature data using pandas ",new_data['temp'])

"""
2 type of datatypes in Pandas
Data frame and Series

Series is a single column of data.
Whole table is a Dataframe
"""

data_dict = new_data.to_dict()
print("Data in dictionary",data_dict)

temp_list = new_data['temp'].to_list()
print("length of temperature data",len(temp_list))
print("Average using sum/len",sum(temp_list)/len(temp_list))
print("Average using mean function",new_data['temp'].mean())
print("Maximum temperature data",new_data['temp'].max())

# Get data in columns

print("Accessing column data #1\n",new_data['condition'])
print("Accessing column data #2\n",new_data.condition)

# Get data in Rows

print("Monday ",new_data[new_data.day == 'Monday'])

print(new_data[new_data.temp == new_data.temp.max()])

# TODO: Convert Monday's temperature to Fahrenheit.

def celsius_to_fahrenheit(temp):
    new_temp = (temp*(9/5)) + 32
    return new_temp

print("Temperature Monday :",new_data[new_data.day == 'Monday']['temp'][0])
fah_temp = celsius_to_fahrenheit(new_data[new_data.day == 'Monday'].temp[0])

print("Temperature in fahrenheit :",fah_temp)


# Create Dataframe from Scratch

data_dict = {
    "students" : [ 'sreehari', 'sreerag', 'nandana'],
    "score" : [78,89,100]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv") # create a csv files
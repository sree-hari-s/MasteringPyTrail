import pandas as pd 

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data.head())
print(data.columns)
print(data.shape)

# TODO : How many squirrels are there based on Primary Fur Color

print(data['Primary Fur Color'].unique())
#print(data.groupby('Primary Fur Color').count())

grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
Cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

print(grey_squirrel_count, black_squirrel_count,Cinnamon_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count,Cinnamon_squirrel_count,black_squirrel_count]
}

df = pd.DataFrame(data_dict)
print(df)
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
week = now.weekday()
"""
Monday = 0 
"""
print(week)
print(year)

date_of_birth = dt.datetime(year=1999,month=11,day=4,hour=3)
print(date_of_birth)
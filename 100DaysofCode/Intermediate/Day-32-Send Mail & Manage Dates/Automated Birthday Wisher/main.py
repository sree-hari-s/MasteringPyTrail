import pandas as pd
import smtplib
from random import randint
import datetime as dt

# 1. Update the birthdays.csv
data = pd.read_csv('birthdays.csv')
dict_data = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today = (month,day)

for data in dict_data:
    bday_month = data['month']
    bday_day = data['day']
    if today == (bday_month,bday_day):
        bday_person = data['name']
        bday_person_email = data['email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
number = randint(1,3)
with open(f'letter_templates/letter_{number}.txt', 'r') as f:
    letter = f.read()
    new_letter = letter.replace("[NAME]", bday_person)
    print(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.

mail = "sreeharis1999@gmail.com"
password = "vektoylzxigdxcxc"

with smtplib.SMTP("smtp.gmail.com",587) as  connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(
        from_addr=mail, 
        to_addrs=bday_person_email,
        msg=f"Subject:Happy Birthday!\n\n{new_letter}"
        )
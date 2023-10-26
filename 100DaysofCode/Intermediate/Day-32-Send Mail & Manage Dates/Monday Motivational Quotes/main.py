import smtplib
import datetime as dt
from random import choice

email = "sreeharis1999@gmail.com"
password = "vektoylzxigdxcxc"

now = dt.datetime.now()
current_day = now.weekday() # Get current day
print(current_day)
if current_day == 0: # send email if current day is monday
    with open("quotes.txt",'r') as file:
        quotes = file.readlines()
        todays_quote = choice(quotes)
        print(todays_quote)

    with smtplib.SMTP("smtp.gmail.com", port="587") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Motivational Quote\n\n{todays_quote}"
            )
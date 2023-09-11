"""
Instructions
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of 
printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]
"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]

# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

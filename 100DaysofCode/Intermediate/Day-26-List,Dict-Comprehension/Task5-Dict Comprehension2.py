"""
Instructions
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each 
temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f use this formula:

(temp_c * 9/5) + 32 = temp_f

Example Input

{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

Example Output

{'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

"""

weather_c = eval(input())
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {
    day:(temp* 9/5) + 32 for (day,temp) in weather_c.items()
}

print(weather_f)
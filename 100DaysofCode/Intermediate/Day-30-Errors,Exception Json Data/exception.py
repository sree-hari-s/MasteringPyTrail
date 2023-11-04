"""
# Custom Exception
You will use true_values and false_values to create a function named str_to_bool to convert strings to Boolean values. str_to_bool will accept one parameter named value.

Create the function str_to_bool. Convert value to lower case letters. If value matches an entry in true_values the function should return True. If value matches an entry in false_values it should return False. If it doesn't match any of the values, it should raise a ValueError, with a message of Invalid entry.
"""
def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')

true_values = ['yes', 'y']
false_values = ['no', 'n']

print(str_to_bool("Noo"))
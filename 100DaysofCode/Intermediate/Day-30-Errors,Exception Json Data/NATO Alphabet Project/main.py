
#TODO 1. Create a dictionary in this format:
"""
{"A": "Alfa", "B": "Bravo"}
"""
import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = { row.letter:row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    user_input =input("Enter the code word: ").upper()
    
    try:
        nato_code = [new_dict[code] for code in user_input ]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed please.")
    else:
        print(nato_code)
        break
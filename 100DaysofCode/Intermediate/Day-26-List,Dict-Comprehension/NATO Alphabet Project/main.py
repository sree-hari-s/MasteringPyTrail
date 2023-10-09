#TODO 1. Create a dictionary in this format:
"""
{"A": "Alfa", "B": "Bravo"}
"""
import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = { row.letter:row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input =input("Enter the code word: ").upper()

split_input = list(user_input)
nato_code = [new_dict[code] for code in split_input ]
print(nato_code)
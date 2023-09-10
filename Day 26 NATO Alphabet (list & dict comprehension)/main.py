#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

word = input("Enter a word: ")

nato_alphabet_dict = {row.letter:row.code for (index, row) in pd.read_csv("nato_phonetic_alphabet.csv").iterrows()}

nato_word = [nato_alphabet_dict[x.upper()] for x in word]

print(nato_word)
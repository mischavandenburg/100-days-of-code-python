import pandas

# read data from csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words
# from a word that the user inputs.
input = input("Enter a word: ").upper()
print([data_dict[i] for i in input])

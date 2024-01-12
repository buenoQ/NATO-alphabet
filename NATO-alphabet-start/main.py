import pandas
# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {}
for (index, row) in data.iterrows():
    phonetic_alphabet_dict[row.letter] = row.code

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
word_in_phonetic_alphabet = [phonetic_alphabet_dict[letter] for letter in user_input]
print(word_in_phonetic_alphabet)

import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabet=pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
alphabet={row.letter:row.code for _,row in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("enter a word: ").upper()
try:
    nato_list=[alphabet[letter] for letter in word ]
except KeyError:
    print("\njust letters please!\n")
else:
    print(nato_list)
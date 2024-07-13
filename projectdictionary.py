"""
Programer: generator.py
Author: Vishal Singh
Generates and displays senteces using grammar
and vocabulary. Words are choosen at random.
"""
import random
# Vocabulary : words in four different part of speech
articles        =   ("A",'An','The')
nouns           =   ('Boy','Girl','Bat','Ball')
verbs           =   ('Hit','Saw','Liked')
prepositions    =   ('With','By')
def sentence():
    return nounphrase()+" " + verbphrase()

def nounphrase():
    return random.choice(articles)+ " " + random.choice(nouns)

def verbphrase():
    return random.choice(verbs)+ " " + nounphrase() + " " +\
        prepositionalphrase()

def prepositionalphrase():
    return random.choice(prepositions) + " " + nounphrase()

def main():
    number=int(input("Enter the number of sentences : "))
    for count in range(number):
        print(sentence())

if __name__=="__main__":
    main()
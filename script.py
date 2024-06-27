# IMPORT PACKAGES
# May use 3rd party PSL Matplotlib and Natural Language Toolkit (NLTK)
import matplotlib.pyplot as plt
import nltk.data
from nltk.util import trigrams
from nltk import pos_tag, word_tokenize
import csv
import re

# Open text file to clean/preprocess
f = open('Texts/test.txt','r')
#Read text, lowercase, and clean using regex import
text = re.sub(r'[-\(\)\"#\/@;:<>\{\}\-=~|\.\?]', '',f.read().lower())
# TRIGRAM and POS list and occurrence tally.
# Create CSV list and POS Frequency Distribution array in terms of trigrams
# This is a slow process...expect delays
for pos in pos_tag(word_tokenize(text)) :
    # Add to trigram array OR uptick occurrnece
    # Add to Frequency Distribution array
    print(pos)


f.close()

# WRITE TO CSV
# Create and open Trigram.csv (2 cols Trigram && Occurrences)
# with open('Outputs/Trigram.csv', 'a+') as c:
#     writer = csv.writer(c)
#     # Required CSV headers
#     field = ["Trigram", "Occurrences"]
#     writer.writerow(field)
    
# # Close CSV file when done
# c.close()


# POS IMAGE - Speech.jpg frequency distribution
# IMPORT PACKAGES
# May use 3rd party PSL Matplotlib and Natural Language Toolkit (NLTK)
import matplotlib.pyplot as plt
import nltk.data
from nltk.util import trigrams
from nltk import pos_tag, word_tokenize
import csv
import re
from collections import Counter 


# Open text file to clean/preprocess
f = open('Texts/test.txt','r')
#Read text, lowercase, and clean using regex import
text = re.sub(r'[-\(\)\"#\/@;:<>\,\{\}\-=~|\.\?\!\*\[\]\']', '',f.read().lower())
# TRIGRAM and POS list and occurrence tally.
# Create CSV list and POS Frequency Distribution array in terms of trigrams
t_grams = []
pos_f = [] 
# This is a slow process...expect delays for tokenize process (6s+)
print('-----ENTERING POS TOKENIZE PROCESS------')
print('-----Approx Wait 10s ------')
pos_t = pos_tag(word_tokenize(text))
# Loop through POS to populate trigram array and POS freq. array
# Needed variables
found = False
m_sep = " "
print('-----ENTERING TRIGRAM UNIQUE/COUNT PHASE------')
print('-----Approx Wait 10min ------')
# res = Counter(map(''.join, zip(test_str, test_str[1:]))) 
freq_tri = {}
freq_pos_tri = {}
freq_pos_uni = {}

for i in range(len(pos_t)):
    # Create frequency map of trigrams and tri-POS
    if i < len(pos_t)-2:
        trigram = m_sep.join((pos_t[i][0],pos_t[i+1][0],pos_t[i+2][0]))
        pos_tri = m_sep.join((pos_t[i][1],pos_t[i+1][1],pos_t[i+2][1]))
        if trigram in freq_tri:
            freq_tri[trigram] += 1
        else:
            freq_tri[trigram] = 1

        if pos_tri in freq_pos_tri:
            freq_pos_tri[pos_tri] += 1
        else:
            freq_pos_tri[pos_tri] = 1    
    # Create Frequency map of POS Uni
    pos_uni = pos_t[i][1]
    if pos_uni in freq_pos_uni:
        freq_pos_uni[pos_uni] += 1
    else:
        freq_pos_uni[pos_uni] = 1

print("The Trigram Frequency is : " + str(freq_pos_tri)) 

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
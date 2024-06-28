# IMPORT PACKAGES
# May use 3rd party PSL Matplotlib and Natural Language Toolkit (NLTK)
import matplotlib.pyplot as plt
import numpy as np
import nltk.data
from nltk.util import trigrams
from nltk import pos_tag, word_tokenize
import csv
import re
from collections import Counter 

# Open text file to clean/preprocess
f = open('Texts/test.txt','r')
# Tockenize and store parts of speech
# This is a slow process...expect delays for tokenize process (6s+)
print('-----ENTERING POS TOKENIZE PROCESS------')
print('-----Approx Wait 8s ------')
#Read text, lowercase, and clean using regex import
text = re.sub(r'[-\(\)\"#\/@;:<>\,\{\}\-=~|\.\?\!\*\[\]\'$]', '',f.read().lower())
pos_t = pos_tag(word_tokenize(text))
# Derive from POS array
print('-----ENTERING TRIGRAM UNIQUE/COUNT PHASE------')
print('-----Approx Wait up to .2s ------')
# TRIGRAM and POS list and occurrence tally.
freq_tri = {}
freq_pos_tri = {}
freq_pos_uni = {}
# Loop through POS to populate trigram list and POS freq. list
# Needed variables
found = False
m_sep = " "
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
f.close()

# WRITE TO CSV now that trigrams are counted
print('-----Writing CSV FILE------')
print('-----Approx Wait up to .2s ------')
# Create and open Trigram.csv (2 cols Trigram && Occurrences)
with open('Outputs/Trigram.csv', 'a+') as c:
    # Reset cursor to overwrite csv if already exists
    c.seek(0)
    c.truncate()
    # continue with writing
    writer = csv.writer(c)
    writer.writerow(['Trigram', 'Occurrences'])
    for key, value in freq_tri.items():
        writer.writerow([key, value])
    # Close CSV file when done
    c.close()

# POS IMAGE - Speech.jpg frequency distribution horizontal chart
print('-----Creating POS Freq Dist Charts------')
print('-----Approx Wait up to 14s ------')

plt.figure(figsize=(10,100)) 
plt.rcParams['figure.figsize'] = [30,200]
fig,(axt,axu) = plt.subplots(2)

# POS-Unigram Frequency data plots
# params
pos_l = list(freq_pos_tri.keys())
y_pos = np.arange(len(pos_l))
freq = list(freq_pos_tri.values())
# graph settings
axt.barh(y_pos, freq, align='center')
axt.set_yticks(y_pos, labels=pos_l)
axt.invert_yaxis()  # labels read top-to-bottom
axt.set_xlabel('POS Uni Frequency')
axt.set_ylabel('POS Trigram')
axt.set_title('Distribution')

# POS-Trigram Frequency data plots
# params
pos_l_u = list(freq_pos_uni.keys())
y_pos_u = np.arange(len(pos_l_u))
freq_u = list(freq_pos_uni.values())
# graph settings
axu.barh(y_pos_u, freq_u, align='center')
axu.set_yticks(y_pos_u, labels=pos_l_u)
axu.invert_yaxis()  # labels read top-to-bottom
axu.set_ylabel('POS Unigram')
axu.set_xlabel('POS Tri Frequency')

plt.savefig('Outputs/Speech.png', dpi=150, bbox_inches='tight')

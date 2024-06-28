**Python Challenge Problem**
# Trigram/POS 

The following scipt will read a text file and parse it for analysis with  the Natural Language Processing python library (NLTK) among other standard python libraries.

## Setup and Environments
This script/folder was tested in a conda environment with python 3.9 and all associated imports installed. The script can be run with: 'python script.py'.
```console
foo@bar:~$ python script.py
```
## Data Cleaning
The text file is stripped, using regex, of special symbols and characters and lowercased. This is to ensure all unique trigrams are identified.

## Outputs
If the script runs successfully, you will see the following terminal outputs during processing:

```console
-----ENTERING POS TOKENIZE PROCESS------
-----Approx Wait 8s ------
-----ENTERING TRIGRAM UNIQUE/COUNT PHASE------
-----Approx Wait up to .2s ------
-----Writing CSV FILE------
-----Approx Wait up to .2s ------
-----Creating POS Freq Dist Charts------
-----Approx Wait up to 14s ------
```
###### CSV - Trigram.csv
A CSV file with two columns (trigram, occurrences) and an image with trigram Parts of Speech (POS) and unigram POS are produces.

###### Images - Speech.png
Both unigram POS and trigram POS occurrences were mapped for comparison. The image is produced at 150dpi to allow close inspection (zoom to 300%) as there is a lengthy list of trigram POS combinations.
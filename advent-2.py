
import os
import sys
import string


WORDLIST_FILENAME = "c:/Our Files/Darren/dev/advent/measure.txt"

def loadWords():
  
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string

    lines = inFile.readlines()
    wordlist = [];
    for line in lines:
        wordlist.append(int(line.strip()))
    # wordlist: list of strings
    
    print("", len(wordlist), "words loaded.")
    return wordlist



wordlist = loadWords()

increase = 0
prev = 0
max = len(wordlist)
i = 0
for i, word in enumerate(wordlist):
    curr = int(i) + int(3)
    sub = wordlist[i:curr]
    #print(sub)
    total = sum(sub)
    if prev and len(sub) == 3:
        if prev < total:
            increase += 1
    prev = total
    
print(increase)


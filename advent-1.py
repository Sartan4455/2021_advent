
WORDLIST_FILENAME = "c:/Our Files/Darren/dev/advent/measure.txt"

def loadWords():
 
    inFile = open(WORDLIST_FILENAME, 'r')

    lines = inFile.readlines()
    wordlist = []
    for line in lines:
        wordlist.append(int(line.strip()))
    # wordlist: list of strings
    
    print("", len(wordlist), "words loaded.")
    return wordlist



wordlist = loadWords()


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

increase = 0
prev = 0
i = 0
for word in wordlist:
    if (prev): 
        if int(prev) < int(word):
            #print(str(prev) + ' is less than ' + str(word))
            increase += 1
        #else:
            #print(str(prev) + ' is greater than ' + str(word))
    prev = word
print(increase)


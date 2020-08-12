from random import randint

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
randomLetters = []

for letter in letters:
    randomLetters.append(letter)

for x in range(26):
    randomNumberOne = randint(0, 25)
    randomNumberTwo = randint(0, 25)
    c = randomLetters[randomNumberOne]
    randomLetters[randomNumberOne] = randomLetters[randomNumberTwo]
    randomLetters[randomNumberTwo] = c

dictionaryFile = open('dictionaryFile.txt', 'w')

dictionaryFile.write(str(letters) + '\n')
for x in range(26):
    dictionaryFile.write(randomLetters[x])

dictionaryFile.close()

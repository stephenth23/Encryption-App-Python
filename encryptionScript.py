# Ecryption File

dictionaryFile = open('dictionaryFile.txt', 'r')

orderLetters = dictionaryFile.readline()
randomLetters = dictionaryFile.readline()


while 2 > 0:
    message = input('Your message:\n')
    encryptedMessage = ''
    decryptedMessage = ''

    for letter in message:
        if letter.upper() in orderLetters:
            encryptedMessage += randomLetters[orderLetters.index(letter.upper())].lower()
        elif letter == ' ':
            encryptedMessage += ' '
        else:
            encryptedMessage += letter


    for letter in message:
        if letter.upper() in randomLetters:
            decryptedMessage += orderLetters[randomLetters.index(letter.upper())].lower()
        elif letter == ' ':
            decryptedMessage += ' '
        else:
            decryptedMessage += letter

    print('\nencrypted: ' + str(encryptedMessage))
    print('decrypted: ' + str(decryptedMessage) + '\n\n')



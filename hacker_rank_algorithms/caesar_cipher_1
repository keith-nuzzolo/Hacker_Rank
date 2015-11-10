'''
Julius Caesar protected his confidential information
from his enemies by encrypting it.
Caesar rotated every letter in the string by a fixed number K.
This made the string unreadable by the enemy.
You are given a string S and the number K.
Encrypt the string and print the encrypted string.
'''
def cipher(length, message, shift):
    ''' Takes a message and returns the message with each letter shifted by the
    inputed shift value'''
    new_message = ''
    value = 0
    for i in range(0,length):
        if not message[i].isalpha():
            new_message += message[i]
        else:
            value = ord(message[i])

            if (value <= 90 and value + shift%26 - 90 > 0):
                value += -26 + shift%26
            elif(value >= 90 and value + shift%26 - 122 > 0):
                value += -26 + shift%26
            else:
                value += shift%26
            new_message += chr(value)
    return(new_message)
print(cipher(int(input()),input(), int(input())))

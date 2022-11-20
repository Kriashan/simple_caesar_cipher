import string
import sys
import re

# Encrypt messages
def encrypt(encrypting):
    # Available characters
    letters = list(string.ascii_letters + string.digits + string.punctuation + ' ')
    
    # Input
    encode = input("Enter your string to encrypt: ")
    
    # Sanitize
    key = ''.join(re.findall('[0-9]', input("How much do you want to shift this by must be a whole number: "))) + '0'
    key = int(key) // 10 # Radix is 10 so this is 0/10 which does nothing and avoids blank error
    if not encrypting:
        key = -key
    encode = ''.join(re.findall('[{}]'.format(''.join(letters)), encode))

    # Encrypt
    new_string = []
    for letter in encode:
        new_string.append(letters[(letters.index(letter) + key) % len(letters)])
    
    # stdout output
    stdout('Output: {}'.format(''.join(new_string)))

# Asks the user if the want to encrypt a message? decrypt a message? or exit the program?
def cipher():
    while True:
        ask = input("Do you want to encrypt a message? or decrypt a message? or exit? ").lower() # lower to avoid capitalization issues
        if ask == 'encrypt':
            encrypt(True)
            break
        elif ask == 'decrypt':
            encrypt(False)
            break
        elif ask == 'exit':
            exit(0)
        else:
            stdout('Please enter encrypt, or decrypt, or exit')

def stdout(*text):
    for item in text:
        sys.stdout.write(str(item) + ' ')
    sys.stdout.write('\n')

if __name__ == '__main__':
    cipher()

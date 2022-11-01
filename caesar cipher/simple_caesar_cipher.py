import string
import sys
import re

def cipher():
    letters = list(string.ascii_letters + string.digits + string.punctuation + '')
    print(letters)

    encode = input("Enter your string to encode: ")
    key = ''.join(re.findall('[0-9]', input("How much do you want to shift this by can be a positive or negative integer: ")))
    key = int(key)
    new_string = []

    for letter in encode:
        new_string.append(letters[(letters.index(letter) + key) % len(letters)])
    stdout('Output: ' + ''.join(new_string))

def stdout(text):
    sys.stdout.write(str(text) + '\n')

if __name__ == '__main__':
    cipher()

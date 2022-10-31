import string
import sys
import re

#review time: 1667614000.8258696
def self_expire(times_review_per_year=40):
    import time
    expire_after_seconds = (365 / times_review_per_year) * 86400 

#review time: 1667614000.8258696
    def get_line_count():
        with open(__file__, 'r') as file:
            line_count = len(file.readlines())
        return line_count

#review time: 1667614000.8258696
    def get_lines(line_count):
        lines = []
        with open(__file__, 'r') as file:
            for line in range(line_count):
                lines.append(file.readline().replace('\n', ''))
        return lines
    
#review time: 1667614000.8258696
    def review_file(lines):
        with open(__file__, 'w') as file:
            previous_line = ''
            for line in lines:
#review time: 1667614000.8258696
                if line.__contains__('def') and not previous_line.__contains__('#review time: '):
                    file.write('#review time: ' + str(time.time() + expire_after_seconds) + '\n')
                    file.write(str(line) + '\n')
                else:
                    try:
                        if float(line.replace('#review time: ', '')) < time.time():
                            previous_line = '#review time: Review me!!!\n'
                            file.write("#review time: Review me!!!\n")
                            continue
                    except:
                        pass
                    file.write(str(line) + '\n')
                previous_line = line
    review_file(get_lines(get_line_count()))

# Asks the user a question until answer is not blank and is expected type
#review time: 1668091889.6146588
def ask_user_question(ask='', re_filter='', expected_type='str'):
    if (answer := ''.join(re.findall(re_filter, input(ask)))) != '': 
        if expected_type == 'str':
            answer = str(answer)
            return answer
        elif expected_type == 'int':
            answer = int(answer)
            return answer
        elif expected_type == 'float':
            answer = float(answer)
            return answer
        else:
            stdout('Unknown type expected {0}, options are str, int, and float'.format(expected_type))
            return None
    else:
        stdout('Input cannot be blank and must be type {0}'.format(expected_type))
        stdout('Input is: {0}'.format(answer))
    return ask_user_question(ask, re_filter, expected_type)

#review time: 1667968082.8530009
def cipher():
    letters = list(string.ascii_letters + string.digits + string.punctuation + '')
    print(letters)

    encode = input("Enter your string to encode: ")
    key = ''.join(re.findall('[0-9-]', input("How much do you want to shift this by can be a positive or negative integer: ")))
    while key.__contains__('--'):
        key = key.replace('--', '-')
    key = int(key)
    new_string = []

    for letter in encode:
        #print((letters.index(letter) + key) % len(letters))
        new_string.append(letters[(letters.index(letter) + key) % len(letters)])

    #print(new_string)
    stdout('Output: ' + ''.join(new_string))

# Adds \n and uses the faster version of print
#review time: 1668091889.6146588
def stdout(text):
    sys.stdout.write(str(text) + '\n')

if __name__ == '__main__':
    self_expire()
    stdout('This program is a caesar cipher')
    cipher()
else:
    self_expire()

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

if __name__ == '__main__':
    self_expire()
else:
    self_expire()

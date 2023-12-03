import re
REGEX_CHARS = "one|two|three|four|five|six|seven|eight|nine"
REGEX = "[0-9]|" + REGEX_CHARS
REGEX_REV = "[0-9]|" + REGEX_CHARS[::-1]
STR_TO_INT = {'zero':'0', 'one':'1', 'two':'2', 
              'three':'3', 'four':'4', 'five':'5',
              'six':'6', 'seven':'7', 'eight':'8', 
              'nine':'9'}

val = 0

def to_digit(s):
    '''
    Convert read in value to a digit
    '''
    print(s)
    try:
        rv = str(int(s))
    except ValueError:
        rv = STR_TO_INT.get(s)
    return rv

with open('inputs/day1.txt', 'r') as data:
    lines = data.readlines()
    for line in lines:
        first = re.findall(REGEX, line)[0]
        last = re.findall(REGEX_REV, line[::-1])[0][::-1]
        print(first, last)
        val += int(str(to_digit(first)) + str(to_digit(last)))

print(val)
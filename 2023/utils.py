def to_digit(s):
    '''
    Covert a written out digit s to it a string representation
    of the digit.

    example: "one" -> "1"

    Remarks: this was written for day1, so it is case sensitive
    (lowercase only).
    '''
    STR_TO_INT = {'zero':'0', 'one':'1', 'two':'2', 
              'three':'3', 'four':'4', 'five':'5',
              'six':'6', 'seven':'7', 'eight':'8', 
              'nine':'9'}
    try:
        return str(int(s))
    except ValueError:
        return STR_TO_INT.get(s)
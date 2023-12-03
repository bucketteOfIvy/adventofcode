import re
SYMBOLS = ["*","#", "+", "$", "/", "=", "@", "%", "&"]

def indices_in_line(line):
    '''
    Returns indices in the line where a symbol is detected.
    '''
    inds = []
    for ind, val in enumerate(line):
        if val in SYMBOLS:
           print('SYMBOL', val, 'FOUND AT', ind)
           inds = inds + [ind]
    return inds

def nums_around_gear(lines, loc):
    '''
    nums_around, but only returns a nonempty list if exactly 2 nums are found.
    '''
    nums = []
    if loc == []:
        return []

    row_low, row_high = max(0, loc[0] - 1), min(len(lines), loc[0] + 2)
    col_low, col_high = max(0, loc[1] - 1), min(len(lines), loc[1] + 2)

    blot_triples = []
    for row_num in range(row_low, row_high):
        for col_num in range(col_low, col_high):
            if re.match("[0-9]", lines[row_num][col_num]):
                new_num, tail, head = find_full(lines[row_num], col_num)
                print('found num!', 'is', new_num)
                if new_num not in nums:
                    nums.append(new_num)
                    blot_triples.append((row_num, tail, head))

    if len(nums) != 2:
        return []

    for loc in blot_triples:
        print('before blot:', lines[loc[0]][loc[1]:loc[2]+1])
        blot_out(lines, loc[0], loc[1], loc[2]+1)
        print('after blot:', lines[loc[0]][loc[1]:loc[2]+1])

    return [int(nums[0]) * int(nums[1])]

def nums_around(lines, loc):
    '''
    Returns a list of all numbers located around the the location given in
    loc.
    '''
    nums = []
    if loc == []:
        return []

    row_low, row_high = max(0, loc[0] - 1), min(len(lines), loc[0] + 2)
    col_low, col_high = max(0, loc[1] - 1), min(len(lines), loc[1] + 2)

    blot_triples = []
    for row_num in range(row_low, row_high):
        for col_num in range(col_low, col_high):
            if re.match("[0-9]", lines[row_num][col_num]):
                new_num, tail, head = find_full(lines[row_num], col_num)
                print('found num!', 'is', new_num)
                if new_num not in nums:
                    nums.append(new_num)
                    blot_triples.append((row_num, tail, head))

    for loc in blot_triples:
        print('before blot:', lines[loc[0]][loc[1]:loc[2]+1])
        blot_out(lines, loc[0], loc[1], loc[2]+1)
        print('after blot:', lines[loc[0]][loc[1]:loc[2]+1])

    return nums

def blot_out(lines, row, tail, head):
    '''
    Replace all values in row bewteen tail and head (inc) with "."
    Works in place
    '''
    for i in range(tail, head + 1):
        lines[row][i] = "."

def find_full(line, ind):
    '''
    Given a list of characters and an index where there's a numeric,
    constructs the entire numeric and returns it as a string.

    Additionally, returns the tail and head of the string.
    '''
    full = line[ind]
    tail, head = ind, ind
    # If legal, check the left.
    if ind > 0:
        ind_to_check = ind - 1
        while ind_to_check >= 0:
            if not re.match('[0-9]', line[ind_to_check]):
                break
            full = line[ind_to_check] + full
            ind_to_check -= 1
        tail = ind_to_check + 1

    if ind + 1 < len(line):
        ind_to_check = ind + 1
        while ind_to_check < len(line):
            if not re.match('[0-9]', line[ind_to_check]):
                break
            full = full + line[ind_to_check]
            ind_to_check += 1
        head = ind_to_check - 1
    
    return full, tail, head
    

def find_gear_ratios(lines):
    '''
    Find nums, but it finds gear ratios and returns a list of them.
    '''
    lines2 = [[letter for letter in line] for line in lines]

    # Find the locations of all symbols.
    inds_to_check = []
    for row_num, line in enumerate(lines2):
        cols = indices_in_line(line)
        inds_to_check.extend([(row_num, col) for col in cols])

    all_nums = []
    for loc in inds_to_check:
        if loc != []:
            print('Checking around the symbol', lines2[loc[0]][loc[1]], 'which is at', loc[0], loc[1])
            # Arguably this is cursed!
            all_nums.extend(nums_around_gear(lines2, loc))

    return all_nums

def find_nums(lines):
    '''
    Given all lines, finds the relevant numbers
    and returns a list of them.
    '''

    # Turn this into a list of lists.
    lines2 = [[letter for letter in line] for line in lines]

    # Find the locations of all symbols.
    inds_to_check = []
    for row_num, line in enumerate(lines2):
        cols = indices_in_line(line)
        inds_to_check.extend([(row_num, col) for col in cols])


    # Check around each symbol.
    all_nums = []
    for loc in inds_to_check:
        if loc != []:
            print('Checking around the symbol', lines2[loc[0]][loc[1]], 'which is at', loc[0], loc[1])
            # Arguably this is cursed!
            all_nums.extend(nums_around_gear(lines2, loc))

    return all_nums

if __name__ == "__main__":
    with open('inputs/day3.txt') as data:
        lines = data.readlines()
    for line in lines:
        for letter in line:
            if not letter in SYMBOLS and not re.match('[0-9]', letter) and letter != "." and letter != "\n":
                SYMBOLS.append(letter)
    print('symbols list:', SYMBOLS)
    nums = find_nums(lines)
    nums = [int(num) for num in nums]
    print(sum(nums))

    print("=========== PART 2 ===============")
    nums = find_gear_ratios(lines)
    print(sum([int(num) for num in nums]))

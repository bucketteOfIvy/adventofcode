import re
CUBE_CNTS = {'blue':14, 'red':12, 'green':13}
REGEX_CUBES = 'red|blue|green'
REGEX_NUMS = '\d+'

def is_possible(mtch):
    for col, cnt in mtch:
        if int(cnt) > CUBE_CNTS[col]:
            return False
    return True

id_cnt = 0
with open('inputs/day2.txt') as data:
    data_lines = data.readlines()
    for line in data_lines:
        gm, vals = re.split(":", line)
        cnts = re.findall(REGEX_NUMS, vals)
        cols = re.findall(REGEX_CUBES, vals)
        
        mtch = [(col, cnt) for col, cnt in zip(cols, cnts)]

        if is_possible(mtch):
            print("line:\n", line, "is possible")
            id_val = re.findall("\d+", gm)[0]
            id_cnt += int(id_val)

print(id_cnt)

with open('inputs/day2.txt') as data:
    data_lines = data.readlines()
    gm_mtchs = []
    for line in data_lines:
        gm, vals = re.split(":", line)
        cnts = re.findall(REGEX_NUMS, vals)
        cols = re.findall(REGEX_CUBES, vals)
        
        mtch = {'red':0, 'green':0, 'blue':0}
        
        for cnt, col in zip(cnts, cols):
            if int(cnt) > mtch[col]:
                mtch[col] = int(cnt)
        gm_mtchs.append(mtch)

val = 0
for mtch in gm_mtchs:
    val += mtch['red'] * mtch['blue'] * mtch['green']

print(val)
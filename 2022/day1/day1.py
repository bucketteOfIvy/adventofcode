# SOLVE DAY 1
def get_next_cal(lines):
    nl, a = lines.pop(0), 0
    while nl != '\n' and lines != []:
        a += int(nl)
        nl = lines.pop(0)
    return a

if __name__ == "__main__":

    with open('input.txt', 'r') as input:
        lines = input.readlines()
    
    bst_thr = [get_next_cal(lines), get_next_cal(lines), get_next_cal(lines)]

    while lines != []:
        comp = get_next_cal(lines)
        
        if min(bst_thr) < comp:
            bst_thr.remove(min(bst_thr))
            bst_thr.append(comp)
            print(f'upset! now {bst_thr}')

    print(f'bst: {bst_thr}')
    print(f'sum: {sum(bst_thr)}')
                


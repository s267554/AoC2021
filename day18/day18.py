import re

def sn_add(sn1, sn2):
    return f"[{sn1},{sn2}]"


def find_nearest_reg_num(sn, index_start, index_end, direction):

    if direction == 'forward':
        index_end_nearest = sn[index_end+2:].find(']') + index_end # +2 for ],
        index_start_nearest = index_end + 1 # +1 for ','
        right, left = eval(sn[index_start_nearest:index_end_nearest])

    return

def sn_explode(sn, index):

    index_start_reg_num = index
    index_end_reg_num = index+sn[index:].find(']')+1

    left, right = eval(sn[index_start_reg_num : index_end_reg_num])

    find_nearest_reg_num(sn, index_start_reg_num, index_end_reg_num, direction='forward')

    return 
    

def sn_reduce(sn):
    expl, spl = find4(sn), find10(sn)
    if expl == -1 and spl == -1:
        return sn, False

    if spl == -1 or expl < spl:
        sn = sn_explode(sn, expl-1)
    elif expl == -1 or spl < expl:
        sn = sn_split(sn, spl)
    else:
        raise ValueError('WTF')

    return sn, True

def find4(sn):
    par = 0
    for index, ch in enumerate(sn):
        if par > 4:
            return index
        if ch == '[':
            par += 1
        if ch == ']':
            par -= 1
    return -1

def find10(sn):
    prev = sn[0]
    for index, ch in enumerate(sn):
        if ch.isdigit() and prev.isdigit():
            return index-1
        prev = ch
    return -1    


def main():

    with open('./day18/test.txt') as input_file:
        #snails = [eval(line) for line in input_file.readlines()]
        lines = [line.strip() for line in input_file.readlines()]

    result = lines[0]

    for i, line in enumerate(lines[1:]):
        print(f'i: {i}')
        
        line = sn_add(result, line)
        

        while True:
            line_reduced, is_reduced = sn_reduce(line)
            print(f'line_reduced: {line_reduced}')
            if is_reduced:
                break

    return

if __name__ == '__main__':

    main()
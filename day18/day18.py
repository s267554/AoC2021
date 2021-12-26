import re

def sn_add(sn1, sn2):
    return f"[{sn1},{sn2}]"


def find_nearest_reg_num(sn, index_start, index_end, numToAdd, direction):

    skip_chars = '[],'

    index_with_int = -1
    new_int = -1

    if direction == 'forward':
        for i, c in enumerate(sn[index_end:]):
            if c not in skip_chars:
                index_with_int = index_end + i
                new_int = int(c) + numToAdd
                break
    
        return index_with_int, new_int


    if direction == 'backward':
        for i, c in enumerate(sn[:index_start][::-1]):
            if c not in skip_chars:
                index_with_int = len(sn[:index_start]) - i
                new_int = int(c) + numToAdd
                break
    
        return index_with_int, new_int

    raise ValueError('not good')
    
def sn_explode(sn, index):

    index_start_reg_num = index
    index_end_reg_num = index+sn[index:].find(']')+1

    left, right = eval(sn[index_start_reg_num : index_end_reg_num])

    i_new_int_l, new_int_l = find_nearest_reg_num(sn, index_start_reg_num, index_end_reg_num, numToAdd=left, direction='backward')

    if i_new_int_l == -1:
        left_sn = sn[:index_start_reg_num]
    else:
        left_sn = sn[:i_new_int_l-1] + str(new_int_l)

    i_new_int_r, new_int_r = find_nearest_reg_num(sn, index_start_reg_num, index_end_reg_num, numToAdd=right, direction='forward')

    if i_new_int_r == -1:
        right_sn = sn[index_end_reg_num:]
    else:
        right_sn = str(new_int_r) + sn[i_new_int_r+1:]
    
    
    new_sn = left_sn + ',0' + sn[index_end_reg_num:i_new_int_r] + str(new_int_r) + sn[i_new_int_r+1:]

    return new_sn
    

def sn_reduce(sn):
    expl, spl = find4(sn), find10(sn)
    if expl == -1 and spl == -1:
        return sn, False

    if spl == -1 or expl < spl:
        sn = sn_explode(sn, expl-1)
        return sn, True
    elif expl == -1 or spl < expl:
        sn = sn_split(sn, spl)
        return sn, True
    else:
        raise ValueError('WTF')

    

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

def magn(stuff):
    if isinstance(stuff, list):
        return 3*magn(stuff[0]) + 2*magn(stuff[1])
    return stuff

def main():

    with open('./day18/test.txt') as input_file:
        #snails = [eval(line) for line in input_file.readlines()]
        lines = [line.strip() for line in input_file.readlines()]

    result = lines[0]

    for i, line in enumerate(lines[1:]):
        print(f'i: {i}')
        
        line = sn_add(result, line)
        

        while True:
            line_reduced, keep_reducing = sn_reduce(line)
            print(f'line_reduced: {line_reduced}')
            line = line_reduced
            if not keep_reducing:
                break

    #eval string as list then calc magnitude
    toCalc = eval(result)
    return magn(toCalc)

if __name__ == '__main__':

    res = main()
    print(res)
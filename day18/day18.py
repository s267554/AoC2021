import re
from math import ceil, floor

def sn_add(sn1, sn2):
    return f"[{sn1},{sn2}]"


def find_nearest_reg_num(sn, index_start, index_end, numToAdd, direction):

    skip_chars = '[],'

    int_start, int_end = -1, -1
    new_int = -1

    num = ''

    if direction == 'forward':
        for i, c in enumerate(sn[index_end:]):
            if c not in skip_chars:
                if num == '':
                    int_start = index_end + i
                num += c
            elif c in skip_chars and num != '':
                int_end = index_end + i
                new_int = int(num) + numToAdd
                break
    
        return [int_start, int_end], new_int


    if direction == 'backward':
        for i, c in enumerate(sn[:index_start][::-1]):
            if c not in skip_chars:
                if num == '':
                    int_end = len(sn[:index_start]) - i
                num += c
            elif c in skip_chars and num != '':
                int_start = len(sn[:index_start]) - i
                new_int = int(num[::-1]) + numToAdd
                break
    
        return [int_start, int_end], new_int

    raise ValueError('not good')
    
def sn_explode(sn, index):

    index_start_reg_num = index
    index_end_reg_num = index+sn[index:].find(']')+1

    left, right = eval(sn[index_start_reg_num : index_end_reg_num])

    i_new_int_l, new_int_l = find_nearest_reg_num(sn, index_start_reg_num, index_end_reg_num, numToAdd=left, direction='backward')
    i_new_int_r, new_int_r = find_nearest_reg_num(sn, index_start_reg_num, index_end_reg_num, numToAdd=right, direction='forward')

    sn_new = '0'

    if new_int_l != -1:
        sn_new = sn[:i_new_int_l[0]] + str(new_int_l) + sn[i_new_int_l[1]:index_start_reg_num] + sn_new
    else:
        sn_new = sn[:index_start_reg_num] + sn_new
    
    if new_int_r != -1:
        sn_new += sn[index_end_reg_num:i_new_int_r[0]] + str(new_int_r) + sn[i_new_int_r[1]:]
    else:
        sn_new += sn[index_end_reg_num:]
    return sn_new

def sn_split(sn, index):
    num = int(sn[index:index+2])/2
    left, right = floor(num), ceil(num)

    sn_new = sn[:index] + f"[{left},{right}]" + sn[index+2:]

    return sn_new




def sn_reduce(sn):
    while True:
        expl, spl = find4(sn), find10(sn)
        if expl == -1 and spl == -1:
            return sn
        if expl != -1:
            sn = sn_explode(sn, expl-1)
        elif spl != -1:
            sn = sn_split(sn, spl)
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

    with open('test.txt') as input_file:
        lines = [line.strip() for line in input_file.readlines()]

    result = lines[0]

    for i, line in enumerate(lines[1:]):
        
        line = sn_add(result, line)
        result = sn_reduce(line)

    #eval string as list then calc magnitude
    print(result)
    toCalc = eval(result)
    return magn(toCalc)

if __name__ == '__main__':

    res = main()
    print(res)
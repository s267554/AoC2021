import re

def sn_add(sn1, sn2):
    return f"[{sn1},{sn2}]"

def sn_explode(sn, index):
    left, right = eval(sn[index : index+sn[index:].find(']')+1])
    

def sn_reduce(sn):
    expl, spl = find4(sn), find10(sn)
    if expl == -1 and spl == -1:
        return sn, False
    if spl == -1 or expl < spl:
        sn = sn_explode(sn, expl-1)
    elif expl == -1 or spl < expl:
        sn = sn_split(sn, spl)
    else:
        print("wtf")

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

with open('test.txt') as input_file:
    #snails = [eval(line) for line in input_file.readlines()]
    lines = [line.strip() for line in input_file.readlines()]


result = lines[0]
for line in lines[1:]:
    line = sn_add(result, line)
    sn_reduce(line)
    break
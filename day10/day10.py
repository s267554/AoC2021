#!/bin/python3

POINTS = {')':3, ']':57, '}':1197, '>':25137}
NEEDED = {'(':')', '[':']', '{':'}', '<':'>'}
ADDINGS = {'(':1, '[':2, '{':3, '<':4}

with open('input.txt') as input_file:
    puzzle = input_file.read().splitlines()

sol1 = 0
scores = []

for line in puzzle:
    stack = []
    corrupted = False

    for ch in line:
        if ch in '([{<':
            stack.append(ch)
        else:
            if NEEDED[stack.pop()] != ch:
                sol1 += POINTS[ch]
                corrupted = True
                break

    if not corrupted:
        score = 0
        for open_par in stack[::-1]:
            score = score * 5 + ADDINGS[open_par]
        scores.append(score)

scores.sort()
sol2 = scores[ len(scores) // 2 ]

print(f"sol1 is {sol1} and sol2 is {sol2}")
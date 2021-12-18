import math

with open('input.txt') as input_file:
    puzzle = input_file.read().split(': ')[1]
    v = puzzle.split(', ')
    min_x, max_x = map(int, v[0][2:].split('..'))
    min_y, max_y = map(int, v[1][2:].split('..'))

min_vx0 = 0
max_vx0 = max_x

max_vy0 = -min_y
min_vy0 = min_y

sol = set()
for vx0 in range(min_vx0, max_vx0+1):
    for vy0 in range(min_vy0, max_vy0+1):
        x, y = 0, 0
        vx, vy = vx0, vy0

        ok = False
        while x <= max_x and y >= min_y:
            if min_x <= x <= max_x and min_y <= y <= max_y:
                ok = True
                break
            x += vx
            y += vy
            if vx > 0:
                vx -=1
            vy -=1
        if ok:
            sol.add((vx0, vy0))

print(f"sol2 is {len(sol)}")
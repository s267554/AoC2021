with open('input.txt') as input_file:
    m = [list(map(int, line.strip())) for line in input_file]

MAX_ROW, MAX_COL = len(m), len(m[0])

def check(r, c):
    m[r][c] += 1
    if m[r][c] > 9 and (r, c) not in flashed:
        flashed.add((r, c))
        if r+1 < MAX_ROW:
            if c+1 < MAX_COL:
                check(r+1, c+1)
            if c-1 >= 0:
                check(r+1, c-1)
            check(r+1, c)             
        if r-1 >= 0:
            if c+1 < MAX_COL:
                check(r-1, c+1)
            if c-1 >= 0:
               check(r-1, c-1)
            check(r-1, c)                    
        if c+1 < MAX_COL:
            check(r, c+1)
        if c-1 >= 0:
            check(r, c-1)

flashed = set()
flashes, synchro = 0, 0
for step in range(1000):
    flashed = set()

    for r, row in enumerate(m):
        for c, el in enumerate(row):
            check(r, c)

    for r, c in flashed:
        m[r][c] = 0
        if step < 100:
            flashes += 1
            
    if not synchro and len(flashed) == MAX_COL * MAX_ROW:
        synchro = step + 1
        if step > 100:
            break

print(f"sol1 is {flashes} and sol2 is {synchro}")
with open('input.txt') as input_file:
    m = [list(map(int, line.strip())) for line in input_file]

MAX_ROW, MAX_COL = len(m), len(m[0])

def check(r, c):
    if 0 <= r < MAX_ROW and 0 <= c < MAX_COL:
        m[r][c] += 1
        
        if m[r][c] > 9 and (r, c) not in flashed:
            flashed.add((r, c))
            for row in range(r-1, r+2):
                for col in range(c-1, c+2):
                    if row != r or col != c:
                        check(row, col)

flashed = set()
flashes, synchro = 0, 0

for step in range(1000):
    flashed.clear()

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
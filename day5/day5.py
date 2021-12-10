puzzle = open("input.txt", "r")

### numpy sucks

m1 = [[0] * 1000 for _ in range(1000)]
m2 = [[0] * 1000 for _ in range(1000)]

for line in puzzle.readlines():
    a, b = line.split(' -> ')
    ax, ay = a.split(',')
    bx, by = b.split(',')
    
    ax, ay, bx, by = int(ax), int(ay), int(bx), int(by)
    
    if ax == bx:
        if ay > by:
            ay, by = by, ay
        for j in range(ay, by+1):
            m1[ax][j] += 1
            m2[ax][j] += 1
    elif ay == by:
        if ax > bx:
            ax, bx = bx, ax
        for i in range(ax,bx+1):
            m1[i][by] += 1
            m2[i][by] += 1
    else:
        dirx, diry = 1, 1
        if ay > by:
            diry = -1
        if ax > bx:
            dirx = -1
        for _ in range(abs(ax-bx)+1):
            m2[ax][ay] += 1
            ax += dirx
            ay += diry

sol1 = 0
for i in range(1000):
    for j in range(1000):
        if m1[i][j] > 1:
            sol1 += 1

sol2 = 0
for i in range(1000):
    for j in range(1000):
        if m2[i][j] > 1:
            sol2 += 1

print(f"sol1 is {sol1} and sol2 is {sol2}")

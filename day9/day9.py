m = []
with open('input.txt') as input_file:
    m = [list(map(int, line.strip())) for line in input_file]

lows = []
sol1 = 0

for i in range(len(m)):
    for j in range(len(m[0])):
        h = m[i][j]
        if i+1 < len(m) and m[i+1][j] <= h:
            continue
        if i-1 >= 0 and m[i-1][j] <= h:
            continue
        if j+1 < len(m[0]) and m[i][j+1] <= h:
            continue
        if j-1 >= 0 and m[i][j-1] <= h:
            continue
        sol1 += 1 + h
        lows.append((i,j))

sizes = []
for il, jl in lows:
    size = 0
    stack = [(il, jl)]
    visited = set()

    while len(stack) > 0:
        (i, j) = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        h = m[i][j]
        if h == 9:
            continue
        size += 1
        if i+1 < len(m) and m[i+1][j] >= h:
            stack.append((i+1, j))
        if i-1 >= 0 and m[i-1][j] >= h:
            stack.append((i-1, j))
        if j+1 < len(m[0]) and m[i][j+1] >= h:
            stack.append((i, j+1))
        if j-1 >= 0 and m[i][j-1] >= h:
            stack.append((i, j-1)) 
            
    sizes.append(size)
sizes.sort()

sol2 = 1
for mul in sizes[-3:]:
    sol2 *= mul

print(f"sol1 is {sol1} and sol2 is {sol2}")

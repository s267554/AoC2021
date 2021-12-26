matrix = [list(line.rstrip()) for line in open('input.txt').readlines()]

print(matrix)
n, m = len(matrix), len(matrix[0])

step = 0
changed = True
while changed:
    changed = False
    toMove = []
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el == '>':
                if matrix[i][(j+1) % m] == '.':
                    toMove.append((i, j))
                    changed = True
    for i, j in toMove:
        matrix[i][(j+1) % m] = '>'
        matrix[i][j] = '.'

    toMove = []
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el == 'v':
                if matrix[(i+1) % n][j] == '.':
                    toMove.append((i, j))
                    changed = True
    for i, j in toMove:
        matrix[(i+1) % n][j] = 'v'
        matrix[i][j] = '.'
    step += 1
print(step)
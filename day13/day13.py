with open('input.txt') as input_file:
    points, folds = input_file.read().split('\n\n')
    points = [tuple(map(int, point.split(','))) for point in points.splitlines()]
    folds = [fold.split(' ')[-1] for fold in folds.splitlines()]

#  first iteration for sol1
value = int(folds[0][2:])
if folds[0][0] == 'y':
    points = set(list(map(lambda p: (p[0], value*2 - p[1]) if p[1] > value else p, points)))
elif folds[0][0] == 'x':
    points = set(list(map(lambda p: (value*2 - p[0], p[1]) if p[0] > value else p, points)))
print(f"sol1 is {len(points)}, read sol2 by yourself")

# remaining folds for sol2
for fold in folds[1:]:
    value = int(fold[2:])
    # not worth extracting and refactoring lambda functions
    if fold[0] == 'y':
        points = set(list(map(lambda p: (p[0], value*2 - p[1]) if p[1] > value else p, points)))
    elif fold[0] == 'x':
        points = set(list(map(lambda p: (value*2 - p[0], p[1]) if p[0] > value else p, points)))

# print sol2
for x in range(10):
    for y in range(50):
        if (y, x) in points:
            print('#', end='')
        else:
            print('.', end='')
    print()

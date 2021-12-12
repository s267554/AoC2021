with open('input.txt') as input_file:
    lines = input_file.read().splitlines()
    edges = [line.split('-') for line in lines]

sol = 0
paths = [(['start'], False)]
while len(paths) > 0:
    cur_path, twice_small = paths.pop()
    last_cave = cur_path[-1]
    if 'end' == last_cave:
        sol += 1
        continue
    # slow
    for edge in edges:
        if last_cave in edge:
            next_cave = edge[1] if last_cave == edge[0] else edge[0]
            if next_cave.isupper() or next_cave == 'end':
                paths.append((cur_path + [next_cave], twice_small))
            elif next_cave != 'start':
                occurrences = cur_path.count(next_cave)
                if not twice_small and occurrences == 1:
                    paths.append((cur_path + [next_cave], True))
                elif occurrences == 0:
                    paths.append((cur_path + [next_cave], twice_small))

print(f"sol is {sol}")
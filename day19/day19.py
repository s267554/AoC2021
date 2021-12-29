""" 3-D FIRST AND ONLY BRUTE FORCE"""

from collections import Counter

COMBS = []

# z is vectorial product or something
# there must be some itertools stuff for these for's
for face_dir in range(3):
    for face_sign in [-1, 1]:
        for up_dir in range(3):
            for up_sign in [-1, 1]:
                for z_dir in range(3):
                    for z_sign in [-1, 1]:
                        if len(set([face_dir, up_dir, z_dir])) == 3:
                            template = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            template[0][face_dir] = face_sign
                            template[1][up_dir] = up_sign
                            # fuck handedness
                            template[2][z_dir] = z_sign
                            COMBS.append(template)

def transform(beacon, trans_vect):
    res = list(beacon)
    for dim in range(3):
        value = 0
        for i, t in enumerate(trans_vect[dim]):
            value += beacon[i] * t
        res[dim] = value
    return res

def manhattan(b1, b2):
    dist = 0
    for i in range(3):
        dist += abs(b1[i] - b2[i])
    return dist


def main():
    with open('input.txt') as input_file:
        scanners = [[list(eval(beacon.rstrip())) for beacon in scanner.splitlines()[1:]] for scanner in input_file.read().split('\n\n')]

        abs_beacons = {tuple(b) for b in scanners[0]}
        offsets = [[0,0,0]]
        visited = [False for __ in scanners[1:]]

        while False in visited:
            for i, scanner in enumerate(scanners[1:]):
                if visited[i]:
                    continue

                for tr in COMBS:
                    list_offsets = []

                    beacons_transformed = [transform(b, tr) for b in scanner]

                    for start in abs_beacons:
                        for end in beacons_transformed:
                            offset = [end[dim] - start[dim] for dim in range(3)]
                            list_offsets.append(tuple(offset))
                    result = Counter(list_offsets).most_common(1)[0]
                    if result[1] > 11:
                        offsets.append(result[0])
                        for b in beacons_transformed:
                            newb = tuple(b[dim] - result[0][dim] for dim in range(3))
                            abs_beacons.add(newb)
                        visited[i] = True
                        break
        
        max_distance = 0
        for i in offsets:
            for j in offsets:
                distance = manhattan(i, j)
                if distance > max_distance:
                    max_distance = distance
        print(f"sol1 is {len(abs_beacons)} and sol2 is {max_distance}")

if __name__ == '__main__':
    main()
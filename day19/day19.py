""" 3-D FIRST AND ONLY BRUTE FORCE"""

from collections import Counter

COMBS = []

# z is vectorial product or something
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
                            # bruh check this 'vectorial product' sign lolz 
                            # dont need anymore, fuck handedness
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

with open('input.txt') as input_file:
    scanners = [[list(eval(beacon.rstrip())) for beacon in scanner.splitlines()[1:]] for scanner in input_file.read().split('\n\n')]

    map_scanner = [[] for __ in scanners]

    # scanner 0 is default
    # first is tansofrmation vector then offset then target
    map_scanner[0] = [[1,0,0],[0,1,0],[0,0,1]], [0,0,0], 0

    abs_beacons = {tuple(b) for b in scanners[0]}
    offsets = [[0,0,0]]

    visited = [False for __ in scanners]

    for __ in range(len(scanners)-1):
        for i, first_scanner in enumerate(scanners[1:]):
            if visited[i+1]:
                continue
            for tr in COMBS:
                list_offsets = []

                # print(first_scanner)
                beacons_transformed = [transform(b, tr) for b in first_scanner]
                # print(beacons_transformed)

                # now i cycle trough all possible pairings, calc offset then see if i get 12+ matches
                # lots of possibilities though
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
                    visited[i+1] = True
                    break
    
    max_distance = 0
    for i in offsets:
        for j in offsets:
            distance = manhattan(i, j)
            if distance > max_distance:
                max_distance = distance
    print(f"sol1 is {len(abs_beacons)} and sol2 is {max_distance}")

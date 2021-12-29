""" 3-D FIRST AND ONLY """

COMBS = []

# z is vectorial product or something
for face_dir in range(3):
    for face_sign in [-1, 1]:
        for up_dir in range(3):
            for up_sign in [-1, 1]:
                for z_dir in range(3):
                    if len(set([face_dir, up_dir, z_dir])) == 3:
                        template = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        template[0][face_dir] = face_sign
                        template[1][up_dir] = up_sign
                        # bruh check this 'vectorial product' sign lolz 
                        template[2][z_dir] = face_sign * up_sign
                        COMBS.append(template)

def transform():
    print("transform called")

def transpose():
    print("transpose called")


with open('test.txt') as input_file:
    scanners = input_file.read().split('\n\n')
    data = [[eval(beacon.rstrip()) for beacon in scanner.splitlines()[1:]] for scanner in scanners]



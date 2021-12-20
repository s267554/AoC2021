""" still no numpy uh? """

def pad(img, times=1, padding='.'):
    rows, cols = len(img), len(img[0])
    m = [list(padding*times + "".join(line) + padding*times) for line in img]
    for __ in range(times):
        m.insert(0, list(padding * (cols+2*times)))
        m.append(list(padding * (cols+2*times)))
    return m

def enhance(img):
    m = [line.copy() for line in img]
    for ir, row in enumerate(img):
        for ic, ch in enumerate(row):
            if ir > 0 and ic > 0 and ir < len(img)-1 and ic < len(img[0])-1:
                number = ''
                for i in range(ir-1, ir+2):
                    number += "".join(img[i][ic-1:ic+2])
                number = number.replace('.', '0')
                number = number.replace('#', '1')
                m[ir][ic] = algo[int(number, base=2)]
    return m

def crop(img, offset=1):
    return [line[offset:-offset] for line in img[offset:-offset]]

def draw(m):
    for line in m:
        print("".join(line))

if __name__ == "__main__":
    with open('input.txt') as input_file:
        algo, image = input_file.read().split('\n\n')
        image = [list(line) for line in image.splitlines()]

    # change this to target sol1 or sol2
    reps = 50
    image = pad(image, times=2*reps)
    for __ in range(reps):
        image = enhance(image)

    image = crop(image, offset=reps)

    #draw(image)
    sol = 0
    for row in image:
        for ch in row:
            sol = sol +1 if ch == '#' else sol
    print(f"sol is {sol}")
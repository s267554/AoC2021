sol = 0
puzzle = open("input.txt")

def contains(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    for s in set2:
        if s not in set1:
            return False
    return True

for line in puzzle.readlines():
    splitted_line = line.split('|')
    signs = splitted_line[0].strip().split(' ')
    outputs = splitted_line[1].strip()
    
    m, rev = dict(), dict()
        
    while len(m) < 10:
        for sign in signs:
            s = "".join(sorted(sign))
            if m.get(s):
                continue
            if len(s) == 2:
                m[s] = 1
                rev[1] = s
            elif len(s) == 3:
                m[s] = 7
                rev[7] = s
            elif len(s) == 4:
                m[s] = 4
                rev[4] = s
            elif len(s) == 7:
                m[s] = 8
                rev[8] = s
            elif len(s) == 6:
                if rev.get(4) and contains(s, rev[4]) and not rev.get(9):
                    m[s] = 9
                    rev[9] = s
                    continue
                if rev.get(9) and rev.get(1) and contains(s, rev[1]) and not rev.get(0):
                    m[s] = 0
                    rev[0] = s
                    continue
                if rev.get(9) and rev.get(0) and not rev.get(6) and not rev.get(6):
                    m[s] = 6
                    rev[6] = s
                    continue
            elif len(s) == 5:
                if rev.get(7) and contains(s, rev.get(7)):
                    m[s] = 3
                    rev[3] = s
                    continue
                if rev.get(3) and rev.get(6) and contains(rev.get(6), s):
                    m[s] = 5
                    rev[5] = s
                    continue
                if rev.get(3) and rev.get(5) and not rev.get(2):
                    m[s] = 2
                    rev[2] = s
                    continue
                    
    result = ""
    for o in outputs.split(' '):
        result += str(m["".join(sorted(o))])
    sol += int(result)
print(f"sol2 is {sol}")
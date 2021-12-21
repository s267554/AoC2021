# no dyn prog was like 20 secs
memo = dict()

dices = [1, 2, 3]
freqs = dict()
for d1 in dices:
    for d2 in dices:
        for d3 in dices:
            if d1+d2+d3 not in freqs:
                freqs[d1+d2+d3] = 1
            else:
                freqs[d1+d2+d3] += 1

# print(freqs)
# only consider u1
# got lucky


def play(p1, p2, s1, s2, turn):
    if (p1, p2, s1, s2, turn) in memo:
        return memo[(p1, p2, s1, s2, turn)]
    universes = 0
    if turn:
        if s2 > 20:
            return 0
        for key, value in freqs.items():
            tmp = (p1+key) % 10
            universes += value * play(tmp, p2, s1+tmp+1, s2, False)
    else:
        if s1 > 20:
            return 1
        for key, value in freqs.items():
            tmp = (p2+key) % 10
            universes += value * play(p1, tmp, s1, s2+tmp+1, True)
    memo[(p1, p2, s1, s2, turn)] = universes
    return universes

# input is first two args
print(play(3, 9, 0, 0, True))

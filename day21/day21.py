DICES = [1, 2, 3]
FREQS = {i: 0 for i in range(3,10)}
for d1 in DICES:
    for d2 in DICES:
        for d3 in DICES:
            FREQS[d1+d2+d3] += 1

# best way to refactor this symmetric blobs?
def play(pos1, pos2, score1, score2, turn):
    if (pos1, pos2, score1, score2, turn) in memo:
        return memo[(pos1, pos2, score1, score2, turn)]
    univ1, univ2 = 0, 0

    if turn:
        if score2 > 20:
            return (0, 1)
        for outcome, freq in FREQS.items():
            tmp = (pos1+outcome) % 10
            results = list(map(lambda a: a*freq, play(tmp, pos2, score1+tmp+1, score2, False)))
            univ1 += results[0]
            univ2 += results[1]
    else:
        if score1 > 20:
            return (1, 0)
        for outcome, freq in FREQS.items():
            tmp = (pos2+outcome) % 10
            results = list(map(lambda a: a*freq, play(pos1, tmp, score1, score2+tmp+1, True)))
            univ1 += results[0]
            univ2 += results[1]

    memo[(pos1, pos2, score1, score2, turn)] = (univ1, univ2)
    return (univ1, univ2)

# input is first two args
if __name__ == '__main__':
    memo = dict()
    print(max(play(3, 9, 0, 0, True)))
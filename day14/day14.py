from collections import Counter

with open('input.txt') as input_file:
    TEMPLATE, lines = input_file.read().split('\n\n')
    RULES = {key: value for (key, value) in [line.split(' -> ') for line in lines.splitlines()]}

pair_freq = {key: 0 for key in RULES.keys()}
for pair, freq in dict(Counter([TEMPLATE[i:i+2] for i in range(len(TEMPLATE)-1)])).items():
    pair_freq[pair] += freq

first = TEMPLATE[0]
last = TEMPLATE[-1]

def solve(iterations, freq_dict):
    for __ in range(iterations):
        new_freq_dict = freq_dict.copy()
        for pair, freq in freq_dict.items():
            new_pair1 = pair[0] + RULES[pair]
            new_pair2 = RULES[pair] + pair[1]
            new_freq_dict[new_pair2] += freq
            new_freq_dict[new_pair1] += freq
            new_freq_dict[pair] -= freq
        freq_dict = new_freq_dict

    freqs = dict()
    for pair, freq in freq_dict.items():
        for letter in pair:
            freqs[letter] = freqs[letter] + freq if letter in freqs else freq
    freqs = [int((value+1)/2 if key in [first, last] else value/2) for (key, value) in freqs.items()]
    freqs.sort()
    return freqs[-1] - freqs[0]

sol1 = solve(10, pair_freq.copy())
sol2 = solve(40, pair_freq.copy())

print(f"sol1 is {sol1} and sol2 is {sol2}")
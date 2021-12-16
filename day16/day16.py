"""that's pretty pretty ugly"""

with open('input.txt') as input_file:
    decode = "".join([f'{int(hexa, 16):04b}' for hexa in input_file.read()])

sol1 = 0
# many copies of str decode

def parsePacket(decode):
    version, packet_type = int(decode[0:3], 2), int(decode[3:6], 2)
    decode = decode[6:]

    global sol1
    sol1 += version

    if packet_type == 4:
        literal = ''
        while len(decode) >= 5:
            prefix, numb = decode[0], decode[1:5]
            decode = decode[5:]
            literal += numb
            if prefix == '0':
                break
        res = int(literal, 2)

    else:
        length_type = decode[0]
        decode = decode[1:]

        packet_values = []

        if length_type == '0':
            bits_to_read = int(decode[:15], 2)
            decode = decode[15:]

            toParse = decode[:bits_to_read]
            while len(toParse) >= 6:
                value, toParse = parsePacket(toParse)
                packet_values.append(value)
            decode = decode[bits_to_read:]

        elif length_type == '1':
            packets_to_read = int(decode[:11], 2)
            decode = decode[11:]

            for __ in range(packets_to_read):
                value, decode = parsePacket(decode)
                packet_values.append(value)

        if packet_type == 0:
            res = sum(packet_values)
        elif packet_type == 1:
            product = 1
            for v in packet_values:
                product *= v
            res = product
        elif packet_type == 2:
            res = min(packet_values)
        elif packet_type == 3:
            res = max(packet_values)
        elif packet_type == 5:
            res = int(packet_values[0] > packet_values[1])
        elif packet_type == 6:
            res = int(packet_values[0] < packet_values[1])
        elif packet_type == 7:
            res = int(packet_values[0] == packet_values[1])

    return res, decode

sol2 = parsePacket(decode)[0]
print(f"sol1 is {sol1} and sol2 is {sol2}")
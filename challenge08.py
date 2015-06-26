# Detect AES in ECB mode
import binascii
import itertools


# open file, strip \n and unhex
ciphertext = [binascii.unhexlify(lines.strip()) for lines in open('8.txt').readlines()]

def score(text, k=16):
    blocks = [text[i:i+k] for i in range(0, len(text), k)]
    pairs = itertools.combinations(blocks, 2)
    same = 0
    for p in pairs:
        if p[0] == p[1]:
            same += 1
    return same


for line_no, line in enumerate(ciphertext):
    if score(line) > 0:
        print("Line number: {}, Text -> {}".format(line_no, line))

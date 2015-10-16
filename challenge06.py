# It is offically on, now => Breaking repeating-key XOR
# File ('6.txt') as been based64'd after being encrypted with repeating-key XOR.
import base64
import itertools
from cf import break_single_byte_XOR, encode_repeating_key_XOR


def get_hamming_distance(x, y):
    "Return Hamming Distance of two strings (x,y)."
    if not isinstance(x, bytes):
        x = bytes(x, 'ascii')
    if not isinstance(y, bytes):
        y = bytes(y, 'ascii')
    return sum([bin(x[i] ^ y[i]).count('1') for i in range(len(x))])


def normalized_edit_distance(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)][0:4]
    pairs = list(itertools.combinations(blocks, 2))
    scores = [get_hamming_distance(p[0], p[1])/float(k) for p in pairs][0:6]
    return sum(scores) / len(scores)


def break_repeating_key_XOR(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposed_blocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [break_single_byte_XOR(bytes(x))[0] for x in transposed_blocks]
    return bytes(key)

    
# Solution
text = base64.b64decode(open('6.txt', 'r').read())
k = min(range(2, 41), key=lambda k: normalized_edit_distance(text, k))
key = break_repeating_key_XOR(text, k)
y = encode_repeating_key_XOR(text, key)
print("KEY: {} \n{}".format(key, y))

    

# It is offically on, now => Breaking repeating-key XOR
# File ('6.txt') as been based64'd after being encrypted with repeating-key XOR.
import base64
import itertools import combinations, zip_longest
from cpals import hamming



def normalized_edit_distance(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)][0:4]
    pairs = list(combinations(blocks, 2))
    scores = [hamming(p[0], p[1])/float(k) for p in pairs][0:6]
    return sum(scores) / len(scores)


def break_repeating_key_XOR(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposed_blocks = list(zip_longest(*blocks, fillvalue=0))
    key = [break_single_byte_XOR(bytes(x))[0] for x in transposed_blocks]
    return bytes(key)

    
# Solution
text = base64.b64decode(open('6.txt', 'r').read())
k = min(range(2, 41), key=lambda k: normalized_edit_distance(text, k))
key = break_repeating_key_XOR(text, k)
y = encode_repeating_key_XOR(text, key)
print("KEY: {} \n{}".format(key, y))

    

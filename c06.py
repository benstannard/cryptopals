# It is offically on, now => Breaking repeating-key XOR
# File ('6.txt') as been based64'd after being encrypted with repeating-key XOR.
from cpals import *


def normalized_edit_distance(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)][:4]
    pairs = list(combinations(blocks, 2))
    scores = [hamming(p[0], p[1])/float(k) for p in pairs]
    # return blocks, pairs, scores, sum(scores) / len(scores)
    return sum(scores) / len(scores)


def break_repeating_key_XOR(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposed_blocks = list(zip_longest(*blocks, fillvalue=0))
    key = [decrypt_xorc(bytes(x))[0] for x in transposed_blocks] # [0] returns the byte/codepoint
    return bytes(key)


def brxor(buffer, n=41): # break repeating key XOR
    k = min(range(2, n), key=lambda k: normalized_edit_distance(buffer, k))
    key = break_repeating_key_XOR(text, k)
    return key


# Solution
text = base64.b64decode(open('6.txt', 'r').read())
k = min(range(2, 41), key=lambda k: normalized_edit_distance(text, k))
key = break_repeating_key_XOR(text, k)
print("Key:", key)
print("RESULT")
print(rxor(text, key))

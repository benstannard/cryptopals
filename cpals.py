# cpals.py - Collection of crypto functions used
# All functions assume input is raw bytes. Unhexlify(input_params) when calling each function.
from binascii import unhexlify
from itertools import *
import base64


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def xorc(plain, key): # single character
    return xor(plain, bytes([key] * len(plain)))

def rxor(plain, key): # repeating key XOR
    return bytes([plain[i] ^ key[i % len(key)] for i in range(len(plain))])

def hamming(x, y): # Hamming Distance
    return sum([bin(x[i] ^ y[i]).count('1') for i in range(min(len(x), len(y)))])
     
def decrypt_xorc(buffer=None):
    "XOR each byte against input buffer and score with highest char frequency for best/max result"
    def key(s):
        return score(s[1]) 
    return max([(n, xorc(buffer, n)) for n in range(256)], key=key)

def score(s):
    "Func to score text based on character frequencies. Use max(..., key=score)"
    score = 0
    for i in s:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score

# From http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}


def test():
    assert(hamming(b'this is a test', b'wokka wokka!!!') == 37)

    print("Test pass")

test()

# c02.py
# str.encode returns an encoded version of the string as a bytes object
from binascii import unhexlify
from itertools import cycle
from cpals import *
from c03 import score

A = '1c0111001f010100061a024b53535009181c'
B = '686974207468652062756c6c277320657965'
C = '746865206b696420646f6e277420706c6179'


def xor(plain, key):
    "Input str and key. Cycle key so it's same length as str. XOR bytes."
    return bytes([a ^ b for a, b in zip(bytes.fromhex(plain), cycle(bytes.fromhex(key)))])


def rxor(plain, key):
    "Input str and key. Cycle key so it's same length as str. XOR bytes."
    ptest = lambda x: x if isinstance(x, bytes) else bytes.fromhex(x)
    ktest = lambda x: x if isinstance(x, bytes) else bytes.fromhex(x)
    p = ptest(plain)
    k = ktest(key)
    return bytes([p[i] ^ k[i % len(k)] for i in range(len(p))])


def test():
    rv = xor(A, B)
    thekid = unhexlify(C) # reads b"the kid don't play"
    assert rv == thekid
    print("Tests pass.")


test()

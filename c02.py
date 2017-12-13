# c02.py
# str.encode returns an encoded version of the string as a bytes object
import binascii
from itertools import cycle


A = '1c0111001f010100061a024b53535009181c'
B = '686974207468652062756c6c277320657965'
C = '746865206b696420646f6e277420706c6179'


def xor(s, key):
    "Input hex-string, unhex to operate on bytes and XOR against supplied key"
    #TODO: add if not isinstance() tests to covert hex to bytes
    k = cycle(binascii.unhexlify(key))
    return ''.join([chr(int(a) ^ int(b)) for a, b in zip(binascii.unhexlify(s), k)]).encode("UTF-8")


def test():
    rv = xor(A, B)
    final = binascii.unhexlify(C)
    assert rv == final
    print("Tests pass.")


test()

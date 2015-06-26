# cf.py : crypto functions
# collection of all crypto functions

import binascii
import itertools
from Crypto.Util.strxor import strxor_c

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


##
## Decrypting and scoring functions
##
def score(byte_string):
    """
    Input a byte repsentation of string. 
    Index each byte, convert to letters. 
    Use letter frequencies to score/rank.
    """
    score = 0
    for i in byte_string:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score


def break_single_byte_XOR(s):
    'Input byte string s. XOR each letter in s against all chars. Return max score base on char frequency.'
    def key(p):
        return score(p[1]) # 2nd element in tuple below
    return max([(i, strxor_c(s, i)) for i in range(0, 256)], key=key)


##
## Encrypting functions
##

def encode_repeating_key_XOR(text, key):
    """
    Inputs: plaintext & key. If not bytes, convert to bytes.
    XOR each letter in plaintext in repeating cycle against key, allowing key length != length of plaintext.
    Returns: Encrypted Ciphertext. From bytes doc: bytes(iterable_of_ints) -> immutable array of bytes. 
    """
    if not isinstance(text, bytes):
        text = bytes(text, 'ascii')
    if not isinstance(key, bytes):
        key = bytes(key, 'ascii')
#    return bytes([b1 ^ b2 for b1, b2 in zip(plainbytes, itertools.cycle(keybytes))])
    return bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])



##        
## Helper function for string encode/decoding
##
def get_hamming_distance(x, y):
    "Return Hamming Distance of two strings (x,y)."
    if not isinstance(x, bytes):
        x = bytes(x, 'ascii')
    if not isinstance(y, bytes):
        y = bytes(y, 'ascii')
    return sum([bin(x[i] ^ y[i]).count('1') for i in range(len(x))])

def hex_to_str(hexstr, encoding='utf-8'):
    "Decode the given hex as if it is a plaintext string."
    return binascii.a2b_hex(hexstr).decode(encoding=encoding)

def bytes_to_base64(b):
    "Return an ASCII-encoded base64 text representing the given bytes."
    return base64.b64encode(b).decode()

def bytes_to_hex(b):
    return binascii.b2a_hex(b).decode()

def str_to_bytes(text):
    return bytes(text, encoding='utf-8')

def base64_to_bytes(b):
    return base64.b64decode(b)

def print_bytes_maps(bytestring):
    'Returns which hex character maps to each integer.'
    if isinstance(bytestring, bytes):
        return "{} maps to hex ->{}".format((i, hex(i)) for i in bytestrting)

def modulo_practice(bytestr, key):
    if not isinstance(bytestr, bytes):
        bytestr = bytes(bytestr, 'ascii')
    for i in range(len(bytestr)):
        print("{} mod 3 -> {}".format(i, i % len(key)))

def convert_to_bits(n, pad):
    result = []
    while n > 0:
        if n % 2 == 0:
            result = [0] + result
        else:
            result = [1] + result
        n = n / 2
    while len(result) < pad:
        result = [0] + result
    return result


def string_to_bits(s):
    result = []
    for c in s:
        results = result + convert_to_bits(ord(c), 7)
    return result




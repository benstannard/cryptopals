"""
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
"""
import binascii
import base64
from Crypto.Util.strxor import strxor

x = '1c0111001f010100061a024b53535009181c'
xor = '686974207468652062756c6c277320657965'
expectedY = '746865206b696420646f6e277420706c6179'
print()
print("X:", x, len(x))
print("XOR:", xor, len(xor))
print("ExpectedY:", expectedY, len(expectedY))
print()

print("now unhexlified")
unhex_x = binascii.unhexlify(x)
unhex_xor = binascii.unhexlify(xor)
unhex_y = binascii.unhexlify(expectedY)
print(unhex_x, len(unhex_x))
print(unhex_xor, len(unhex_xor))
print(unhex_y,len(unhex_y))
print()

u = strxor(unhex_x, unhex_xor)
print("strxor", u)




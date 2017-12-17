# Convert hex to base64
import binascii
import base64

x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
y = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex_to_base64(s):
    "input a string type hex. output to base64."
    return base64.b64encode(binascii.unhexlify(s)).decode('utf-8')


def test():
    assert hex_to_base64(x) == y
    print("Test passed")


test()

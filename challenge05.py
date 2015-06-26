# Implement repeating-key XOR
import binascii

x = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
y = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
key = 'ICE'



def repeating_key_xor(text, key):
    """
    Inputs: plaintext & key. If not bytes, convert to bytes
    Function XOR each letter in plaintext in repeating cycle against key, allowing key length != length of plaintext.
    Returns: Encrypted Ciphertext. From bytes doc: bytes(iterable_of_ints) -> immutable array of bytes. 
    """
    if not isinstance(text, bytes):
        text = bytes(text, 'ascii')
    if not isinstance(key, bytes):
        key = bytes(key, 'ascii')
    return bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])


r = repeating_key_xor(x, key)
print("Result -> {}".format(r))


def test():
    assert binascii.hexlify(r).decode() == y
    print("All tests passed.")

test()


        

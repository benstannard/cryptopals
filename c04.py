# Detect single-characer XOR
import binascii
from cf import score, break_single_byte_XOR

def f(filename=None):
    decoded_lines = [binascii.unhexlify(lines.strip()) for lines in open(filename).readlines()]
    best_text = [break_single_byte_XOR(i)[1] for i in decoded_lines] # index tuple
    return max(best_text, key=score)

result = f('4.txt')
print(result)

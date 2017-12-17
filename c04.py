# Detect single-characer XOR
from binascii import unhexlify
from cpals import decrypt_xorc, score, freqs


def f(filename=None):
    lines = [unhexlify(lines.strip()) for lines in open(filename).readlines()]
    decoded = [decrypt_xorc(line) for line in lines]
    scored = sorted([(score(line[1]), line) for line in decoded])
    return max(scored)


def test():
    result = f('4.txt')
    print(result)


test()

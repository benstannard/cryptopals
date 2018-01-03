# AES in ECB mode, Electronic Codebook (ECB) 
# openssl enc -aes-128-ecb -d -in 7.txt  # bad magic number
import base64
from Crypto.Cipher import AES

text = base64.b64decode(open('7.txt', 'r').read())
key = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)
decoded = key.decrypt(text).decode("UTF-8")
print(decoded)


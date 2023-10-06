import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


with open(os.path.join("/home/cse/Lab3/Q4files", "Encrypted4"), 'rb') as f:
    iv = f.read(16)
    ciphertext = f.read()
key = b'\x98\xd6)\x99\xcf\xb7\xb3b\xcfi7\xc6\xbcXO\xb0'
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
with open('Q4a', 'a') as f:
    f.write(plaintext.decode())

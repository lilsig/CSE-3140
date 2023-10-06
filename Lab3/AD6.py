import os
import sys
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA


def get_decryption_key(filename):
    with open(filename, 'rb') as f:
        encrypted_key = f.read()
    d_key = open("/home/cse/Lab3/Solutions/d.key", 'rb')
    private_key = RSA.import_key(d_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    shared_key = cipher_rsa.decrypt(encrypted_key)
    return shared_key


if __name__ == "__main__":
    identifier = sys.argv[1]
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".ID"):
            with open(filename) as f:
                cur_identifier = f.read()
            if cur_identifier.strip() == identifer:
                file_to_decrypt = filename[:-3]
                print(f"{file_to_decrypt} encryption key is:")
                print(get_decryption_key(f"{file_to_decrypt}.key"))





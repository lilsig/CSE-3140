import sys
import ast
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(AES.block_size)
        cipthertext = f.read()


    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)


    with open(output_file, 'wb') as f:
        f.write(plaintext)


if __name__ = "__main__":
    encrypted_filename = sys.argv[1]
    filename = encrypted_filename[:-10]
    key_input = input("Enter decrypted key: ")
    key = ast.literal_eval(key_input)
    decrypt_file(encrypted_filename, filename, key)
    print(f"{filename} has been restored")

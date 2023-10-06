import sys
import os
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
if __name__ == "__main__":
    path = '/home/cse/Lab3/'
    os.chdir(path)
    with open("Q3pk.pem", "rb") as f:
        key = RSA.import_key(f.read())


    for filename in os.listdir('Q3files'):
        if filename.endswith(".exe.sign"):
            continue


        with open(os.path.join("/home/cse/Lab3/Q3files", filename), "rb") as f:
            data = f.read()
            #data = data.decode()
            h = SHA256.new(data)


        sf = filename + ".sign"
        with open(os.path.join("/home/cse/Lab3/Q3files", sf), "rb") as f:
            priv_key = f.read()


        try:
            pkcs1_15.new(key).verify(h, priv_key)
            with open("Q3a", "a") as f:
                print(filename)
                f.write(filename + "\n")
        except:
            pass



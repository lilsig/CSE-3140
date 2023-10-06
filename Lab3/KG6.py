from Crypto.PublicKey import RSA
key = RSA.generate(2048)
pub_key = key.publickey().export_key()
priv_key = key.export_key()
with open('e.key', 'wb') as f:
    f.write(pub_key)


with open('d.key', 'wb') as f:
    f.write(priv_key)

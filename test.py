from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

import random
random_generator=Random.new().read
key=RSA.generate(1024,random_generator)
public_key=key.publickey()
print public_key.exportKey('RSA')
pubkey=RSA.importKey(public_key.exportKey('OpenSSH'))
hash=SHA256.new("jello").digest()
signature=key.sign(hash, '')
print signature

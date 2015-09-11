import xml.etree.ElementTree as ET

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from Crypto.Hash import SHA256
from base64 import b64decode 

rsakey=RSA.importKey('ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC4AGw0zx2qPXXyKAmn2/GE+NSUFNvnDZl3AjrxG45pdprrl6MpsF8vyQyR4nxumPKxgRNR709pTOLbhnr5M6O3akIJORxIc+zi8Qp0l/Ocy4nBxqf7ln+Lpy2W2JGchxaVLw4c+NQqELo74LNsTeg3RQQT9bEK09v9jACWQp+Hcw==')

inbox=ET.parse('email.xml').getroot()

i=0
for email in inbox.findall('email'):
    i=i+1
    print "checked "+str(i)+" messages."
    for signature in email.findall('signature'):
        for message in email.findall('message'):
            sig=b64decode(signature.text)
            signer=PKCS1_v1_5.new(rsakey)
            mes=message.text
            digest = SHA256.new()
            digest.update(b64decode(mes))
            if signer.verify(digest, sig):
                print 'verified message: '+mes

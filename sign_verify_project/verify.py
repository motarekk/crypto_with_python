import sys
from Crypto.Util.number import bytes_to_long
from hashlib import sha256

# usage
usage = "Usage:\n> python verify.py [firmware] [fw_signature] [pubkey]"
if len(sys.argv) < 2:
    print(usage)
    exit()

# hash function
def hash(dat):
    hash = sha256()
    hash.update(dat)
    return hash.digest()

# INPUT: firmware file, signature file, and public key
with open(sys.argv[1], "rb") as fw_file:
    fw = fw_file.read()
    fw_file.close()

with open(sys.argv[2], "rb") as fw_signature:
    S = int(fw_signature.read())
    fw_signature.close()

with open(sys.argv[3], "rb") as pubkey:
    n = int(pubkey.readline())
    e = int(pubkey.readline())
    pubkey.close()

# caclulate the sha2 of the firmware 
H = bytes_to_long(hash(fw))

# verify signature 
verify = pow(S, e, n)

# check the output of verification with the hash generated in the first step
if verify == H:
    print("Verification Succeeded!")
else:
    print("Verification Failed")
import sys
from Crypto.Util.number import bytes_to_long
from hashlib import sha256

# usage
usage = "Usage:\n> python sign.py [firmware] [privkey]"
if len(sys.argv) < 2:
    print(usage)
    exit()

# hash function
def hash(dat):
    hash = sha256()
    hash.update(dat)
    return hash.digest()

# INPUT: firmware file, private key 
with open(sys.argv[1], "rb") as fw_file:
    fw = fw_file.read()
    fw_file.close()

with open(sys.argv[2], "rb") as privkey:
    n = int(privkey.readline())
    d = int(privkey.readline())
    privkey.close()

# calculate tha sha2 digest of the firmware
H = bytes_to_long(hash(fw))

# sign the firmware with your RSA private key
S = pow(H, d, n)

# OUTPUT: FW_signature.txt
with open("FW_signature.txt", "w") as fout:
    fout.write(str(S))
    print("signature saved to FW_signature.txt")
    fout.close()
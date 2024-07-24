from Crypto.Util.number import *

# RSA parameters
p = getPrime(1024)       
q = getPrime(1024)       
n = p * q               
phi = (p-1) * (q-1)     
e = 65537               
d = pow(e, -1, phi)  

# Saving public and private keys to a file
with open("pubkey.txt", "w") as pubkey:
    pubkey.write(str(n)+'\n')
    pubkey.write(str(e))
    pubkey.close()

with open("privkey.txt", "w") as privkey:
    privkey.write(str(n)+'\n')
    privkey.write(str(d))

# info
print("public key is saved to pubkey.txt\nprivate key is saved to privkey.txt")

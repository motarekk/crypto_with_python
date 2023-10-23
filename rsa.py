"""
RSA encryption/decryption
"""

from Crypto.Util.number import *    # pip install pycryptodom

# parameters
p = getPrime(1024)
q = getPrime(1024)
n = p * q              # public field
phi = (p-1) * (q-1)    # private field
e = (2**16)+1          # 65537 [lookup: https://en.wikipedia.org/wiki/65,537]
d = pow(e, -1, phi)

PT = bytes_to_long(b'rsa is cool')
CT = pow(PT, e, n)
decrypted = long_to_bytes(pow(CT, d, n))

# demo
print(f"plaintext: {PT}\nciphertext: {CT}\ndecrypted: {decrypted}")

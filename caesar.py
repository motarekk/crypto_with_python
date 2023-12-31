"""
Caesar Cipher Encryption/Decryption 
Caesar Cipher is a stream symmetric cipher
key space == 1 to len(alphabet)-2 == 1 to 24 --> brute-forcable
stream cipher: encryption & decryption is done bit-by-bit
symmetric cipher: encryption & decryption is done with the secret key
Author: motarek
"""
from os import urandom

alphabet = "abcdefghijklmnopqrstuvwxyz"

# encryption
def caesar_encrypt(plaintext, key): #__INPUT__#
    # check key is between 1 to 24
    # assert --> make sure
    assert key > 0

    plaintext = plaintext.lower()
    ciphertext = ''

    #__PROCESS__#
    for state in plaintext:
        # skip special characters
        if state not in alphabet:
            ciphertext += state
        else:
            ciphertext += alphabet[(alphabet.index(state) + key)%25 ] # use mod to keep the alphabet field of 24

    #__OUTPUT__#
    return ciphertext

# decryption
def caesar_decrypt(ciphertext, key): #__INPUT__#
    # check key is between 1 to 24
    # assert --> make sure
    assert key > 0

    ciphertext = ciphertext.lower()
    plaintext = ''
    
    #__PROCESS__#
    for state in ciphertext:
        # skip special characters
        if state not in alphabet:
            plaintext += state
        else:
            plaintext += alphabet[ (alphabet.index(state) - key)%25 ] # use mod to keep the alphabet field of 24
    
    #__OUTPUT__#
    return plaintext

# === helper functions === #
def get_random_key():
    return int(urandom(1).hex(), 16)%25

# === demo === # 
# parameters
key = get_random_key()

# encryption
plaintext = "I love cryptography"
print(f"===== Caesar encryption demo =====\nplaintext: {plaintext}, key: {key}")
print(f"encrypted: {caesar_encrypt(plaintext, key)}")
print(f"---------------------------------------------")

# decryption
ciphertext = caesar_encrypt(plaintext, key)
print(f"===== Caesar decryption demo =====\nciphertext: {ciphertext}, key: {key}")
print(f"decrypted: {caesar_decrypt(ciphertext, key)}")

"""
# === additional knowledge === #
[[ About Security Level ]]
Security level of an algorithm is the number of operations required to break it, and it's measured by 'bits of security'
Number of operations required to break an algorithm = 2**n, where n represents 'bits of security'
Caesar Cipher ---> 2**4 + 8 = 24 operations --> weak against bruteforce attack
AES-128: 128  ---> 2**128 operations --> after Biclique attack: 2*126.1
AES-192: 192  ---> 2**192 operations --> after Biclique attack: 2*189.7
AES-256: 256  ---> 2**256 operations --> after Biclique attack: 2*254.4
"""

'''
Caesar/ROT Cipher Brute-Forcer
Author: motarek
'''
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#---- INPUT ----#
ciphertext = ''

# take input from user
for arg in ' '.join(sys.argv[1:]):
    ciphertext += arg

#---- PROCESS ----#
def caesar_decrypt(ciphertext, key): # input
    # check key is an integer and is > 0
    assert key > 0

    ciphertext = ciphertext.upper()
    plaintext = ''

    for state in ciphertext:
        # skip special characters
        if state not in alphabet:
            plaintext += state
        else:
            plaintext += alphabet[ (alphabet.index(state) - key)%25 ] # use mod to keep the alphabet field of 24

    return plaintext

def bruteforce(ciphertext):
    for i in range(1, 25):
        print(f"{i}: {caesar_decrypt(ciphertext, i)}")

#---- OUTPUT ----#
bruteforce(ciphertext)

"""
Implementation of Simplified Data Encryption Standard (S-DES)
Results are not correct. Troubleshoot of the code is required
"""

def sdes_encrypt(plaintext, key) -> str:    
    # subkey generation
    subkeys = subkey_generation(key)

    # initial permutation
    state = initial_permutation(plaintext)

    # two rounds of feistel network
    for i in range(2):
        state = feistel(state, subkeys[i])

    # final permutation
    ciphertext = final_permutation(state)

    return ciphertext

def sdes_decrypt(ciphertext, key) -> str:
        # subkey generation
    subkeys = subkey_generation(key)

    # initial permutation
    state = initial_permutation(ciphertext)

    # two rounds of feistel network
    for i in range(1, -1, -1):
        state = feistel(state, subkeys[i])

    # final permutation
    plaintext = final_permutation(state)
    
    return plaintext

def subkey_generation(key) -> list: 
    # P10
    key = permutation_10(key)

    # divide
    L = key[:4]
    R = key[4:]

    # left shift by 1
    L = L[1:] + L[0]
    R = R[1:] + R[0]

    # generate first subkey
    subkey_1 = permutation_8(L + R)

    # left shift by 2
    L = L[1:] + L[0]
    R = R[1:] + R[0]

    # generate second subkey
    subkey_2 = permutation_8(L + R)

    subkeys = [subkey_1, subkey_2]

    return subkeys

def initial_permutation(plaintext) -> str:
    IP = [1, 5, 2, 0, 3, 7, 4, 6]
    permuted_text = ""
    for i in IP:
        permuted_text += plaintext[i]
    return permuted_text

def expand_permutation(R0) -> str:
    E_P = [3, 0, 1, 2, 1, 2, 3, 0]
    permuted_text =""
    for i in E_P:
        permuted_text += R0[i]
    return permuted_text

def permutation_4(R0_F) -> str:
    P4 = [1, 3, 2, 0]
    permuted_text = ""
    for i in P4:
        permuted_text += R0_F[i]
    return permuted_text

def permutation_10(key):
    P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    permuted_key = ""
    for i in P10:
        permuted_key += key[i]
    return permuted_key
    
def permutation_8(key):
    P8 = [5, 2, 6, 3, 7, 4, 9, 8]
    permuted_key = ""
    for i in P8:
        permuted_key += key[i]
    return permuted_key

def final_permutation(state) -> str:
    IP_1 = [3, 0, 2, 4, 6, 1, 7, 5]
    permuted_text = ""
    for i in IP_1:
        permuted_text += state[i]
    return permuted_text

def sbox_0(L) -> str:
    S0 = [['01', '11', '00', '11'], ['00', '10', '10', '01'], ['11', '01', '01', '11'], ['10', '00', '11', '10']]
    row = int(L[0] + L[3], 2)
    column = int(L[1] + L[2], 2)
    sboxed = S0[column][row]
    return sboxed

def sbox_1(R) -> str:
    S1 = [['00', '10', '11', '10'], ['01', '00', '00', '01'], ['10', '01', '01', '00'], ['11', '11', '00', '11']]
    row = int(R[0] + R[3], 2)
    column = int(R[1] + R[2], 2)
    sboxed = S1[column][row]
    return sboxed

def feistel(state, subkey) -> str:
    # divide state
    L0 = state[:4]
    R0 = state[4:]

    R1 = pad(xor(L0, F(R0, subkey)), 4)
    L1 = R0
    state = L1 + R1
    return state

def F(R0, subkey) -> str:
    # E/P
    R0_F = expand_permutation(R0)

    # XOR with subkey
    R0_F = pad(xor(R0_F, subkey), 8)

    # divide R0_F
    L = R0_F[:4]
    R = R0_F[4:]

    # s-box
    L = sbox_0(L)
    R = sbox_1(R)
    R0_F = L + R

    # P4
    R0_F = permutation_4(R0_F)
    return R0_F

# HELPER FUNCTIONS
def xor(a, b):
    return bin(int(a, 2) ^ int(b, 2)).replace('0b', '')

def pad(a, b):
    while len(a) < b:
        a = '0' + a
    return a

# DEMO
plaintext = '01110010'
key = '1010000010'
ciphertext = sdes_encrypt(plaintext, key)
decrypted = sdes_decrypt(ciphertext, key)
print("==== sdes demo ====")
print(f"plaintext = {plaintext}\nciphertext = {ciphertext}\ndecrypted = {decrypted}")

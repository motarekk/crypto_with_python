"""
Implementation of Simplified Data Encryption Standard
S-DES encryption/decryption
plaintext & key must be input in binary
Author: motarek
"""

# encryption
def des_encrypt(plaintext, key):
    state = plaintext

    # subkey generation (scheduling) = generate 2 subkeys
    subkeys = generate_subkey(key)

    # initial permutation
    state = ip(state)

    # 2 fiestel networks
    for i in range(2):
        state = feistel(state, subkeys[i])

    # final permutation
    state = ip_1(state)
    
    ciphertext = state

    return ciphertext


def generate_subkey(key):
    # P10
    key = p10(key)

    # split key
    key_l = key[:5]
    key_r = key[5:]
    
    # LS-1
    key_l_shifted = key[:5]
    key_r_shifted = key[5:]
    #__ to be completed __#

    key = key_l_shifted + key_r_shifted

    # P8 --> subkey 0
    subkey_0 = p8(key)

    # LS-2 
    key_l_shifted = key[:5]
    key_r_shifted = key[5:]
    #__ to be completed __#

    key = key_l_shifted + key_r_shifted

    # P8 --> subkey 1
    subkey_1 = p8(key)

    return subkey_0, subkey_1


def feistel(state, subkey):
    # split state
    state_l = state[:4]
    state_r = state[4:]

    # first round function
    f_state_r = round_function(state_r, subkey)

    # XOR right side with left side of the state
    state_l = state_l ^ f_state_r

    state = state_r + state_l

    return state


def round_function(state, subkey):
    output = ''

    # E/P (Expansion Permutation)
    state = e_p(input)
    
    # XOR with subkey
    state ^= subkey

    # Sbox
    state = sbox(state)

    # P4
    state = p4(state)

    return output


# === permutation & substitution functions === #
def p10(input):
    output = ''
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]   

    for i in range(10):
        for j in P10:
            output[i] = input[j]

    return output
    
def p8(input):
    output = ''
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]   

    for i in range(10):
        for j in P8:
            output[i] = input[j]

    return output

def p4(input):
    output = ''
    P4 = [2, 4, 3, 1]

    for i in range(10):
        for j in P4:
            output[i] = input[j]

    return output

# IP (Initial Permuation)
def ip(input):
    output = ''
    IP = [2, 6, 3, 1, 4, 8, 5, 7]

    for i in range(10):
        for j in IP:
            output[i] = input[j]

    return output

# IP**-1 (Final Permutation)
def ip_1(input):
    output = ''
    IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]

    for i in range(10):
        for j in IP_1:
            output[i] = input[j]

    return output

# E/P (Expansion Permutation)
def e_p(input):
    output = ''
    E_P = [4, 1, 2, 3, 2, 3, 4, 1]

    for i in range(10):
        for j in E_P:
            output[i] = input[j]

    return output

def sbox(input):
    output = ''

    # split input
    input_0 = input[:4] 
    input_1 = input[4:]

    # sboxes
    S0 = [['01', '11', '00', '11'], ['00', '10', '10', '01'], ['11', '01', '01', '11'], ['10', '00', '11', '10']]
    S1 = [['00', '10', '11', '10'], ['01', '00', '00', '01'], ['10', '01', '01', '00'], ['11', '11', '00', '11']]

    # substitution
    #___ to be completed ___#

    return output

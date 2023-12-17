# crypto_with_python
A short course for AOU students

## Outline
[ Module 1: Introduction to Cryptography ]
- What is cryptography? (encryption = plaintext -> cipher(algorithm) -> ciphertext)
- Cryptography objectives (confidentiality, integrity, authenticity, non-repudiation)
- Applications of cryptography (VPN, file encryption, software signing, online banking,..)
- Cryptography mechanisms (transposition, substitution)
- Basic cryptnalysis techniques (bruteforce, frequency analysis, extracting patterns)
- Historical (classical) Ciphers (Caesar, Playfair, Vigenère)
- Implementing Caesar Cipher encryption/decryption & bruteforce in python
- Design your own cipher

[ Module 2: Modern Cryptography ]
- Evolution of symmetric ciphers (Caesar, Enigma, DES, 3DES, AES, Ascon)
- Feistel Network (cipher)
- Data Encryption Standard (DES)
- Implementing Simplified DES (S-DES) in python
- Rijndael Cipher = Advnaced Encryption Standard (AES)
- Galois Field of AES GF(2**8)
- Block ciphers modes of operation: ECB, CBC, OFB, CFB, CTR
- AES encryption/decryption using python pycryptomoe library
- Encrypting/decrypting files in AES using openssl command-line tool
- Asymmetric ciphers: RSA algorithm: encryption/decryption & signing/verifying
- Implementing RSA in python
- Solving CTF challenges for AES & RSA
- Design your own cipher

[ Module 3: Lightweight Cryptography ]
- Authenticated Encryption with Associated Data (AEAD)
- What is hashing? What are the most known hashing functions? (MD5, SHA1, SHA2, SHA3)
- NIST Lightweight Cryptography (LWC) project for developing more lightweight ciphers than AES-GCM
- Ascon Cipher (NIST LWC winner in 2023): encryption/decryption & hashing
- Ascon Family: Ascon AEAD, Ascon Hash, Ascon XOF (eXtendible Output Function)

[ Pratical resources ]
- Course repository on GitHub: https://github.com/motarekk/crypto_with_python/
- Cryptohack platform: https://cryptohack.org/

[ Other links ]
- YouTube (some sesions are online): https://www.youtube.com/watch?v=wIrHNBla4ns&list=PLeI2QhZHGbbgEeZI6eMS2jNXoqHhE9RFH
- Medium (writeups): https://medium.com/@motarekk

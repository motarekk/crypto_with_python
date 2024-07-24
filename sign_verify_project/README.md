# Enjoy the project

#### 1- Compile firmware
> gcc -o FW fw.c

#### 2- Generate RSA keypair
> python keygen.py

#### 3- Sign firmware with private key
> python sign.py FW.exe privkey.txt

#### 4- Verify firmware signature with public key
> python verify.py FW.exe FW_signature.txt pubkey.txt

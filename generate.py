#!/usr/bin/python

def generate_pw(n, pw, total):
    if n == 0:
        print pw
    else:
        if len(pw) == 0 or len(pw) == total-1:
            for i in range(65, 90):
                pw2 = pw + chr(i)
                generate_pw(n-1, pw2, total)            
        else: 
            for i in range(33, 126):
                pw2 = pw + chr(i)
                generate_pw(n-1, pw2, total)

generate_pw(5, "", 5)

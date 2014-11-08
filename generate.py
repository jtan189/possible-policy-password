#!/usr/bin/python

def generate_pw(n, pw):
    if n == 0:
        print pw
    else:
        for i in range(33, 126):
            pw2 = pw + chr(i)
            generate_pw(n-1, pw2)

generate_pw(5, "")


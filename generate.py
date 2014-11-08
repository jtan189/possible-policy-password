#!/usr/bin/python
vowels = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]

def generate_pw(n, pw, total, num_vowels):
    if n == 0:
        if num_vowels >= 3:
            print pw
    else:
        low = 33
        high = 126
        if len(pw) == 0 or len(pw) == total-1:
            low = 65
            high = 90

        for i in range(low, high):
            num_vowels2 = num_vowels
            if i in vowels:
                num_vowels2 = num_vowels+1
            pw2 = pw + chr(i)
            generate_pw(n-1, pw2, total, num_vowels2)

generate_pw(5, "", 5, 0)

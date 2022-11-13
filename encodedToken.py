#!/bin/env python3

import base64

# Simple Python Script to make a wordlist for Authentication Token
# Authentication Token = USER:PASSWORD
# Now that we can make a Authentic Token word list, we can Fuzz it.

with open ('wordlist.txt','r') as f:
    for word in f :
        token = "admin:"+word
        print("Encoding... " + token)
        base64_bytes = token.encode("ascii")
        enc = base64.b64encode(base64_bytes)
        print(enc)
        with open ("encoded_wordlist.txt",'a') as w:
            w.write(str(enc) + "\n")
        print("Done \n -------------------")
print("Task is Complete \n  -----xx-----xx-----")

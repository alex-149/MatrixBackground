import secrets
import random 
import string
import time

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
pwd = ''
pwd += ''.join(secrets.choice(alphabet))

while True:
    time.sleep(0.005)
    print(pwd)  
    pwd = ''
    for i in range(209):
        pwd += ''.join(secrets.choice(alphabet))
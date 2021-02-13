import re
from cryptography.fernet import Fernet

p= input("Enter your Reference ID : ")

if re.match('^[a-zA-Z0-9]+$',p):
    if(len(p) == 12):
        print("Valid Reference ID")
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(bytes(p, "utf-8"))
        print("Encrypted Reference ID : " + str(encoded_text))
        decoded_text = cipher_suite.decrypt(encoded_text)
        print("Decrypted Reference ID : " + str(decoded_text))
    else:
        print("Reference ID should be 12 Digits")
else:
    print("Reference ID should contain only alphanumeric")

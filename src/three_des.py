"""
Szyfrowanie tekstu przy pomocy algorytmu 3DES.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/pyDes/
"""


from pyDes import *
from binascii import unhexlify as unhex


def encrypt_by_3des(message, key):
    """ Encrypting message using 3DES in ECB Mode """
    return key.encrypt(message)


def decrypt_3des(message, key):
    """ Decrypting message """
    return key.decrypt(message)


def fill_to_eight(message):
    if(len(message)%8 == 0):
        return message
    else:
        for i in range(len(message)%8+2):
            message += " "
        return message



def main():
    """ Crypt&Decrypt message using 3DES """
    message = input("Podaj wiadomość: ")
    message = fill_to_eight(message)
    message = bytes(message, encoding='utf-8')

    key = triple_des(unhex("133457799BBCDFF1112233445566778877661100DD223311"))

    encrypted_message = key.encrypt(message)
    print("Zaszyfrowany tekst: ", encrypted_message)

    decrypted_message = key.decrypt(encrypted_message)
    print("Odszyfrowany tekst: ", decrypted_message.decode("ISO-8859-1").rstrip('\0'))


if __name__ == "__main__":
    main()

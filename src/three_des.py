"""
Szyfrowanie tekstu przy pomocy algorytmu 3DES.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/pyDes/
"""


from pyDes import *
import timeit
from utils.pad import fill_to_block


def encrypt_by_3des(message, key):
    """ Encrypting message using 3DES in ECB Mode """
    return key.encrypt(message)


def decrypt_3des(message, key):
    """ Decrypting message """
    return key.decrypt(message)


def main():
    """ Crypt&Decrypt message using 3DES """
    message = input("Podaj wiadomość: ")
    message = fill_to_block(message, 8)
    message = bytes(message, encoding='utf-8')

    key = input("Podaj klucz: \n")
    key = fill_to_block(key, 16)
    key = triple_des(key)

    starttime = timeit.default_timer()
    encrypted_message = key.encrypt(message)
    print("Czas szyfrowania używając 3DES: ", timeit.default_timer() - starttime, "s")
    print("Zaszyfrowany tekst: ", encrypted_message)

    starttime = timeit.default_timer()
    decrypted_message = key.decrypt(encrypted_message)
    print("Czas odszyfrowania 3DES: ", timeit.default_timer() - starttime, "s")
    print("Odszyfrowany tekst: ", decrypted_message.decode("ISO-8859-1").rstrip('\0'))


if __name__ == "__main__":
    main()

"""
Szyfrowanie tekstu przy pomocy algorytmu DES.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/des/
"""

from des import DesKey
import timeit
from utils.pad import fill_to_block


def encrypt_by_des(message, key):
    """ Encrypting message using DES in ECB Mode """
    return key.encrypt(message, padding=True)


def decrypt_des(message, key):
    """ Decrypting message and removing padding from message """
    return key.decrypt(message, padding=True)


def main():
    """ Crypt&Decrypt message using DES """
    message = input("Podaj wiadomość: ")
    message = bytes(message, encoding='utf-8')

    key = input("Podaj klucz: \n")
    key = fill_to_block(key, 8)
    key = key.encode('utf-8')
    key = DesKey(key)

    starttime = timeit.default_timer()
    encrypted_message = encrypt_by_des(message, key)
    print("Czas szyfrowania używając DES: ", timeit.default_timer() - starttime, "s")

    starttime = timeit.default_timer()
    decrypted_message = decrypt_des(encrypted_message, key)
    print("Czas odszyfrowania DES: ", timeit.default_timer() - starttime, "s")

    print("Zaszyfrowany tekst: ", encrypted_message)
    print("Odszyfrowany tekst: ", decrypted_message.decode("ISO-8859-1").rstrip('\0'))


if __name__ == "__main__":
    main()
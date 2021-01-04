"""
Szyfrowanie tekstu przy pomocy algorytmu RSA.

Autor: Michał Degowski
Źródło algorytmu szyfrującego: https://pypi.org/project/rsa/
"""

import rsa
import timeit

def encrypt_RSA(message, pub):
    """ Encrypting message using RSA in CBC Mode """
    return rsa.encrypt(message, pub)

def decrypt_RSA(message, priv):
    """ Decrypting message using RSA in CBC Mode """
    return rsa.decrypt(message, priv)

def main():
    """ Crypt&Decrypt message using RSA """
    message = input("Podaj wiadomość: ")
    message = bytes(message, encoding='utf-8')

    (pub, priv) = rsa.newkeys(512)

    starttime = timeit.default_timer()
    encrypted_message = encrypt_RSA(message, pub)
    print("Czas szyfrowania używając RSA: ", timeit.default_timer() - starttime, "s")

    starttime = timeit.default_timer()
    decrypted_message = decrypt_RSA(encrypted_message, priv)
    print("Czas odszyfrowania RSA: ", timeit.default_timer() - starttime, "s")

    print("Zaszyfrowany tekst: ", encrypted_message)
    print("Odszyfrowany tekst: ", decrypted_message.decode('utf8'))


if __name__ == "__main__":
    main()

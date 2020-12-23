"""
Szyfrowanie tekstu przy pomocy algorytmu RSA.

Autor: Michał Degowski
Źródło algorytmu szyfrującego: https://pypi.org/project/rsa/
"""

import rsa

def encrypt_RSA(message, pub):
    """ Encrypting message using RSA Mode """
    return rsa.encrypt(message, pub)

def decrypt_RSA(message, priv):
    """ Decrypting message and removing padding from message """
    return rsa.decrypt(message, priv)

def main():
    """ Crypt&Decrypt message using RSA """
    message = input("Podaj wiadomość: ")
    message = bytes(message, encoding='utf-8')

    (pub, priv) = rsa.newkeys(512)

    encrypted_message = encrypt_RSA(message, pub)
    decrypted_message = decrypt_RSA(encrypted_message, priv)

    print("Zaszyfrowany tekst: ", encrypted_message)
    print("Odszyfrowany tekst: ", decrypted_message.decode('utf8'))


if __name__ == "__main__":
    main()

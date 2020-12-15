"""
Szyfrowanie tekstu przy pomocy algorytmu DES.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/des/
"""

from des import DesKey


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

    # Key written using bytes in Python3
    key = DesKey(b"some key")

    encrypted_message = encrypt_by_des(message, key)
    decrypted_message = decrypt_des(encrypted_message, key)

    print("Zaszyfrowany tekst: ", encrypted_message)
    print("Odszyfrowany tekst: ", decrypted_message.decode("ISO-8859-1").rstrip('\0'))


if __name__ == "__main__":
    main()
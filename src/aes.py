"""
Szyfrowanie tekstu przy pomocy algorytmu AES.

Autor: Michał Degowski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""

from Crypto.Cipher import AES
from utils.pad import pad, unpad
import base64
# functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data

def aes_encode(message, key):
    """ Encrypting message using AES in CBC Mode """
    key = bytes(key, encoding='utf8')
    iv = "mm88!@#$%^dsmdms"
    iv = bytes(iv, encoding='utf8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    AES_code = bytes(pad(message), encoding='utf8')
    code = cipher.encrypt(AES_code)
    encrypted_text = str((base64.encodebytes(code)).decode())
    return encrypted_text


def aes_decode(message, key):
    """ Decrypting message and removing padding from message """
    key = bytes(key, encoding='utf8')
    iv = "mm88!@#$%^dsmdms"
    iv = bytes(iv, encoding='utf8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = base64.b64decode(message.encode())
    decrypted_text = cipher.decrypt(message).decode()
    decrypted_code = decrypted_text.rstrip('\0')
    return unpad(decrypted_code)

def main():
    """ Crypt&Decrypt message using AES """
    message = input("Podaj wiadomość: \n")
    secret_key = input("Podaj klucz (musi być 16 znaków!): \n")
    encrypted_text = aes_encode(message, secret_key)
    print('Zaszyfrowany tekst: ', encrypted_text)
    print('Odszyfrowany tekst: ', aes_decode(encrypted_text, secret_key))


if __name__ == "__main__":
    main()
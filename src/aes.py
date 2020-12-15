"""
Szyfrowanie tekstu przy pomocy algorytmu AES.

Autor: Michał Degowski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""

from Crypto.Cipher import AES
import base64
# functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data


def aes_encode(text, key, iv):
    key = bytes(key, encoding='utf8')
    # print(key) = "tdqsgf8888!@#$%^"
    iv = bytes(iv, encoding='utf8')
    # print(key) = "tdqsgf8888!@#$%^"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    PADDING = '\0'
    pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
    AES_code = bytes(pad_it(text), encoding='utf8')
    code = cipher.encrypt(AES_code)
    base64_text = str((base64.encodebytes(code)).decode()).replace('\n', '')
    return base64_text


def aes_decode(text, key, iv):
    key = bytes(key, encoding='utf8')
    # print(key) = "tdqsgf8888!@#$%^"
    iv = bytes(iv, encoding='utf8')
    # print(key) = "tdqsgf8888!@#$%^"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    textb = base64.b64decode(text.encode('utf-8'))
    decrypted_text = cipher.decrypt(textb).decode('utf-8')
    decrypted_code = decrypted_text.rstrip('\0')
    return decrypted_code


def main():
    message = input("Podaj wiadomość: ")
    secret_key = "tdqsgf8888!@#$%^"
    iv = "tdqsgf8888!@#$%^"
    encrypted_text = aes_encode(message, secret_key, iv)
    print('Zaszyfrowany tekst: ', encrypted_text)
    print('Odszyfrowany tekst: ', aes_decode(encrypted_text, secret_key, iv))


if __name__ == "__main__":
    main()

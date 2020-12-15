"""
Szyfrowanie tekstu przy pomocy algorytmu AES.

Autor: Michał Degowski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""

from Crypto.Cipher import AES
import base64
# functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data

def aes_encode(message, key, iv):
    key = bytes(key, encoding='utf8')
    iv = bytes(iv, encoding='utf8')
    # print(iv) = "mm88!@#$%^dsmdms"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pad = lambda s: s + (16 - len(s) % 16) * '\0'
    AES_code = bytes(pad(message), encoding='utf8')
    code = cipher.encrypt(AES_code)
    encrypted_text = str((base64.encodebytes(code)).decode())
    return encrypted_text


def aes_decode(message, key, iv):
    key = bytes(key, encoding='utf8')
    iv = bytes(iv, encoding='utf8')
    # print(iv) = "mm88!@#$%^dsmdms"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = base64.b64decode(message.encode())
    decrypted_text = cipher.decrypt(message).decode()
    decrypted_code = decrypted_text.rstrip('\0')
    return decrypted_code

def main():
    message = input("Podaj wiadomość: \n")
    secret_key = input("Podaj klucz (musi być 16 znaków!): \n")
    iv = "mm88!@#$%^dsmdms"
    encrypted_text = aes_encode(message, secret_key, iv)
    print('Zaszyfrowany tekst: ', encrypted_text)
    print('Odszyfrowany tekst: ', aes_decode(encrypted_text, secret_key, iv))


if __name__ == "__main__":
    main()
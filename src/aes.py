"""
Szyfrowanie tekstu przy pomocy algorytmu AES.

Autor: Michał Degowski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""

from os import urandom
from Crypto.Cipher import AES
def aes():
    # Do generowania zaszyfrowanego tekstu
    secret_key = urandom(16)
    iv = urandom(16)
    obj = AES.new(secret_key, AES.MODE_CBC, iv)

    # Szyfracja wiadomości (musi mieć 16 znaków)
    message = b'Szyfrowanie__AES'
    print('Oryginalna wiadomość : ', message)
    encrypted_text = obj.encrypt(message)
    print('Zaszyfrowany tekst: ', encrypted_text)

    # Deszyfracja wiadomości
    rev_obj = AES.new(secret_key, AES.MODE_CBC, iv)
    decrypted_text = rev_obj.decrypt(encrypted_text)
    print('Odszyfrowany tekst: ', decrypted_text.decode('utf-8'))
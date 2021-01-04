"""
Szyfrowanie tekstu przy pomocy algorytmu ElGamal.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://github.com/RyanRiddle/elgamal
"""


import src.elgamal_library as elgamal
import timeit


def main():
    """ Crypt&Decrypt message using ElGamal """
    message = input("Podaj wiadomość: ")
    keys = elgamal.generate_keys()
    priv = keys['privateKey']
    pub = keys['publicKey']

    starttime = timeit.default_timer()
    cipher = elgamal.encrypt(pub, message)
    print("Czas szyfrowania używając metody ElGamal: ", timeit.default_timer() - starttime, "s")

    starttime = timeit.default_timer()
    plain = elgamal.decrypt(priv, cipher)
    print("Czas odszyfrowywania dla ElGamal: ", timeit.default_timer() - starttime, "s")

    print("Zaszyfrowany tekst: ", cipher)
    print("Odszyfrowany tekst: ", plain)


if __name__ == "__main__":
    main()
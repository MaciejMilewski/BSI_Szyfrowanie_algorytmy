"""
Przykład zastosowania saltingu.

Autor: Maciej Milewski
Źródło: https://pypi.org/project/bcrypt/
"""


import bcrypt


def check_key(plain_text_key, hashed_key):
    """ Compare real key with another one """
    return bcrypt.checkpw(plain_text_key, hashed_key)


def main():
    """ Example of using hash with salt to store secret key """
    secret_key = input("Podaj klucz do szyfru: ")
    secret_key = bcrypt.hashpw(secret_key, bcrypt.gensalt( 10 ))
    print("Klucz po użyciu hash + salting: ", secret_key)
    new_key = input("Podaj klucz do porównania: ")
    if check_key(new_key, secret_key):
        print("Klucze są identyczne.")
    else:
        print("Klucze nie są identyczne.")


if __name__ == "__main__":
    main()
"""
Szyfrowanie tekstu korzystające z ECC.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""


from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii
import timeit
import os


def encrypt_AES_GCM(msg, secretKey):
    """ encrypt AES in GCM mode """
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)


def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
    """ decrypt AES in GCM mode """
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


def ecc_point_to_256_bit_key(point):
    """ setting generator point for elliptic curve """
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()


def encrypt_ECC(msg, pubKey, curve):
    """ Encryption using ECC with 256 bit key and GCM mode to chain cipher blocks """
    ciphertextPrivKey = secrets.randbelow(curve.field.n)
    sharedECCKey = ciphertextPrivKey * pubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    ciphertext, nonce, authTag = encrypt_AES_GCM(msg, secretKey)
    ciphertextPubKey = ciphertextPrivKey * curve.g
    return (ciphertext, nonce, authTag, ciphertextPubKey)


def decrypt_ECC(encryptedMsg, privKey):
    """ ECC decryption """
    (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
    sharedECCKey = privKey * ciphertextPubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
    return plaintext


def main():
    """ Crypt&Decrypt message using ECC & AES """
    curve = registry.get_curve('brainpoolP256r1')
    msg = input("Podaj wiadomość: ")
    msg = msg.encode('utf-8')
    print("Oryginalna wiadomość:", msg.decode("ISO-8859-1").rstrip('\0'))

    privKey = secrets.randbelow(curve.field.n)
    pubKey = privKey * curve.g

    starttime = timeit.default_timer()
    encryptedMsg = encrypt_ECC(msg, pubKey, curve)
    encryptedMsgObj = {
        'ciphertext': binascii.hexlify(encryptedMsg[0]),
        'nonce': binascii.hexlify(encryptedMsg[1]),
        'authTag': binascii.hexlify(encryptedMsg[2]),
        'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
    }
    print("Czas szyfrowania używając ECC: ", timeit.default_timer() - starttime, "s")

    starttime = timeit.default_timer()
    decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
    print("Czas odszyfrowania ECC: ", timeit.default_timer() - starttime, "s")

    print("Zaszyfrowana wiadomość:", encryptedMsgObj)
    print("Odszyfrowana wiadomość:", decryptedMsg.decode("ISO-8859-1").rstrip('\0'))


if __name__ == "__main__":
    main()
import os
import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# AES KEY
AES_KEY = os.urandom(32)


# AES Encrypt
def aes_encrypt(message):

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(AES_KEY), modes.CFB(iv))

    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()

    return iv + ciphertext


# AES Decrypt
def aes_decrypt(ciphertext):

    iv = ciphertext[:16]
    actual_cipher = ciphertext[16:]

    cipher = Cipher(algorithms.AES(AES_KEY), modes.CFB(iv))

    decryptor = cipher.decryptor()

    return decryptor.update(actual_cipher).decode()


# RSA Keys
(publicKey, privateKey) = rsa.newkeys(2048)


# RSA Encrypt
def rsa_encrypt(message):

    return rsa.encrypt(message.encode(), publicKey)


# RSA Decrypt
def rsa_decrypt(cipher):

    return rsa.decrypt(cipher, privateKey).decode()

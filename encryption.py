from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# 256-bit AES key
key = os.urandom(32)

def encrypt(message):

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()

    return iv + ciphertext


def decrypt(ciphertext):

    iv = ciphertext[:16]
    actual_cipher = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()

    return decryptor.update(actual_cipher).decode()
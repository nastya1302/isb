import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricAlgorithm:
    """
    Implementation of a class for a symmetric encryption algorithm.
    """

    @staticmethod
    def generates_symmetric_key(lenght_key: int) -> bytes:
        key = os.urandom(lenght_key)
        return key
    
    @staticmethod
    def encrypts_text(key: bytes, text: str) -> bytes:
        padder = padding.ANSIX923(128).padder()
        text = bytes(text, 'UTF-8')
        padded_text = padder.update(text)+padder.finalize()
        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return c_text

    @staticmethod
    def decrypts_text(key: bytes, text: bytes) -> str:
        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        unpadder = padding.ANSIX923(128).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        return unpadded_dc_text
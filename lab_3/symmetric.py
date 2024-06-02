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
    def encrypts_text(key: bytes, sourse_text: str) -> bytes:
        padder = padding.PKCS7(128).padder()
        text = bytes(sourse_text, 'UTF-8')
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
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        final_text = unpadded_dc_text.decode('UTF-8', errors='ignore')
        return final_text
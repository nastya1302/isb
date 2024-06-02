import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricAlgorithm:
    """
    Implementation of a class for a symmetric encryption algorithm.
    """

    @staticmethod
    def generates_symmetric_key(lenght_key: int) -> bytes:
        """
        The method generates a key for a symmetric encryption algorithm.
        """
        key: bytes = os.urandom(lenght_key)
        return key

    @staticmethod
    def encrypts_text(key: bytes, sourse_text: str) -> bytes:
        """
        Encrypt the text using a symmetric algorithm.
        """
        padder = padding.PKCS7(64).padder()
        text: bytes = bytes(sourse_text, "UTF-8")
        padded_text: bytes = padder.update(text) + padder.finalize()
        iv: bytes = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text: bytes = iv + encryptor.update(padded_text) + encryptor.finalize()
        return c_text

    @staticmethod
    def decrypts_text(key: bytes, text: bytes) -> str:
        """
        Decrypt the text using a symmetric algorithm.
        """
        iv: bytes = text[:8]
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        text: bytes = text[8:]
        dc_text: bytes = decryptor.update(text) + decryptor.finalize()
        unpadder = padding.PKCS7(64).unpadder()
        unpadded_dc_text: bytes = unpadder.update(dc_text) + unpadder.finalize()
        text: str = unpadded_dc_text.decode("UTF-8", errors="ignore")
        return text
 
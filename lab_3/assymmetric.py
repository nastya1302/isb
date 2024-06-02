from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class AssymmetricAlgorithm:
    """
    A class for working with asymmetric cryptography.
    """

    @staticmethod
    def generates_assymmetric_key() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generate keys for an asymmetric algorithm.
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()
        return public_key, private_key

    @staticmethod
    def encrypts_key(public_key: rsa.RSAPublicKey, symmetric_key: bytes) -> bytes:
        """
        Encrypt the symmetric encryption key with a public key.
        """
        encrypt_symmetric_key: bytes = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return encrypt_symmetric_key

    @staticmethod
    def decrypts_key(private_key: rsa.RSAPrivateKey, encrypt_symmetric_key: bytes) -> bytes:
        """
        Decrypt a symmetric key with a private key.
        """
        decrypt_symmetric_key: bytes = private_key.decrypt(
            encrypt_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return decrypt_symmetric_key
 
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class AssymmetricAlgorithm:
    @staticmethod
    def generates_assymmetric_key() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return public_key, private_key
    
    @staticmethod
    def encrypts_key(public_key: rsa.RSAPublicKey, symmetric_key: bytes) -> bytes:
        encrypt_symmetric_key = public_key.encrypt(
            symmetric_key, 
            padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()), algorithm = hashes.SHA256(), label = None))
        return encrypt_symmetric_key
    
    @staticmethod
    def decrypts_key(private_key: rsa.RSAPrivateKey, encrypt_symmetric_key: bytes) -> bytes:
        decrypt_symmetric_key = private_key.decrypt(
            encrypt_symmetric_key,
            padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()), algorithm = hashes.SHA256(),label = None))
        return decrypt_symmetric_key
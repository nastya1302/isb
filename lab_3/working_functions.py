import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa


def read_file(path: str) -> str:
    """
    A function for reading a file. accepts a path as input, returns a string.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        return text
    except FileNotFoundError as e:
        print(e)


def write_file(path: str, text: str) -> None:
    """
    A function for writing to a file using a specified path.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(e)


def read_json(path: str) -> dict:
    """
    A function for reading a .json file. accepts a path as input, returns a dictionary.
    """
    try:
        with open(path, "r", encoding="UTF-8") as f:
            text = json.load(f)
        return text
    except FileNotFoundError as e:
        print(e)


def read_file_bytes(path: str) -> bytes:
    """ """
    try:
        with open(path, mode="rb") as f:
            text = f.read()
        return text
    except FileNotFoundError as e:
        print(e)


def write_file_bytes(path: str, text: bytes) -> None:
    """ """
    try:
        with open(path, "wb") as f:
            f.write(text)
    except Exception as e:
        print(e)

def read_public_key(path: str) -> rsa.RSAPublicKey:
    """ """
    try:
        with open(path, 'rb') as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
        return d_public_key
    except FileNotFoundError as e:
        print(e)


def write_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
    """ """
    try:
        with open(path, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as e:
        print(e)


def read_private_key(path: str) -> rsa.RSAPrivateKey:
    """ """
    try:
        with open(path, 'rb') as pem_in:
            private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(private_bytes,password=None,)
        return d_private_key
    except FileNotFoundError as e:
        print(e)


def write_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
    """ """
    try:
        with open(path, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))
    except Exception as e:
        print(e)
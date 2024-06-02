from working_functions import *
from const import PATH
from symmetric import SymmetricAlgorithm
from assymmetric import AssymmetricAlgorithm
import warnings
from cryptography.utils import CryptographyDeprecationWarning



def main() -> None:
    warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
    paths: dict = read_json(PATH)
    write_file_bytes(paths["symmetric_key"], SymmetricAlgorithm.generates_symmetric_key(16))
    write_file_bytes(paths["encrypted_file"], SymmetricAlgorithm.encrypts_text(read_file_bytes(paths["symmetric_key"]), read_file(paths["initial_file"])))
    keys = AssymmetricAlgorithm.generates_assymmetric_key()
    write_public_key(paths["public_key"], keys[0])
    write_private_key(paths["private_key"], keys[1])
    write_file_bytes(paths["encrypted_symmetric_key"], AssymmetricAlgorithm.encrypts_key(keys[0], read_file_bytes(paths["symmetric_key"])))
    write_file_bytes(paths["decrypted_symmetric_key"], AssymmetricAlgorithm.decrypts_key(keys[1], read_file_bytes(paths["encrypted_symmetric_key"])))
    write_file(paths["decrypted_file"], SymmetricAlgorithm.decrypts_text(read_file_bytes(paths["decrypted_symmetric_key"]), read_file_bytes(paths["encrypted_file"])))



if __name__ == "__main__":
    main()
 
import argparse

from working_functions import WorkingWithFiles
from symmetric import SymmetricAlgorithm
from assymmetric import AssymmetricAlgorithm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-set", "--settings", type=str, help="File with paths.")
    parser.add_argument(
        "-s", "--size", type=int, help="The size of the encryption key."
    )
    parser.add_argument(
        "-gen_sym",
        "--generating_symmetric",
        help="Generating a key for a symmetric algorithm and saving it along the specified path.",
    )
    parser.add_argument(
        "-gen_asym",
        "--generating_asymmetric",
        help="Generating keys for a asymmetric algorithm and saving it along the specified path.",
    )
    parser.add_argument(
        "-enc_sym",
        "--encrypt_sym",
        help="Encrypt the symmetric encryption key with the public key and save it in the specified path.",
    )
    parser.add_argument(
        "-dec_sym",
        "--decrypt_sym",
        help="Decrypt the symmetric encryption key with the private key and save it in the specified path.",
    )
    parser.add_argument(
        "-enc",
        "--encryption",
        help="Encryption of text by key for symmetric encryption.",
    )
    parser.add_argument(
        "-dec",
        "--decryption",
        help="Decryption of text by key for symmetric encryption.",
    )

    args = parser.parse_args()
    paths = WorkingWithFiles.read_json(args.settings)
    size_key: int = args.size
    symmetric = SymmetricAlgorithm()
    asymmetric = AssymmetricAlgorithm()

    match args:
        case args if args.generation_symmetric:
            WorkingWithFiles.write_file_bytes(
                paths["symmetric_key"], symmetric.generates_symmetric_key(size_key)
            )
        case args if args.generation_asymmetric:
            keys = asymmetric.generates_assymmetric_key()
            WorkingWithFiles.write_public_key(paths["public_key"], keys[0])
            WorkingWithFiles.write_private_key(paths["private_key"], keys[1])
        case args if args.encryption:
            WorkingWithFiles.write_file_bytes(
                paths["encrypted_file"],
                symmetric.encrypts_text(
                    WorkingWithFiles.read_file_bytes(paths["symmetric_key"]),
                    WorkingWithFiles.read_file(paths["initial_file"]),
                ),
            )
        case args if args.decryption:
            WorkingWithFiles.write_file(
                paths["decrypted_file"],
                SymmetricAlgorithm.decrypts_text(
                    WorkingWithFiles.read_file_bytes(paths["decrypted_symmetric_key"]),
                    WorkingWithFiles.read_file_bytes(paths["encrypted_file"]),
                ),
            )
        case args if args.encrypt_sym:
            WorkingWithFiles.write_file_bytes(
                paths["encrypted_symmetric_key"],
                asymmetric.encrypts_key(
                    WorkingWithFiles.read_file_bytes["public_key"],
                    WorkingWithFiles.read_file_bytes(paths["symmetric_key"]),
                ),
            )
        case args if args.decrypt_sym:
            WorkingWithFiles.write_file_bytes(
                paths["decrypted_symmetric_key"],
                asymmetric.decrypts_key(
                    WorkingWithFiles.read_file_bytes["private_key"],
                    WorkingWithFiles.read_file_bytes(paths["symmetric_key"]),
                ),
            )


if __name__ == "__main__":
    main()
 
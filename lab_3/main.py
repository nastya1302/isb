from working_functions import *
from const import PATH
from symmetric import SymmetricAlgorithm


def main() -> None:
    paths: dict = read_json(PATH)
    write_file_bytes(paths["symmetric_key"], SymmetricAlgorithm.generates_symmetric_key(16))


if __name__ == "main":
    main()
 
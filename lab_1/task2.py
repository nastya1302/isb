from working_functions import *
from paths import path


def decryption(path_sourse_text: str, path_key: str, path_encrypted_text: str) -> None:
    text: str = read_file(path_encrypted_text)
    with open("C:/Users/nasty/isb/lab_1/task2_key.json", 'r', encoding='UTF-8') as f:
        key = json.load(f)
    key: dict = read_json(path_key)
    new_text: str = ''
    for letter in text:
        if letter in key:
            new_text += key[letter]
    write_file(path_sourse_text, new_text)


def main() -> None:
    paths: dict = read_json(path)
    decryption(paths["task2_sourse_text"], paths["task2_key"], paths["task2_encrypted_text"])


if __name__ == "__main__":
    main()
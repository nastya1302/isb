import json


def read_file(path: str) -> str:
    """
    A function for reading a file. accepts a path as input, returns a string.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def write_file(path: str, text: str) -> None:
    """
    A function for writing to a file using a specified path.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_json(path: str) -> dict:
    """
    A function for reading a .json file. accepts a path as input, returns a dictionary.
    """
    with open(path, "r", encoding="UTF-8") as f:
        text = json.load(f)
    return text

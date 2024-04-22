import json


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def write_file(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='UTF-8') as f:
        text = json.load(f)
    return text    
alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def create_dict() -> dict:
    dict_alphabet: dict = {}
    i: int = 0
    for letter in alphabet:
        dict_alphabet[letter] = i
        i += 1    
    return dict_alphabet


def create_vigenere_ciphe() -> dict:
    list_letter = list(alphabet)
    list_line = {}
    for i in range(32):
        list_line[i] = list_letter[i:i+32:1] + list_letter[0:i]
    return list_line


def create_shifr() -> None:
    with open("C:/Users/nasty/isb/lab_1/task1_sourse_text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    with open("C:/Users/nasty/isb/lab_1/task1_key.txt", "r", encoding="utf-8") as f:
        key = f.read()
    text = "".join(text.split())
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    dict_alphabet = create_dict()
    table = create_vigenere_ciphe()
    new_text = ''
    for k, t in zip(key, text):
        new_text += table[dict_alphabet[k]][dict_alphabet[t]]
    with open("C:/Users/nasty/isb/lab_1/task1_encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(new_text)


create_shifr()
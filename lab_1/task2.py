import json


def decryption():
    with open("C:/Users/nasty/isb/lab_1/task2_encrypted_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
    with open("C:/Users/nasty/isb/lab_1/task2_key.json", 'r', encoding='UTF-8') as f:
        key = json.load(f)
    new_text = ''
    for letter in text:
        if letter in key:
            new_text += key[letter]
    with open("C:/Users/nasty/isb/lab_1/task2_sourse_text.txt", "w", encoding='UTF-8') as f:
        f.write(new_text)


decryption()
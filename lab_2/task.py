from math import sqrt, erfc
from scipy.special import gammainc

from const import PI


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


def frequency_bitwise_test(path: str) -> float:
    sequence: str = read_file(path)
    summa: int = 0
    for count in sequence:
        if count == "1":
            summa += 1
        else:
            summa += -1
    summa = abs(summa)/sqrt(len(sequence))
    p_value: float = erfc(summa/sqrt(2))
    return p_value


def test_for_same_consecutive_bits(path: str) -> float:
    sequence: str = read_file(path)
    percentage_of_units: float = sequence.count("1")/len(sequence)
    p_value: float = 0 
    if not abs(percentage_of_units - 0.5) < (2 / sqrt(len(sequence))):
        p_value = 0
    else:
        v_n: int = 0
        for i in range(len(sequence) - 1):
            if not (sequence[i] == sequence[i + 1]):
                v_n += 1
        p_value = erfc(abs(v_n - 2 * len(sequence) * percentage_of_units * (1 - percentage_of_units)) / 
                            (2 * sqrt(2 * len(sequence)) * percentage_of_units * (1 - percentage_of_units)))
    return p_value


def longest_sequence_test(path: str) -> float:
    sequence: str = read_file(path)
    blocks_sequence = [sequence[i:i + 8] for i in range(0, len(sequence), 8)]
    list_lenght: list = []
    for block_sequence in blocks_sequence:
        list_lenght.append(len(max(block_sequence.split('0'), key = len)))
    v1 = list_lenght.count(1) + list_lenght.count(0)
    v2 = list_lenght.count(2)
    v3 = list_lenght.count(3)
    v4 = len(list_lenght) - (v1 + v2 + v3)
    v = [v1, v2, v3, v4]
    x: float = 0
    for v_i, pi_i in zip(v, PI):
        x += ((v_i - 16 * pi_i) * (v_i - 16 * pi_i)) / (16 * pi_i)
    p_value: float = gammainc(3 / 2, x / 2)
    return p_value


def main() -> None:
    #res1: float = frequency_bitwise_test("C:/Users/nasty/isb/lab_2/sequence_c.txt")
    #res2: float = test_for_same_consecutive_bits("C:/Users/nasty/isb/lab_2/sequence_c.txt")
    res = longest_sequence_test("C:/Users/nasty/isb/lab_2/sequence_c.txt")
    print(res)
    #print(res1)
    #print(res2)


if __name__ == "__main__":
    main()
 
from math import sqrt, erfc
from scipy.special import gammainc

import const


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


def frequency_bitwise_test(sequence: str) -> float:
    """
    The frequency bitwise test finds the value
    of P_value to check the sequence for randomness.
    """
    summa: float = abs(sequence.count("1") - sequence.count("0")) / sqrt(len(sequence))
    p_value: float = erfc(summa / sqrt(2))
    return p_value


def test_for_same_consecutive_bits(sequence: str) -> float:
    """
    The test determines how often the 1 and 0
    changes occur to establish the randomness of the sequence.
    """
    percentage_of_units: float = sequence.count("1") / len(sequence)
    p_value: float = 0
    if not abs(percentage_of_units - 0.5) < (2 / sqrt(len(sequence))):
        p_value = 0
    else:
        v_n: int = 0
        for i in range(len(sequence) - 1):
            if not (sequence[i] == sequence[i + 1]):
                v_n += 1
        p_value = erfc(abs(v_n - 2 * len(sequence) * percentage_of_units * (1 - percentage_of_units))
            / (2 * sqrt(2 * len(sequence)) * percentage_of_units * (1 - percentage_of_units)))
    return p_value


def longest_sequence_test(sequence: str) -> float:
    """
    The test searches for the longest sequence of units, its evaluation
    takes place, which is compared with a similar evaluation for a reference random sequence.
    """
    blocks_sequence = [sequence[i : i + 8] for i in range(0, len(sequence), 8)]
    list_lenght: list = []
    for block_sequence in blocks_sequence:
        list_lenght.append(len(max(block_sequence.split("0"), key=len)))
    v: list = []
    v.append(list_lenght.count(1) + list_lenght.count(0))
    v.append(list_lenght.count(2))
    v.append(list_lenght.count(3))
    v.append(len(list_lenght) - (v[0] + v[1] + v[2]))
    x: float = 0
    for v_i, pi_i in zip(v, const.PI):
        x += ((v_i - 16 * pi_i) * (v_i - 16 * pi_i)) / (16 * pi_i)
    p_value: float = gammainc(3 / 2, x / 2)
    return p_value


def main() -> None:
    sequence: str = read_file(const.PATH_J)
    res1: float = frequency_bitwise_test(sequence)
    res2: float = test_for_same_consecutive_bits(sequence)
    res3: float = longest_sequence_test(sequence)
    print(res1)
    print(res2)
    print(res3)


if __name__ == "__main__":
    main()

from math import sqrt, erfc


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
    return erfc(summa/sqrt(2))


def test_for_same_consecutive_bits(path: str) -> float:
    sequence: str = read_file(path)
    percentage_of_units: float = sequence.count("1")/len(sequence)
    if not abs(percentage_of_units - 0.5) < (2 / sqrt(len(sequence))):
        return 0
    else:
        v_n: int = 0
        for i in range(len(sequence) - 1):
            if not (sequence[i] == sequence[i + 1]):
                v_n += 1
        p_value: float = erfc(abs(v_n - 2 * len(sequence) * percentage_of_units * (1 - percentage_of_units)) / 
                            (2 * sqrt(2 * len(sequence)) * percentage_of_units * (1 - percentage_of_units)))
        return p_value


def main() -> None:
    res1: float = frequency_bitwise_test("C:/Users/nasty/isb/lab_2/sequence_c.txt")
    res2: float = test_for_same_consecutive_bits("C:/Users/nasty/isb/lab_2/sequence_c.txt")
    print(res1)
    print(res2)


if __name__ == "__main__":
    main()
 
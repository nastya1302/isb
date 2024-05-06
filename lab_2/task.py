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
    

def main() -> None:
    res: float = frequency_bitwise_test("C:/Users/nasty/isb/lab_2/sequence_c.txt")
    print(res)


if __name__ == "__main__":
    main()
 
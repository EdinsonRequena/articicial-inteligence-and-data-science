from typing import List


def challenge(numbers: List[int]) -> List[int]:
    even_numbers_v2 = [number for number in numbers if number % 2 == 0]
    return even_numbers_v2


def main():
    numbers = [35, 16, 10, 34, 37, 25]

    challenge(numbers)


if __name__ == '__main__':
    main()

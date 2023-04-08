from typing import List


def list_comprehensions() -> List[int]:

    numbers = []
    for element in range(1, 11):
        numbers.append(element * 2)
    print(numbers)

    numbers_v2 = [element * 2 for element in range(1, 11)]
    print(numbers_v2)

    return numbers_v2


def list_comprehensions_with_conditional() -> List[int]:

    numbers = []
    for i in range(1, 11):
            if i % 2 == 0:
                numbers.append(i * 2)
    print(numbers)

    numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
    print(numbers_v2)


def main():
    list_comprehensions()
    list_comprehensions_with_conditional()


if __name__ == '__main__':
    main()

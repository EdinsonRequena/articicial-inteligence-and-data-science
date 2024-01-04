"""
Verify if number is prime
"""

from typing import List
import random

numberListRandom: List[int] = [
    random.randint(0, 100) for number in range(0, 15)]
numberList: List[int] = [1, 3, 4, 6, 32, 6, 64, 8, 10, 2, 3, 5, 7, 11, 13, 17]


def isPrime(arr: List[int]) -> List:
    """
    Verify if number is prime
    """
    primeArr: List[int] = [number for number in arr if number % 2 != 0]

    return primeArr


def main():
    """
    Main Function
    """

    print(isPrime(numberList))


if __name__ == '__main__':

    main()

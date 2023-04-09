from typing import List, Dict
import random


def dict_comprehensions() -> Dict[int, int]:

    squares = {i: i * i for i in range(1, 11)}
    print(squares)


def dict_comprehensions_countries(countries: List[str]) -> Dict[str, int]:

    population = {country: random.randint(1, 100) for country in countries}
    print(population)


def dict_comprehensions_countries_with_if(countries: List[str]) -> Dict[str, int]:

    population = {country: random.randint(
        1, 100) for country in countries if country != 'US'}
    print(population)


def dict_comprehensions_names_ages(names: List[str], ages: List[int]) -> Dict[str, int]:

    person = {name: age for name, age in zip(names, ages)}
    # print(dict(zip(names, ages)))
    print(person)


def main():
    countries = ['VE', 'CO', 'PE', 'US']

    names = ['vicky', 'angel', 'isa', 'eddy', 'jose', 'luis', 'ian']
    ages = [random.randint(1, 35) for i in range(1, 5)]

    dict_comprehensions_names_ages(names, ages)
    dict_comprehensions_countries(countries)
    dict_comprehensions_countries_with_if(countries)
    dict_comprehensions()


if __name__ == '__main__':
    main()

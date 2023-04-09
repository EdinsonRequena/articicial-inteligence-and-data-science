from typing import Dict
import random


def population_over_50(countries_with_population: Dict[str, int]) -> Dict[str, int]:
    res = {country: population for country,
           population in countries_with_population.items() if population > 50}
    print(countries_with_population.items())
    print(res)


def challenge(text: str) -> Dict[str, int]:
    res = {l: text.count(l) for l in text if (l in 'aeiou')}
    print(res)


def main():
    countries = ['VE', 'CO', 'PE', 'US']

    random_text = 'this is a random teeext'

    countries_with_population = {
        country: random.randint(1, 100) for country in countries}

    population_over_50(countries_with_population)
    challenge(random_text)


if __name__ == '__main__':
    main()

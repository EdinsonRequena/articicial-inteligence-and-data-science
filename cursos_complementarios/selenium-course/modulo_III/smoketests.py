"""

Tema: Assertions y Test suites
Curso: Selenium con python.
Plataforma: Platzi.
Profesor: Hector Vega.
Alumno: @edinsonrequena.

"""

# Unittest Modules
from unittest import TestLoader, TestSuite

# Pyunirtreport Modules
from pyunitreport import HTMLTestRunner

# Our Modules
from assertions import AssertionsTest
from searchtests import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    'output': 'smoke-report'
}

if __name__ == '__main__':

    runner = HTMLTestRunner(**kwargs)
    runner.run(smoke_test)

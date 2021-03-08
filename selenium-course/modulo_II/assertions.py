"""

Tema: Assertions y Test suites
Curso: Selenium con python.
Plataforma: Platzi.
Profesor: Hector Vega.
Alumno: @edinsonrequena.

"""

# Unittest Modules
import unittest

# Selenium Modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path='/home/edinson/Descargas/geckodriver')
        driver = cls.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):

        self.assertTrue(self.is_element_present(By.NAME, 'q'))


    def test_language_option_field(self):

        self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()


    def is_element_present(self, how, what):

        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':

    unittest.main(verbosity = 2)

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

class SearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path = '/home/edinson/Descargas/geckodriver')
        driver = cls.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        #driver.implicitly_wait(15)


    def test_search_tee(self):

        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()


    def test_search_card(self):

        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('card')
        search_field.submit()

        products = driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/h2/a')
        self.assertEqual(2, len(products))


    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

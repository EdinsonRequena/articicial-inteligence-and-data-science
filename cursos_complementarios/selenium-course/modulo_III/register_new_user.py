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

class RegisterANewUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path = '/home/edinson/Descargas/geckodriver')
        driver = cls.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        #driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()
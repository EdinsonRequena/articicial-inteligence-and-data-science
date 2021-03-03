"""

Test automatizados para repuestos.
Verision: 0.2

"""

# Unitest Modules
import unittest

# Pyunitreport Modules
from pyunitreport import HTMLTestRunner

# Selenium Modules
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path = '/home/edinson/Descargas/geckodriver')
        driver = cls.driver
        driver.get('https://testrepuesto.westus.cloudapp.azure.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_empresa_button(self):

        #main_button = self.driver.find_elements_by_class_name("btn")
        main_button = self.driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[1]/a")
        main_button.click()


    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()


if __name__ == '__main__':

    unittest.main(
    verbosity = 2,
    testRunner = HTMLTestRunner(
        output = 'modulo_1/',
        report_name = 'hello-world-report',
        ))
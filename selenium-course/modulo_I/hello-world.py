import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path = '/home/edinson/Descargas/geckodriver')
        driver = cls.driver
        driver.implicitly_wait(10)


    def test_repuestos(self):

        driver = self.driver
        driver.get('https://testrepuesto.westus.cloudapp.azure.com/')


    def test_wikipedia(self):

        driver = self.driver
        driver.get('https://www.wikipedia.org/')

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
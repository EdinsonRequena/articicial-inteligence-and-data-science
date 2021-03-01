import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path = '/home/edinson/Descargas/geckodriver')
        driver = cls.driver
        driver.get('https://testrepuesto.westus.cloudapp.azure.com/')
        driver.maximize_window()
        #driver.implicitly_wait(15)


    def test_empresa_button(self):

        main_button = self.driver.find_elements_by_class_name("btn")


    def test_descargar_ya_button(self):

        descargar_button = self.driver.find_element_by_class_name('btn-outline-primary')


    def test_mas_info_button(self):

        mas_info_button = self.driver.find_element_by_id('footerModalOpen')

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
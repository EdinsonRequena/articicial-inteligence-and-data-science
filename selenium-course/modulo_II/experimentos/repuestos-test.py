"""

Test automatizados para repuestos.

"""

# Python Modules
import time

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
        #driver.implicitly_wait(15)

    def test_a_bussines_button(self):

        bussines_button = self.driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[1]/a")
        bussines_button.click()

    def test_b_login_button(self):

        login_button = self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[1]/a')
        login_button.click()

    def test_c_send_credentials(self):

        user_name = self.driver.find_element_by_id('emailLoginForm').send_keys('#')

        password = self.driver.find_element_by_id('passwordLoginForm').send_keys('#')

        login_modal_button = self.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div/div/div[2]/form/div[4]/button')
        login_modal_button.submit()

        time.sleep(20)

    def test_d_datos(self):

        datos_button = self.driver.find_element_by_xpath('/html/body/div/div/nav/ul/li[1]/a').click()

    def test_e_name_field(self):

        name_field = self.driver.find_element_by_id('name')
        name_field.clear()
        name_field.send_keys('test')

    def test_f_last_name(self):

        last_name_field = self.driver.find_element_by_id('last_name')
        last_name_field.clear()
        last_name_field.send_keys('test')

    def test_h_email_field(self):

        email_field = self.driver.find_element_by_id('email')
        email_field.clear()
        email_field.send_keys('empresa')

    def test_i_profesion_field(self):

        profesion_field = self.driver.find_element_by_id('job_title')
        profesion_field.clear()
        profesion_field.send_keys('test')

    def test_j_phone_field(self):

        phone_field = self.driver.find_element_by_id('phone_number')
        phone_field.clear()
        phone_field.send_keys('test')

    def test_k_description_field(self):

        description_field = self.driver.find_element_by_id('properties[about]')
        description_field.clear()
        description_field.send_keys('teeeeest')

    def test_z_save_button(self):

        save_button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[2]/div/button')
        save_button.click()

        time.sleep(10)


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

"""

<<<<<<< HEAD
Test automatizados para seccion mis datos.
=======
Test automatizados para repuestos.
Verision: 0.2
>>>>>>> 0338d94634a2434b689e1488ac50e30580dbde33

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

        cls.driver = webdriver.Firefox(executable_path = '/home/edinson/Escritorio/geckodriver')
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

        user_name = self.driver.find_element_by_id('emailLoginForm').send_keys('test')

        password = self.driver.find_element_by_id('passwordLoginForm').send_keys('test')

        login_modal_button = self.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div/div/div[2]/form/div[4]/button')
        login_modal_button.submit()

        time.sleep(20)

    def test_d_datos(self):

        datos_button = self.driver.find_element_by_xpath('/html/body/div/div/nav/ul/li[1]/a').click()

<<<<<<< HEAD
    def test_e_first_name_field(self):

        name_field = self.driver.find_element_by_id('name')
        name_field.clear()
        name_field.send_keys('test')

    def test_f_last_name_field(self):

        last_name_field = self.driver.find_element_by_id('last_name')
        last_name_field.clear()
        last_name_field.send_keys('test')


    def test_h_email_field(self):
=======
    def test_e_email_field(self):
>>>>>>> 0338d94634a2434b689e1488ac50e30580dbde33

        email_field = self.driver.find_element_by_id('email')
        email_field.clear()
        email_field.send_keys('empresa')

<<<<<<< HEAD
    def test_i_phone_field(self):

        phone_field = self.driver.find_element_by_id('phone_number')
        phone_field.clear()
        phone_field.send_keys('test')

    def test_j_description_field(self):

        descrtiption_field = self.driver.find_element_by_id('properties[about]')
        descrtiption_field.clear()
        descrtiption_field.send_keys('test')

    def test_z_save_button(self):
=======
    def test_f_save_button(self):
>>>>>>> 0338d94634a2434b689e1488ac50e30580dbde33

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
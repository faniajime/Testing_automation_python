import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestRegisterAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        firstnameInput = driver.find_element(By.NAME, "firstname")
        firstnameInput.send_keys("test")
        lastnameInput = driver.find_element(By.NAME, "lastname")
        lastnameInput.send_keys("account")
        emailInput = driver.find_element(By.NAME, "email")
        emailInput.send_keys("testAccpruebasucrFabiolaY Mau@gmai.com")
        passwordInput = driver.find_element(By.NAME, "password")
        passwordInput.send_keys("uX6Q4MPfUa7gKep")
        passwordConfInput = driver.find_element(By.NAME, "password_confirmation")
        passwordConfInput.send_keys("uX6Q4MPfUa7gKep")
        passwordConfInput.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("My Account Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites", driver.title)
        self.assertIn("Thank you for registering with Fake Online Clothing Store.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
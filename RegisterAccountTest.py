import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import UserAccountCreator

class TestRegisterAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register_account(self):
        username, password =  UserAccountCreator.get_random_userAccount(10)
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        firstnameInput = driver.find_element(By.NAME, "firstname")
        firstnameInput.send_keys(username)
        lastnameInput = driver.find_element(By.NAME, "lastname")
        lastnameInput.send_keys("TestLastName")
        emailInput = driver.find_element(By.NAME, "email")
        emailInput.send_keys(username + "@gmai.com")
        passwordInput = driver.find_element(By.NAME, "password")
        passwordInput.send_keys(password)
        passwordConfInput = driver.find_element(By.NAME, "password_confirmation")
        passwordConfInput.send_keys(password)
        passwordConfInput.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("My Account Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites", driver.title)
        self.assertIn("Thank you for registering with Fake Online Clothing Store.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
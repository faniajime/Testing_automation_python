import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestRegisterAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def login(self):
        

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html")
        self.assertIn("Olivia 1/4 Zip Light Jacket", driver.page_source)
        time.sleep(5)
        wishListBtn = driver.find_element(By.XPATH, "//*[@id=\"maincontent\"]/div[2]/div/div[1]/div[5]/div/a[1]/span")
        wishListBtn.click()
        time.sleep(5)
        self.assertIn("Olivia 1/4 Zip Light Jacket has been added to your Wish List.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
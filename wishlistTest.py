import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestRegisterAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
        self.driver.find_element(By.ID, "email").send_keys("pancho@gmail.com")
        self.driver.find_element(By.ID, "pass").send_keys("pkRHK4eEMgWE8TQ")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 > span").click()
  

    def test_add_to_wishlist(self):
        driver = self.driver
        self.login()
        time.sleep(5)
        self.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html")
        self.assertIn("Olivia 1/4 Zip Light Jacket", driver.page_source)
        time.sleep(5)
        wishListBtn = self.driver.find_element(By.XPATH, "//*[@id=\"maincontent\"]/div[2]/div/div[1]/div[5]/div/a[1]/span")
        wishListBtn.click()
        time.sleep(5)
        self.assertIn("Olivia 1/4 Zip Light Jacket has been added to your Wish List.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
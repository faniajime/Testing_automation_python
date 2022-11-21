import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestRegisterAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def login(self):
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
        self.driver.find_element(By.ID, "email").send_keys("pancho@gmail.com")
        self.driver.find_element(By.ID, "pass").send_keys("pkRHK4eEMgWE8TQ")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 > span").click()
  

    def test_add_to_wishlist(self):
        driver = self.driver
        self.login()
        time.sleep(2)
        self.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html")
        self.assertIn("Olivia 1/4 Zip Light Jacket", driver.page_source)
        time.sleep(2)
        wishListBtn = self.driver.find_element(By.XPATH, "//*[@id=\"maincontent\"]/div[2]/div/div[1]/div[5]/div/a[1]/span")
        wishListBtn.click()
        time.sleep(2)
        self.assertIn("Olivia 1/4 Zip Light Jacket has been added to your Wish List.", driver.page_source)

    def test_remove_from_wishlist(self):
        driver = self.driver
        self.login()
        time.sleep(2)
        self.driver.get("https://magento.softwaretestingboard.com/wishlist/")
        self.assertIn("Olivia 1/4 Zip Light Jacket", driver.page_source)
        time.sleep(2)
        product = self.driver.find_element(By.CSS_SELECTOR, ".product-item-info")
        actions = ActionChains(self.driver).move_to_element(product).perform()
        self.driver.find_element(By.LINK_TEXT, "Remove item").click()
        time.sleep(2)
        self.assertIn("Olivia 1/4 Zip Light Jacket has been removed from your Wish List.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
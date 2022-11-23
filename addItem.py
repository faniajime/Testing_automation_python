import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AddItem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_add_item(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(By.LINK_TEXT,'Gear').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Bags').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Push It').click()
        
        driver.find_element(By.ID, 'product-addtocart-button').click()
        time.sleep(5)
        self.assertIn("You added Push It Messenger Bag", driver.page_source)
        
        driver.find_element(By.LINK_TEXT,'Gear').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Watches').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Didi Sport').click()
       
        driver.find_element(By.ID, 'product-addtocart-button').click()
        time.sleep(5)
        self.assertIn("You added Didi Sport Watch", driver.page_source)
        
        
        driver.find_element(By.LINK_TEXT,'Gear').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Fitness Equipment').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Quest Lumaflex').click()
       
        driver.find_element(By.ID, 'product-addtocart-button').click()
        time.sleep(5)
        self.assertIn("You added Quest Lumaflex", driver.page_source)
       
       
       
       
    def tearDown(self):
        
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
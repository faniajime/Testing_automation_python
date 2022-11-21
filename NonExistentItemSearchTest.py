import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestNonExistentItemSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_non_existent_item_search(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        searchBar = driver.find_element(By.ID, "search")
        searchBar.send_keys("Koda")
        time.sleep(5)
        searchBar.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("Search results for: 'Koda'", driver.page_source)
        self.assertIn("Your search returned no results.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
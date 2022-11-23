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
  

    def test_compare_items(self):
        driver = self.driver
        self.login()
        self.driver.get("https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html")
        time.sleep(2)

        #Añadir primera blusa
        shirt1 = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]")
        ActionChains(self.driver).move_to_element(shirt1).perform()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[2]/a[2]").click()
        time.sleep(2)

        #Añadir segunda blusa
        shirt2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[2]")
        ActionChains(self.driver).move_to_element(shirt2).perform()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[2]/div/div/div[4]/div/div[2]/a[2]").click()
        time.sleep(2)

        #Añadir tercera blusa
        shirt3 = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[3]")
        ActionChains(self.driver).move_to_element(shirt3).perform()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[3]/div/div/div[4]/div/div[2]/a[2]").click()
        time.sleep(2) 
        
        self.driver.find_element(By.LINK_TEXT, "comparison list").click()
        time.sleep(2)
        self.assertIn("Olivia 1/4 Zip Light Jacket", driver.page_source)
        self.assertIn("Neve Studio Dance Jacket", driver.page_source)
        self.assertIn("Juno Jacket", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
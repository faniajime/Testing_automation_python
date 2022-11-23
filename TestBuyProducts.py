import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest



class TestBuyProducts(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
  
  def test_buyProducts(self):
    self.driver.get("https://magento.softwaretestingboard.com/")
    self.driver.set_window_size(972, 815)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("juanvainas@gmail.com")
    self.driver.find_element(By.ID, "pass").click()
    self.driver.find_element(By.ID, "pass").click()
    self.driver.find_element(By.ID, "pass").send_keys("asdfg123,.")
    self.driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 > span").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "ui-id-9")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#ui-id-12 > span").click()
    self.driver.find_element(By.LINK_TEXT, "Circe Hooded Ice Fleece").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "option-label-size-143-item-166").click()
    self.driver.find_element(By.ID, "option-label-color-93-item-57").click()
    self.driver.find_element(By.ID, "product-addtocart-button").click()
    time.sleep(10)
    self.driver.execute_script("window.scrollTo(0,352.79998779296875)")
    self.driver.find_element(By.CSS_SELECTOR, ".showcart").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "top-cart-btn-checkout").click()
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".button > span").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".checkout > span").click()
  
  def tearDown(self):
    self.driver.close()
  
if __name__ == "__main__":
  unittest.main()

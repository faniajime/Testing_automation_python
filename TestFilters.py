import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestFilterOptions(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_non_existent_item_search(self):
		driver = self.driver
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

		#Inicia la búsqueda del item y checkout
		self.driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > span:nth-child(2)").click()
		time.sleep(3)
		self.driver.find_element(By.LINK_TEXT, "Tops").click()
		time.sleep(3)
		self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .product-image-photo").click()
		time.sleep(3)
		self.driver.find_element(By.ID, "option-label-size-143-item-170").click()
		time.sleep(3)
		self.driver.find_element(By.ID, "option-label-color-93-item-50").click()
		time.sleep(3)
		self.driver.find_element(By.ID, "product-addtocart-button").click()
		time.sleep(3)
		self.driver.find_element(By.CSS_SELECTOR, ".showcart").click()
		time.sleep(3)
		self.driver.find_element(By.ID, "top-cart-btn-checkout").click()

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
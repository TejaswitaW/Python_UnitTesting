#Python test google search functionality
import unittest
from selenium import webdriver
import time
driver=webdriver.Chrome('chromedriver.exe')
class GoogleSearchDemo(unittest.TestCase):
    def setUp(self):
        driver.get("http://google.com")
        driver.maximize_window()
    def test(self):
        print("Test method execution")
        driver.find_element_by_name("q").send_keys("Mahesh Babu")
        time.sleep(5)
        driver.find_element_by_name('btnK').click()
        time.sleep(5)
        driver.find_element_by_class_name('LC20lb').click()
        time.sleep(10)
    def tearDown(self):
        driver.close()
unittest.main()

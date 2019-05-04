from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
class HSMLoginDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver=webdriver.Chrome("chromedriver.exe")
        driver.get("http://www.seleniumbymahesh.com/")
        driver.maximize_window()
    def test_login(self):
        driver.find_element(By.LINK_TEXT,'HMS').click()
        time.sleep(5)
        driver.find_element(By.NAME,'username').send_keys('admin')
        driver.find_element(By.NAME,'password').send_keys('admin')
        driver.find_element(By.NAME,'submit').click()
        time.sleep(10)
    def test_logout(self):
        driver.find_element(By.LINK_TEXT,'Logout').click()
        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        driver.close()
unittest.main()

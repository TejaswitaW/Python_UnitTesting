#using webdriver opened facebook page
from selenium import webdriver
driver=webdriver.Chrome('chromedriver.exe')
#this is we have created driver object
driver.get("https://www.facebook.com/")
print("Title of the URL is : ",driver.title)
print("Current page URL: ",driver.current_url)
driver.get("http://durgasoftvideos.com/")
print("Title is the URL is : ",driver.title)
print("Current page URL: ",driver.current_url)

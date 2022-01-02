from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com/")
username = driver.find_element_by_name("username")
username.send_keys("Username")

time.sleep = 3

password = driver.find_element_by_name("password")
password.send_keys("Password")

time.sleep = 3

login = driver.find_element_by_name("Log In")
login.send_keys(Key.RETURN)

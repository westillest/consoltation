from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)


def symptoms():
    print('Welcome to hospital consltation')
    print('please input your name')
    name = input()
    print('what are some of the symptoms you are having')
    signs = str(input())

#symptoms()

driver.get("https://my.clevelandclinic.org/search")
search = driver.find_element_by_id("search-input")
search.send_keys("headache")
search.send_keys(Keys.RETURN)




#search = driver.find_element_by_xpath("//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3")search.send_keys(Keys.RETURN)















from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://www.zefix.ch')
time.sleep(2)
search = driver.find_element_by_id('firm-name-fomfield')
search.send_keys("Bäckerei")
searchclick = driver.find_element_by_id('submit-search-btn')
searchclick.click()
buttons = driver.find_elements_by_class_name("icon--right")
for element in range(35):
    page = driver.page_source.encode('utf-8')
    with open('seite_' + str(element) + '.htm', 'wb+') as file:
        file.write(page)
        file.close()
    buttons[0].click()
    time.sleep(1)

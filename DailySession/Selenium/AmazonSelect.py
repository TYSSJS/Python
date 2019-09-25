import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(10)
driver.maximize_window()

Select_amazon_search=driver.find_element_by_xpath("//select[@class='nav-search-dropdown searchSelect']")
sc=Select(Select_amazon_search)
sc.select_by_index(1)
sc.select_by_value("search-alias=amazon-devices")
time.sleep(1)
sc.select_by_visible_text("Amazon Fashion")
driver.close()
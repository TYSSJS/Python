from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='text']").send_keys("python",Keys.ENTER)
print(driver.title)
driver.minimize_window()




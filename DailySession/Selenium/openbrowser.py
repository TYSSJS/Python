from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
t=driver.title
print(driver.current_url)
driver.implicitly_wait(10)
driver.maximize_window()
driver.minimize_window()
if "Amazon" in t:
    print("Title:",t)
else:
    print("invalid title")
print("current_url",driver.current_url)
# driver.find_elements_by_xpath()
driver.find_element_by_xpath("//input[@type='text']").send_keys("mobiles")
# driver.find_element(By.XPATH,"//input[@type='text']").send_keys("toys")
# above code find_element and find_element_by_xpath are same.
# driver.back()
driver.forward()
driver.back()
driver.close()

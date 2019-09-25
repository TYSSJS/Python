import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.craftsvilla.com")
driver.maximize_window()
driver.implicitly_wait(20)
saree_ele = driver.find_element_by_link_text("SAREES")

try:
    acti=ActionChains(driver)
    acti.move_to_element(saree_ele).perform()
    banarasi_sari = driver.find_element_by_xpath("//a[text()='Kanjeevaram Silk Sarees']")
    banarasi_sari.click()
except:
     print("not able to hover")
finally:
    print("This is a final block")
    driver. close()
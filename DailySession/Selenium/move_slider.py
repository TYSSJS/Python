from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(10)
frame = driver.find_element_by_class_name("demo-frame")
driver.switch_to.frame(frame)
slider = driver.find_element_by_id("slider")
try:
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider, 100, 0).perform()
    print("slider moved")
except:
    print("slider not moved")
finally:
    driver.close()

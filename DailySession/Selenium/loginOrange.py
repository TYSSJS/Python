import time
import unittest

from selenium import webdriver
class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    def test_loginlogout(self):
        driver=self.driver
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_name("Submit")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

# C:\Users\Amritha\PycharmProjects\PythonProject\framework_unittest\tests\login_test.py

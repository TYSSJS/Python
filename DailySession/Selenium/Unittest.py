import unittest
class Test_sample(unittest.TestCase):
    def setUp(self) -> None:
        print("It will run before every method ")
    def test_method1(self):
        print("In method1")
    def test_method2(self):
        print("In method2")
    def tearDown(self) -> None:
        print("It will run after every method")

if __name__ == '__main__':
    unittest.main(verbosity=2)

# It will run before every method
# In method1
# It will run after every method
# It will run before every method
# In method2
# It will run after every method
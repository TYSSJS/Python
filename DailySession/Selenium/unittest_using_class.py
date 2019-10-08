import unittest
class Test_Sample(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Run before class")

    def setUp(self) -> None:
        print("run before each method")

    def test_method1(self):
        print("This is method1")

    def test_method2(self):
        print("This is method2")

    def tearDown(self) -> None:
        print("run after each method")


    @classmethod
    def tearDownClass(cls) -> None:
        print("Run after class")


if __name__ == '__main__':
    unittest.main(verbosity=2)

# Run before class
# run before each method
# This is method1
# run after each method
# run before each method
# This is method2
# run after each method
# Run after class

import unittest
class Test_Assert(unittest.TestCase):
    def test_AssertTrue(self):
        a=True
        self.assertTrue(a,"a is not True")
        print("a is TRUE")
        b=False
        self.assertFalse(b,"b is not False")

    def test_AssertEquals(self):
        a='TYSS'
        b='TYSS'
        self.assertEquals(a,b,"a is not equal to b")
        print("a and b are equal")

    def test_AssertGreater(self):
        a=2
        b=3
        self.assertGreater(b,a,"b is greater than a")
        self.assertGreaterEqual(b,a,"b greater than or equal to a")

    # def test_AssertLess(self):
    #     a=3
    #     b=4
    #     self.assertLess(a,b,"a is less than b")
    #     self.assertLessEqual(a,b,"a is not less equal than b")

if __name__ == '__main__':
    unittest.main(verbosity=2)
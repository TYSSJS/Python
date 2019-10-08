from pySelenium.unittest_using_class import Test_Sample
from pySelenium.unittest_using_class1 import Test_Sample1
# from <package name.file name> import <class name>

import unittest
tc1=  unittest.TestLoader().loadTestsFromTestCase(Test_Sample1)
tc2= unittest.TestLoader().loadTestsFromTestCase(Test_Sample)
# variable name=unittest.TestLoader().loadTestFromTestCase(class name)
Smoke_test=unittest.TestSuite([tc1,tc2])
# while calling the test suite, which is set of test case, here tc1 and tc2
unittest.TextTestRunner(verbosity=2).run(Smoke_test)
# running the two or more testcase using testsuite is called test sweet.
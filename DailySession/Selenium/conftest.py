import pytest
@pytest.yield_fixture()
def setUp():
    print("i am fixture")
    yield
    print("run after every method")

@pytest.yield_fixture(scope="module")
# class and module can be written
def oneTimeSetup():
    print("----------------run only once before every method-----")
    yield
    print("-----run only once after every method----")

# OUTPUT
# test_TC1_demo.py::test_method1 ----------------run only once before every method-----
# i am fixture
# run after every method
# first method
# PASSED
# test_TC1_demo.py::test_method2 i am fixture
# run after every method
# 2 method
# PASSED
# test_TC1_demo.py::test_method3 i am fixture
# run after every method
# 3 method
# PASSED
# test_TC1_demo.py::test_method4 i am fixture
# run after every method
# 4 method
# PASSED
# test_TC1_demo.py::test_method5 i am fixture
# run after every method
# 5 method
# PASSED-----run only once after every method----

import pytest

@pytest.mark.run(order=3)
def test_method1(oneTimeSetup,setUp):
    print("first method")

@pytest.mark.run(order=1)
def test_method2(setUp):
    print("2 method")

@pytest.mark.run(order=2)
def test_method3(setUp):
    print("3 method")


# OUTPUT order: Method 2,3,1
# cachedir: .pytest_cache
# rootdir: C:\Users\Amritha\PycharmProjects\PythonProject\pySelenium
# plugins: ordering-0.6
# collected 3 items
#
# test_MarkOrder.py::test_method2 i am fixture
# 2 method
# PASSEDrun after every method
#
# test_MarkOrder.py::test_method3 i am fixture
# 3 method
# PASSEDrun after every method
#
# test_MarkOrder.py::test_method1 ----------------run only once before every method-----
# i am fixture
# first method
# PASSEDrun after every method
# -----run only once after every method----


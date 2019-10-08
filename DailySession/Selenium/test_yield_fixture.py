import pytest

@pytest.yield_fixture()
def setUp():
    print("i am fixture")
    yield
    print("run after every method")

def test_method1(setUp):
    print("first method")

def test_method2(setUp):
    print("second method")

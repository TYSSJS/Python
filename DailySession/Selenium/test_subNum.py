from pySelenium.mathLib import subNumber as sN
import pytest

@pytest.mark.skipif(reason="things are not proper")
def test_subNum():
    total=sN(4,1)
    assert total==4,print("this is incorrect")
    print("correct")
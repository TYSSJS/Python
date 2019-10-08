from pySelenium.mathLib import addNumber as aN
import pytest

@pytest.mark.skip("due to incorrect output")
def test_addNum():
    total=aN(1,2)
    assert total==4,print("this is incorrect")
    print("correct")
# test_addNum()
# if(total==4):
#     print("number is equal to four")
# else:
#     print("number is not equal to four")
# instead of above program use Assert

# Below output comes when we have skip method called in marker pytest
# execute from the terminal

# =================================================================================== test session starts ====================================================================================
# platform win32 -- Python 3.6.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0
# rootdir: C:\Users\Amritha\PycharmProjects\PythonProject\pySelenium
# collected 2 items
#
# test_addNum.py s                                                                                                                                                                      [ 50%]
# test_mulNum.py F                                                                                                                                                                      [100%]
#
# ========================================================================================= FAILURES =========================================================================================
# _______________________________________________________________________________________ test_mulNum ________________________________________________________________________________________
#
#     def test_mulNum():
#         mul=mN(2,2)
# >       assert mul==6,print("multiplcation is wrong")
# E       AssertionError: None
# E       assert 4 == 6
#
# test_mulNum.py:4: AssertionError
# ----------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------
# multiplcation is wrong
# =============================================================================== 1 failed, 1 skipped in 0.35s ===============================================================================


from pySelenium.mathLib import mulNumber as mN
def test_mulNum():
    mul=mN(2,2)
    assert mul==4,print("multiplcation is wrong")
    print("multiplication is correct")
# test_mulNum()

# Go to the terminal-->> and type
# Go to the path
# >>>py.test

# =================================================================================== test session starts ====================================================================================
# platform win32 -- Python 3.6.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0
# rootdir: C:\Users\Amritha\PycharmProjects\PythonProject\pySelenium
# collected 0 items / 2 errors
#
# ========================================================================================== ERRORS ==========================================================================================
# _____________________________________________________________________________ ERROR collecting test_addNum.py ______________________________________________________________________________
# test_addNum.py:8: in <module>
#     test_addNum()
# test_addNum.py:6: in test_addNum
#     assert total==4,print("this is incorrect")
# E   AssertionError: None
# E   assert 3 == 4
# ------------------------------------------------------------------------------------- Captured stdout --------------------------------------------------------------------------------------
# this is incorrect
# _____________________________________________________________________________ ERROR collecting test_mulNum.py ______________________________________________________________________________
# test_mulNum.py:6: in <module>
#     test_mulNum()
# test_mulNum.py:4: in test_mulNum
#     assert mul==6,print("multiplcation is wrong")
# E   AssertionError: None
# E   assert 4 == 6
# ------------------------------------------------------------------------------------- Captured stdout --------------------------------------------------------------------------------------
# multiplcation is wrong
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ===================================================================================== 2 error in 0.38s =====================================================================================


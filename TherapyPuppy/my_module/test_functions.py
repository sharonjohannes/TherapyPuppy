"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import mental_state, destress_level, overall_feeling
##
##


def test_mental_state():
    
    assert callable(mental_state)
    assert isinstance(mental_state(2), int)
    
def test_destress_level():
    
    assert callable(destress_level)
    assert isinstance(destress_level(9), int)
    
def test_overall_feeling():

    assert callable(overall_feeling)
    assert isinstance('happy', str)
                 
    
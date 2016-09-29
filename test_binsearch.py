
from pytest import raises
from binsearch import binary_search
import numpy as np

# What if the value is in the array
def test_in_array():
    assert binary_search(range(10), 6) == 6
    
# What if the value is not there in the array
def test_not_in_array():
    assert binary_search(range(10), 10) == -1
    
# What if it is there multiple times 
def test_multiple_times_array1():
    assert binary_search([0,1,2,3,3,3,5,6,7], 3) == 4
    
# What if it is there multiple times 
def test_multiple_times_array2():
    assert binary_search([0,1,2,3,3,3,3,3,5,6,7], 3) == 5
    
# What if the left is less than 0
def test_left_boundary():
    with raises(IndexError):
        binary_search(range(10), 3, left = -100)

# What if the right is more than the lenth of da_array
def test_right_boundary():
    with raises(IndexError):
        binary_search(range(10), 3, right = 1200)
        
# What if the right is more than the lenth of da_array
def test_rangemax():
    with raises(IndexError):
        binary_search(range(10), 3, left = 0, right = 28)

# What if the value is the same type
def test_same_type():
    assert binary_search('abcdefg', 'c') == 2
    
# What if the value is not the same type
def test_different_type():
    with raises(TypeError):
        binary_search('abcdefg', 2)
        
# What if the value is np.nan
def test_nan():
    assert binary_search([0,1,2,3,np.nan,3,5,6,7], np.nan) == 4

# What if the value is np.inf 
def test_inf():
    assert binary_search([0,1,2,3,5,7,100,np.inf], np.inf) == 7
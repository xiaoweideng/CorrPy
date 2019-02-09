## inititalization

import numpy as np
import pytest
import corrPy

single_x = [11]
single_y = [22]
zeros_x = [0,0,0,0]
pos_neg_x = [1,-2,3,-4]
pos_neg_y = [-6,7,-8,9]
large_x = [1000,-2000,3000]
large_y = [-6000,7000,-8000]
multi_x = [1,2,3,4,5]
multi_y = [6,7,8,9,10]
multi_y_plus = [6,7,8,9,10,11]
mix_type_x = [1,"2",3,4,5]
mix_type_y = [1,2,3+2j,4,5]
missing_x = [1,2,3,4,5,6,7, np.nan]
missing_y = [2,3,4,5,np.nan,1,3,4]

matrix_full = np.array(range(25), dtype=float).reshape((5, 5))
matrix_missing = np.array(range(25), dtype=float).reshape((5, 5))
matrix_missing[2,2] = np.nan

# Return Error if wrong type
def test_type():
    with pytest.raise(TypeError):
        corrPy.cov_max(single_x) # fail if only single value
        corrPy.cov_max(mix_type_x,mix_type_y) # fail if wrong type
        corrPy.cov_max(pos_neg_x,multi_x) # fail if the length not match

# Test the output shape
def test_length():
    assert corrPy.cov_max(single_x, single_y) == None # two single value return none
    assert np.shape(corrPy.cov_max(multi_x,multi_y))[0] == np.shape(corrPy.cov_max(multi_x,multi_y))[1] # the output shape should match

# Test if it can calculate the right value
def test_missing_value():
    assert corrPy.cov_max(matrix_missing) == (4,4) # using pair wise complete so the shape is deducted

# Test if it can calculate the right value
def test_value():
    assert corrPy.cov_max(matrix_full) == np.ones((5,5))*2.5 # can deal with 2D array
    assert corrPy.cov_max(matrix_missing) == np.ones((4,4))*2.5 # can deal with NA and calculates the right value
    assert corrPy.cov_max(pos_neg_x, pos_neg_y) == np.cov([1,-2,3,-4], [-6,7,-8,9]) # can deal with 2 1D array inputs
    assert corrPy.cov_max(large_x, large_y) == np.cov(large_x, large_y) # can deal with large number
    assert corrPy.cov_max(zeros_x, pos_neg_y) == np.cov(zeros_x, pos_neg_y) # can deal with zero vectors
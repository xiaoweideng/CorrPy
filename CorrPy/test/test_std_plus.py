# Test for std_plus.py
import os
import sys
sys.path.insert(0, os.path.abspath("../../CorrPy"))
import numpy as np
import pytest
import CorrPy

# create some fake variables 
one_x = [11]
char_x = [1,"2",3,4,5]
complex_x = [1,"2",3,4,5+7j]
bool_x = [True, True, False, True]
zeros_x = [0,0,0,0]
pos_neg_x = [1,-2,3,-4]
large_x = [1000,-2000,3000]
multi_x = [1,2,3,4,5,6,7]
miss_x = [1,2,3,4,5,6,7, np.nan]

def test_type():
    '''test if the input is in a valid format'''
    with pytest.raises(TypeError):
        CorrPy.std_plus(char_x) # return ERROR if input vector has a string 
        CorrPy.std_plus(complex_x) # return ERROR if input vector has a complext number
    assert np.isnan(CorrPy.std_plus(bool_x)) == False # expect a return if input vector has bool
    assert np.isnan(CorrPy.std_plus(pos_neg_x)) == False # expect a return if input vector type is numeric
        
def test_output():
    '''test if the output is in a valid format'''
    assert np.isnan(CorrPy.std_plus(multi_x)) == False
    assert np.isnan(CorrPy.std_plus(pos_neg_x)) == False

def test_value():
    '''test the correctness of the output'''
    # return zero when input has one element
    assert CorrPy.std_plus(one_x) == 0.0 
    # compute standard deviation for input of positive and negative numbers
    assert CorrPy.std_plus(pos_neg_x) == 2.692582403567252 
    # compute standard deviation for large numbers
    assert CorrPy.std_plus(large_x) == np.std(large_x) 
    # ignore the NA and compute the standard deviation for the rest of the numbers
    assert CorrPy.std_plus(miss_x) == CorrPy.std_plus(multi_x) 
    # return zero if input vector are all zeros
    assert CorrPy.std_plus(zeros_x) == 0.0

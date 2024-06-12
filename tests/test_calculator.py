'''My Calculator Test'''
from calculator import calculator

def test_addition():
    '''Test that addition function works '''    
    assert calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert calculator.subtract(2,2) == 0

def test_multiplication():
    assert calculator.multiply(2,2) == 4



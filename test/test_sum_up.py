from src.sum_up import *

def test_sum_up():
    x = 1
    y = 2
    assert sum_up(x,y) == 3

def test_sum_up3():
    assert sum_up3(1,2,3) == 6
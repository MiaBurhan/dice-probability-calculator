from Project import calculate_sum_probability, at_least_success, at_most_success

import pytest

def test_sum_ratioability():
    fraction,ratio = calculate_sum_probability(3, 3)
    assert ratio == pytest.approx(1/216)

def test_at_least_success():
  
    ratio = at_least_success(1, 1, 4, 1)
    assert ratio == pytest.approx(1/6)
    
    
    ratio = at_least_success(1, 2, 4, 1)
    assert ratio == pytest.approx(11/36)
    
    ratio= at_least_success(1, 2, 4, 2)
    assert ratio == pytest.approx(1/36)

def test_at_most_success():
    
    ratio = at_most_success(1, 1, 4, 0)
    assert ratio == pytest.approx(5/6)
    
    ratio = at_most_success(1, 2, 4, 1)
    assert ratio == pytest.approx(35/36)
    
    ratio = at_most_success(1, 2, 4, 2)
    assert ratio == pytest.approx(1)
    

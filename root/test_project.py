from dice_probability import calculate_sum_probability, at_least_success, at_most_success

import pytest

# Test of the function sum_probability for one dice
def sum_probability():
    p_once, p_atleast = calculate_sum_probability(1, 1, 3)
    assert p_once == pytest.approx(1/6)
    assert p_atleast == pytest.approx(1/6)

# Test at_least_success function
def test_at_least_success():
    # 1 die, threshold 4 (success if sum >=4, p=3/6=0.5)
    # 1 throw, at least 1 success: 0.5
    prob = at_least_success(1, 1, 4, 1)
    assert prob == pytest.approx(0.5)
    
    # 2 throws, at least 1 success: 1 - (0.5)^2 = 0.75
    prob = at_least_success(1, 2, 4, 1)
    assert prob == pytest.approx(0.75)
    
    # 2 throws, at least 2 successes: (0.5)^2 = 0.25
    prob = at_least_success(1, 2, 4, 2)
    assert prob == pytest.approx(0.25)

# Test at_most_success function  
def test_at_most_success():
    # 1 die, threshold 4, p=0.5
    # 1 throw, at most 0 successes: 0.5
    prob = at_most_success(1, 1, 4, 0)
    assert prob == pytest.approx(0.5)
    
    # 2 throws, at most 1 success: (0.5)^2 + 2*(0.5)*(0.5) = 0.25 + 0.5 = 0.75
    prob = at_most_success(1, 2, 4, 1)
    assert prob == pytest.approx(0.75)
    
    # 2 throws, at most 2 successes: 1.0
    prob = at_most_success(1, 2, 4, 2)
    assert prob == pytest.approx(1.0)
    
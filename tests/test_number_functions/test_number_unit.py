import math
import pytest

from testing.number_functions import is_even, geo_mean

def test_nf_is_even():
    assert is_even(2) == True   # Simple use case
    assert is_even(3) == False  # Simple use case

    assert is_even(-1) == False # Getting creative
    assert is_even(0) == True   # Getting creative

    # I wanna break my code!
    with pytest.warns(UserWarning, match="Got number with decimal part: 8.01"):
        assert is_even(8.01)
    
    with pytest.warns(UserWarning, match="Got number with decimal part: -8.01"):
        assert is_even(-8.01)


def test_nf_geo_mean():
    # Simple
    assert geo_mean([2, 2, 2]) == 2
    assert geo_mean([1, 2, 3]) == 1.8171

    # More stuff
    assert geo_mean([1.32892, 2.0000, 3.3333, 1]) == 1.7252
    assert geo_mean([10, math.pi]) == 5.6050

    # Hammer Time!
    with pytest.raises(TypeError): # Python will raise this
        geo_mean(1)

    with pytest.raises(TypeError, match=f"Expecting int or float, got {str}"): # I will raise this
        geo_mean(["1", "2.9802"])

    with pytest.raises(ValueError, match="Got invalid input: -2"): # I will raise this
        geo_mean([2, 2, -2])


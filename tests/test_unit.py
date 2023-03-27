import pytest

from testing.number_functions import is_even

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
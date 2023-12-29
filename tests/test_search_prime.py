import pytest

from pkg.search_prime import search_prime_num

@pytest.fixture
def test_data():
    return [1, 2, 3, 4, 5, 7,9,11]

def test_search_pime(test_data):
    result = search_prime_num(test_data)
    assert result == [3, 5, 7, 11]

def test_invalid_serach_prime(test_data):
    result = search_prime_num(test_data)
    result == [3, 5, 7, 11]



if __name__ == "__main__":
    test_search_pime([1, 2, 3, 4, 5, 7,9,11])
    # test_invalid_serach_prime([1, 2, 3, 4, 5, 7,9,11, 13])
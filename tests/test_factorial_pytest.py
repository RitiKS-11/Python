import pytest

from pkg.factorial import factorial

@pytest.fixture
def test_factorial_data():
    return 6

@pytest.mark.parametrize('number, expected_result',[
    (2, 2),
    (3, 6),
    (4, 24),
])
@pytest.mark.factorial
def test_ture_factorial(number, expected_result):
    assert factorial(number) == expected_result

@pytest.mark.parametrize('number, expected_result',[
    (1, 2),
    (7, 6),
    (4, 4),
])
@pytest.mark.factorial
def test_false_factorial(number, expected_result):
    assert factorial(number) != expected_result

@pytest.mark.factorial
def test_factorial_of_six(test_factorial_data):
    assert factorial(test_factorial_data) == 720, 'Should be 720'


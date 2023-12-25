import pytest
from pkg.req import check_connection

@pytest.fixture
def example_url():
    return 'https://www.google.com'

@pytest.mark.success
def test_connection_success(example_url):
    assert check_connection(example_url) == 'Connected', 'Should be connected'

def test_connection_failed(example_url):
    assert check_connection(example_url) == 'Not Connected', 'Should be not connected'

@pytest.mark.parametrize("URLS",[
    'https://www.google.com',
    'https://www.github.com',
    'https://www.example.com',
])
def test_connection_parametrize(URLS):
    assert check_connection(URLS) == 'Connected', 'should be connected'
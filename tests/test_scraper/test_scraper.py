import pytest
import  os

from pkg.scraper.scraper import scrape, parse_product_title, \
                    parse_content, extract_info


@pytest.fixture
def product_name():
    return 'rice'


def test_scrape():
    response = scrape('rice')
    assert response.status_code == 200


def test_parse_content(product_name):
    res = scrape(product_name)
    filename=f'{product_name}.csv'
    
    results = parse_content(res)

    assert  len(results) != 0
    assert results[0]['name'] != ''


def test_incorrect_parse_content(product_name):
    res = scrape(product_name)
    product_list = parse_content(res)
    excepted_result = [{'name': 'Parle Monaco Classic Regular Biscuits 150g', \
                        'price': '50.00', 'product_url': '//www.daraz.com.np'}]

    assert product_list == excepted_result


@pytest.mark.parametrize('product_title,expected_result',[
    ('Basmati Rice - 1kg', '1kg'),
    ('Ghar Ko Achar Buff Sukuti Achar - 500gm', '500gm'),
    ('Lays Spanish Tomato Tango Chips - 42g', '42g'),
    ('Sweet & Sour Mango Achar - 350gm', '350gm')
])


def test_parse_product_title(product_title, expected_result):
    assert parse_product_title(product_title) == expected_result


def test_extract_info():
    assert extract_info('rice') == True


def test_file_is_present(product_name):
    res = extract_info(product_name)

    if res:
        for filename in os.listdir():
            if filename.startswith(f'{product_name}.'):
                file = filename
    
    assert file == f'{product_name}.csv'


def test_file_contains(product_name):
    res = extract_info(product_name)

    if res:
        size = os.path.getsize(f'{product_name}.csv')

    assert size != 0


if __name__ == "__main__":
    # test_scrape('rice')
    # test_parse_content('rice')
    # test_parse_product_title('Basmati Rice 1kg')
    # test_file_is_present('rice')
    test_file_contains('fish')
    
import pytest
import  os

from pkg.scraper.scraper import scrape, parse_product_title, \
                    parse_content, extract_info, store_csv


@pytest.fixture
def product_name():
    return 'rice'


def test_scrape():
    response = scrape('rice')
    assert response.status_code == 200


def test_parse_content(product_name):
    res = scrape(product_name)    
    results = parse_content(res)

    assert  len(results) > 30 and len(results) < 50
    assert list(results[0].keys()) == list(['name', 'price', 'product_url', 'quantity'])
    assert results[0]['name'] != ''


def test_incorrect_parse_content(product_name):
    res = scrape(product_name)
    product_list = parse_content(res)
    excepted_result = [{'name': 'Parle Monaco Classic Regular Biscuits 150g', \
                        'price': '50.00', 'product_url': '//www.daraz.com.np'}]

    assert product_list != excepted_result


@pytest.mark.parametrize('product_title,expected_result',[
    ('Basmati Rice - 1kg', '1kg'),
    ('Ghar Ko Achar Buff Sukuti Achar - 500gm', '500gm'),
    ('Lays Spanish Tomato Tango Chips - 42g', '42g'),
    ('Sweet & Sour Mango Achar - 350gm', '350gm')
])


def test_parse_product_title(product_title, expected_result):
    assert parse_product_title(product_title) == expected_result


def test_extract_info(product_name):
    filepath = f'{product_name}.csv'

    if os.path.isfile(filepath):
        os.remove(filepath)

    extract_info(product_name)
    assert os.path.isfile(filepath)

    with open(filepath) as file:
        contents = file.readlines()
        file_rows = len(contents)

    assert file_rows > 40  


def test_file_is_present(product_name):
    results = [{'name': 'Parle Monaco Classic Regular Biscuits 150g', \
                        'price': '50.00', 'product_url': '//www.daraz.com.np'}]
    
    filepath = f'{product_name}.csv'
    if os.path.isfile(filepath):
        os.remove(filepath)

    store_csv(results, product_name)

    assert os.path.isfile(filepath)


def test_file_contains(product_name):
    res = extract_info(product_name)

    if res:
        filepath = f'{product_name}.csv'
        if os.path.isfile(filepath):
            os.remove(filepath)
    
        assert os.path.getsize(filepath) != 0

if __name__ == "__main__":
    # test_scrape('rice')
    # test_parse_content('rice')
    # test_parse_product_title('Basmati Rice 1kg')
    # test_file_is_present('rice')
    test_extract_info('fish')
    
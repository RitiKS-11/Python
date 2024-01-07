import pytest
import csv, os

from pkg.scraper.scraper import scrape, parse_product_title, parse_content, extract_info

def test_scrape(product_name):
    response = scrape(product_name)
    assert response.status_code == 200


def test_parse_content(product):
    filename=f'{product}.csv'
    expected_result = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expected_result.append(row)

    assert parse_content(product) == expected_result


def test_incorrect_parse_content():
    product_list = parse_content()
    excepted_result = [{'name': 'Parle Monaco Classic Regular Biscuits 150g', 'price': '50.00', 'product_url': '//www.daraz.com.np'}]

    assert product_list == excepted_result


def test_parse_product_title(product_title):
    assert parse_product_title(product_title) == '1kg'


def test_extract_info():
    assert extract_info('rice') == True


def test_file_is_present(product):
    res = extract_info(product)

    if res:
        for filename in os.listdir():
            if filename.startswith(f'{product}.'):
                file = filename
    
    assert file == f'{product}.csv'
    

def test_file_contains(product):
    res = extract_info(product)

    if res:
        size = os.path.getsize(f'{product}.csv')

    assert size != 0


if __name__ == "__main__":
    # test_scrape('rice')
    # test_parse_content('rice')
    # test_parse_product_title('Basmati Rice 1kg')
    # test_file_is_present('rice')
    test_file_contains('fish')
    
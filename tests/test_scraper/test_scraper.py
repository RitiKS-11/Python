import pytest
import csv

from pkg.scraper.scraper import scrape, parse_product_title, parse_content

def test_scrape(product_name):
    response = scrape(product_name)
    assert response.status_code == 200

def test_parse_content(product):
    filename='scrape_data_rice_2024-01-03 18:02:43.441979.csv'
    print(filename)
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

if __name__ == "__main__":
    test_scrape('rice')
    test_parse_content('rice')
    test_parse_product_title('Basmati Rice 1kg')
    
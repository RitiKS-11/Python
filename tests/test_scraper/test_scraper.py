import pytest

from pkg.scraper.scraper import connect_daraz, get_product_detail

def test_connect_daraz():
    response = connect_daraz()
    assert response.status_code == 200

def test_get_product_detail():
    product_list = get_product_detail()
    excepted_result = [{'name': 'Parle Monaco Classic Regular Biscuits 150g', 'price': '50.00', 'product_url': '//www.daraz.com.np/products/parle-monaco-classic-regular-biscuits-150g-i103662073-s1024378053.html?search=1'}]

    assert product_list == excepted_result

def test_false_get_product_detail():
    product_list = get_product_detail()
    excepted_result = [{'name': 'Parle Monaco Classic Regular Biscuits 150g', 'price': '50.00', 'product_url': '//www.daraz.com.np'}]

    assert product_list == excepted_result

if __name__ == "__main__":
    test_connect_daraz()
    test_get_product_detail()
    test_false_get_product_detail()
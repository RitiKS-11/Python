from bs4 import BeautifulSoup
import requests
import json
import csv
from datetime import datetime


def scrape(product):
    try:
        response = requests.get(f'https://www.daraz.com.np/catalog/?q={product}')
    except Exception as error:
        raise(error)

    return response


def parse_content(product):
    res = scrape(product)
    html_lines = res.text.split('window.pageData=')[1].split('</script')[0]

    products = json.loads(html_lines)['mods']['listItems']
    results = []

    with open(f'scrape_data_{product}_{datetime.today()}.csv', 'w') as file:
        fieldnames = ['name', 'price', 'product_url', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products:
            name = product['name']
            price = product['utLogMap']['originalPrice']
            product_url = product['productUrl']

            quantity = parse_product_title(name)

            writer.writerow({'name':name, 'price':price, 'product_url':product_url, 'quantity': quantity})
            results.append({'name':name, 'price':price, 'product_url':product_url, 'quantity': quantity})

    return results


def parse_product_title(name):
    word_list = name.split(' ')
    last_word = word_list[-1]

    if any(m in last_word for m in ['gm', 'g', 'kg', 'Gm', 'G']):
        if any(n.isdigit() for n in last_word ):
            return last_word
        else:
            if any(n.isdigit() for n in word_list[-2]):
                return word_list[-2] + word_list[-1]
            
    return ''
            
def filter_qunatity(results):
    for result in results:
        if result['quantity'] != None:
            if '+' in result['quantity']:
                result['quantity'] = result['quantity'].split('+')[0]
            elif '-' in result['quantity']:
                result['quantity'] = result['quantity'].split('-')[-1].replace('-','')

            if 'kg' in result['quantity'] or 'Kg' in result['quantity']:
                result['quantity'] = int(result['quantity'].replace('kg', '000').replace('Kg', '000')) 
            else:
                result['quantity'] = result['quantity'].replace('gm', '').replace('Gm', '').replace('g', '').replace('G', '').replace('(', '').replace(')','')
                result['quantity'] = int(result['quantity'])
        else:
            result['quantity'] = 0
            
    return results

def sort_asec(results):
    sorted_result_asec = sorted(results, key=lambda x: x.get('quantity', float('inf')))
    return sorted_result_asec

    


def sort_dsec(results):
    sorted_result_desc = sorted(results, reverse=True, key=lambda x: x.get('quantity', float('inf')))
    return sorted_result_desc



# def get_product_detail():
#     try:
#         response = scrape()
#         soup = BeautifulSoup(response.text, 'html.parser')

#         scripts = soup.find_all('script')
#         results = []

#         for script in scripts:
#             if 'window.pageData=' in script.text:
#                 products = json.loads(script.text.replace('window.pageData=',''))
#                 products = products["mods"]["listItems"]
#                 break

#         for product in products:
#             name = product['name']
#             price = product['utLogMap']['originalPrice']
#             product_url = product['productUrl']

#             results.append({'name':name, 'price':price, 'product_url':product_url})
#             break

#         return results
    
#     except Exception as error:
#        raise error

if __name__ == "__main__":
    parse_content('rice')

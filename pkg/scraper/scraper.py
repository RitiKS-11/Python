from bs4 import BeautifulSoup
import requests
import json


def connect_daraz():
    try:
        response = requests.get('https://www.daraz.com.np/catalog/?q=snacks')

    except Exception as error:
        raise(error)
    
    return response



def get_product_detail():
    try:
        response = connect_daraz()
        soup = BeautifulSoup(response.text, 'html.parser')

        scripts = soup.find_all('script')
        results = []

        for script in scripts:
            if 'window.pageData=' in script.text:
                products = json.loads(script.text.replace('window.pageData=',''))
                products = products["mods"]["listItems"]
                break

        for product in products:
            name = product['name']
            price = product['utLogMap']['originalPrice']
            product_url = product['productUrl']

            results.append({'name':name, 'price':price, 'product_url':product_url})
            break

        return results
    
    except Exception as error:
       raise error

if __name__ == "__main__":
    connect_daraz()
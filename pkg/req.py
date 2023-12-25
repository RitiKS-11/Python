import requests

def check_connection(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return "Connected"
        return "Not connected"
    
    except Exception as error:
        raise error

    
import requests

def check_connection():
    response = requests.get('https://www.google.com')

    if response.status_code == 200:
        print("Connected")
    else:
        print("Not connected")
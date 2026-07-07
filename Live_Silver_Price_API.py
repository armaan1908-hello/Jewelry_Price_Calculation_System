import requests

API_KEY = "goldapi-0c40fa590a17ec7b2493f0f2c0ff1822-io"
URL = "https://www.goldapi.io/api/XAG/USD"

def live_silver_price():
    headers = {
        "x-access-token": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        ounce_price = data["price"]
        gram_price = ounce_price / 31
        return round(gram_price,2)
    else:
        print(response.text)
        return NONE

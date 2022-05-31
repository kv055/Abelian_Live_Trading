import requests
def PriceDataFetch():
    # Fetches Bitcoin PriceData
    URI = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=70'
    response = requests.get(URI)
    json = response.json()
    formated = []

    # Formating Data
    for element in json:
        open = round(float(element[1]), 3)
        high = round(float(element[2]), 3)
        low = round(float(element[3]), 3)
        close = round(float(element[4]), 3)
        formated.append([element[0], open, high, low, close])
    
    return formated
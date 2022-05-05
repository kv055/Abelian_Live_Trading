import re
import requests

def get_price(URL):
    answer = requests.get(URL)
    json = answer.json()
    return json
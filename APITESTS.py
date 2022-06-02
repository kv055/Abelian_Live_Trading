import requests

url = "https://twelve-data1.p.rapidapi.com/price"
ticker = "TSLA"
querystring = {"symbol":ticker}

headers = {
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com",
	"X-RapidAPI-Key": "576f339adamshee1d91551d5b1b3p1804ddjsn7b209f387460"
}

response = requests.request("GET", url, headers=headers, params=querystring)
answer = response.json()
answer['ticker'] = ticker


# url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"

# querystring = {"symbol":"TSLA","region":"US"}

# headers = {
# 	"X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
# 	"X-RapidAPI-Key": "576f339adamshee1d91551d5b1b3p1804ddjsn7b209f387460"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)
# answer = response.json()
# price = answer['price']['regularMarketPrice']['raw']
l = 0
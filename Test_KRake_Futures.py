from Kraken.Kraken_Connector import KrakenSpot


KRAKEN_PUB_KEY = 'ggI06mtvlFsp+XNsbxFMSI9Qt1AKCvv7Uyy+fW8ounsIyEwzGWwP8G0T'
KRAKEN_PRIV_KEY = 'T29RIWHSmvA0hPNk4F+bRhiQmJoRBjCiRyneJfBCgZu6Uiba2TzyKnlpnThZwgo7WCFV1E6pVhshoszGt2az7g=='

# https://futures.kraken.com/derivatives/api/v3
FuturesTestConnection = KrakenSpot(KRAKEN_PUB_KEY,KRAKEN_PRIV_KEY)

ballance = FuturesTestConnection.get_account_info()
print(ballance)
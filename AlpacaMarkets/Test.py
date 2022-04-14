import alpaca_trade_api as tradeapi

# Endpoints
APCA_API_BASE_URL =	'https://api.alpaca.markets' 
APCA_API_DATA_URL = 'https://data.alpaca.markets'
APCA_API_PAPERTRADING_URL = 'https://paper-api.alpaca.markets'

# Keys
PAPER_APCA_API_KEY_ID = 'PK0RPI7F5X8M0VVED26I'
PAPER_APCA_API_SECRET_KEY = '6VoDwGzKZ3uvPPq8awfspLesuYDnPqYtx0ZhPefG'

APCA_API_KEY_ID = 'AKTY9EUCRJZWTAIQVKQR'
APCA_API_SECRET_KEY = 'Beynq6kJ4aCapM3E6xRH5BDhziFzuMaxyCTjMwIq'


# LiveTrading Config
livetrading = tradeapi.REST(
    APCA_API_KEY_ID, 
    APCA_API_SECRET_KEY,
    APCA_API_BASE_URL
    )
account = livetrading.get_account()
print('Live Trading Account: ',account)


# PaperTrading Config
papertrading = tradeapi.REST(
    PAPER_APCA_API_KEY_ID, 
    PAPER_APCA_API_SECRET_KEY,
    APCA_API_PAPERTRADING_URL
)

paperaccount = papertrading.get_account()
print('Paper Trading Account: ',paperaccount)


# Get historic Data
historic = papertrading.get_bars(
    "AAPL", 
    tradeapi.TimeFrame(30, tradeapi.TimeFrameUnit.Minute), 
    "2021-06-08", 
    "2021-06-08", 
    adjustment='raw').df

# print(historic)

# Implement WebSockets



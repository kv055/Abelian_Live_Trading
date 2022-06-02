from AlpacaMarkets.AlpacaConnector import Alpaca

# get all stocks
def all_tickers_Alpaca():
    paper_trading_connector = Alpaca(
        'PK0RPI7F5X8M0VVED26I',
        '6VoDwGzKZ3uvPPq8awfspLesuYDnPqYtx0ZhPefG',
        'https://paper-api.alpaca.markets'
    )


    all_assets = paper_trading_connector.get_assets()
    alpaca_assets = [asset for asset in all_assets if asset['tradable'] == True]

    Alpaca_tickers = []

    for asset in alpaca_assets:
        # asset_dict = {
        #     'ticker': asset['symbol'],
        #     'exchange': asset['exchange']
        # }
        Alpaca_tickers.append(asset['symbol'])

    return Alpaca_tickers

def all_links_Alpaca():
    tickers = all_tickers_Alpaca()
    data_provider_name = 'Alpaca'
    live_data_URIs = []
    ohlc_data_URIs = []

    for symbol in tickers:
        ohlc_data_URI = '/stocks/'+symbol+'/bars'
        ohlc_data_URIs.append(ohlc_data_URI)
        live_data_URI = '/stocks/'+symbol+'/bars/latest'
        live_data_URIs.append(live_data_URI)

    # return tuples so that it can be inserted
    db_format_content = []
    # if len(pairs) == len(ohlc_data_URIs) == len(live_data_URIs):
    #     for i in range(0, len(pairs)):
    #         db_format_content.append(
    #             (pairs[i],exchange_name,ohlc_data_URIs[i],live_data_URIs[i])
    #         )
            
    # return db_format_content





# data_api_connectors = Alpaca(
#     'AKTY9EUCRJZWTAIQVKQR',
#     'Beynq6kJ4aCapM3E6xRH5BDhziFzuMaxyCTjMwIq',
#     'https://data.alpaca.markets'
# )


# # historic URL
# h = data_api_connectors.get_historical()
# # live_data URL
# l = data_api_connectors.get_live_data()

# print()
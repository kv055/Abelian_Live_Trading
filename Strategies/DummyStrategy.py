import random


class DumbStrategy:
    def __init__ (self):
        # (self, config_rows, connector_list)
        self.strategy_id = 1

    def execute_trading(self, config_rows):
        for obj in config_rows:
            
            # Initialisation
            price_data = obj['pricedata']()
            account_cursor = obj['connector']
            trading_asset_dict = obj['asset_dict']
            ballances = account_cursor.get_ballance_of_trading_asset_and_cash(trading_asset_dict)

            # Signal Generation
            # n = random.random()
            n =0.81

            # Construction of Order Dict
            order_dict = {
                'ticker' : trading_asset_dict['ticker'],
                'quantity' : 1.0,
                'type' : 'market', 
                'time_in_force' : 'day'
            }

            # Signal Execution
            if (n >= 0.8):
                order_dict['side'] = 'buy'
            elif(n <= 0.2):
                order_dict['side'] = 'sell'

            order_confirmation_or_rejection = account_cursor.new_order(order_dict)
            print(order_confirmation_or_rejection)
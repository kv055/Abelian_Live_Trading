import random
from Database_SQL.Log_Strategy_Output_Class import Log_Live_Strategy_Output

class DumbStrategy:
    def __init__ (self):
        self.strategy_id = 1
        self.connector = Log_Live_Strategy_Output()
        # The following prt might be integrated into the execute_trading method
        # in case for each config row getting its own log table, but not sure yet
        self.connector.create_logging_table()

    def execute_trading(self, config_rows):
        for obj in config_rows:
            
            # Initialisation
            price_data = obj['pricedata']()
            account_cursor = obj['connector']
            trading_asset_dict = obj['asset_dict']
            ballances = account_cursor.get_ballance_of_trading_asset_and_cash(trading_asset_dict)

            # Signal Generation
            # n = 0.1
            n = random.random()
            print('Signal: ',n)
            
            # Construction of Order Dict
            order_dict = {
                'ticker' : trading_asset_dict['ticker'],
                'quantity' : 1.0,
                'type' : 'market', 
                'time_in_force' : 'day'
            }

            # Signal Execution
            if (n >= 0.9):
                order_dict['side'] = 'buy'

                order_confirmation_or_rejection = account_cursor.new_order(order_dict)
                print(order_confirmation_or_rejection)

                # Log everything to the Database
                self.connector.Log_to_db({
                    'Asset_Price':price_data,
                    'Portfolio_Ballances':ballances,
                    'Trade_Signal':n,
                    'Order_Sent':order_dict,
                    'Order_Confirmation_Rejection_msg':order_confirmation_or_rejection
                    })
            
            elif(n <= 0.1):
                order_dict['side'] = 'sell'

                order_confirmation_or_rejection = account_cursor.new_order(order_dict)
                print(order_confirmation_or_rejection)

                # Log everything to the Database
                self.connector.Log_to_db({
                    'Asset_Price':price_data,
                    'Portfolio_Ballances':ballances,
                    'Trade_Signal':n,
                    'Order_Sent':order_dict,
                    'Order_Confirmation_Rejection_msg':order_confirmation_or_rejection
                    })

            else:
                print('No trade executed')
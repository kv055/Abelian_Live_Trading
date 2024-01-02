import random
from Database_Dynamo.aws_dynamo_connect import DynamoDB_Class

class DumbStrategy:
    def __init__ (self):
        self.strategy_id = 1
        self.db = DynamoDB_Class()

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
                self.db.Strategy_Output_Log({
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
                self.db.Strategy_Output_Log({
                    'Asset_Price':price_data,
                    'Portfolio_Ballances':ballances,
                    'Trade_Signal':n,
                    'Order_Sent':order_dict,
                    'Order_Confirmation_Rejection_msg':order_confirmation_or_rejection
                    })

            else:
                print('No trade executed')
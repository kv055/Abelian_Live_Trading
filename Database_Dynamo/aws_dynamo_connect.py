import os
import boto3
from dotenv import load_dotenv

class DynamoDB_Class:
    def __init__(self):
        try:
            load_dotenv()
            self.AWSDYNAMO_REGION = os.getenv('AWSDYNAMO_REGION')
            self.AWSDYNAMO_KEY_ID = os.getenv('AWSDYNAMO_KEY_ID')
            self.AWSDYNAMO_PRIV_KEY = os.getenv('AWSDYNAMO_PRIV_KEY')
            self.AWSDYNAMO_TABLE = os.getenv('AWSDYNAMO_TABLE')
            
            # Initialize a DynamoDB client
            self.dynamodb = boto3.resource(
                'dynamodb', 
                region_name=self.AWSDYNAMO_REGION, 
                aws_access_key_id=self.AWSDYNAMO_KEY_ID, 
                aws_secret_access_key=self.AWSDYNAMO_PRIV_KEY
            )
            self.table = self.dynamodb.Table(self.AWSDYNAMO_TABLE)
        except Exception as e:
            print(f"Error during initialization: {e}")
            # You might want to add additional handling (logging, raising exceptions) based on your use case.

    def Strategy_Output_Log(self, Strategy_Output):
        # Convert all floats to str
        Strategy_Output['Trade_Signal'] = str(Strategy_Output['Trade_Signal'])
        Strategy_Output['Asset_Price']['last_price'] = str(Strategy_Output['Asset_Price']['last_price'] )
        Strategy_Output['Order_Sent']['quantity'] = str(Strategy_Output['Order_Sent']['quantity'])
        Strategy_Output['TradeID'] = Strategy_Output['Trade_Signal'] 
        
        self.table.put_item(Item=Strategy_Output)
        l = 0


    def Liver_Orders_Log(self, Order):
        try:
            self.table.put_item(Item=Order)
            print("Order inserted successfully.")
        except Exception as e:
            print(f"Error inserting order: {e}")
            # Handle the exception appropriately (logging, retrying, etc.).




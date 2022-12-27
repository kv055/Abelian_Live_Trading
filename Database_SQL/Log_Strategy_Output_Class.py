from Database_SQL.aws_sql_connect import SQL_Server
import json

class Log_Live_Strategy_Output:
    def __init__(self) -> None:
        self.db_name = 'Live_Trading_Logs'
        self.connector = SQL_Server(self.db_name) 

    def create_logging_table(self):
        self.log_table_name = 'LOG_STRATEGY_OUTPUT'
        create_log_db_sql = f"""
            CREATE TABLE IF NOT EXISTS {self.db_name}.{self.log_table_name} (
            `Asset_Price` varchar(255) NOT NULL,
            `Portfolio_Ballances` varchar(255) NOT NULL,
            `Trade_Signal` varchar(255) NOT NULL,
            `Order_Sent` varchar(255) NOT NULL,
            `Order_Confirmation_Rejection_msg` varchar(255) NOT NULL
            )
        """
        self.connector.cursor.execute(create_log_db_sql)
        self.connector.connection.commit()

    def Log_to_db(self, log_dict):
        log_sql = """
            INSERT INTO LOG_STRATEGY_OUTPUT (
                Asset_Price,
                Portfolio_Ballances,
                Trade_Signal,
                Order_Sent,
                Order_Confirmation_Rejection_msg
                ) 
                VALUES (%s, %s, %s, %s, %s)
            """

        log_set = [                      
            json.dumps(log_dict['Asset_Price']), 
            json.dumps(log_dict['Portfolio_Ballances']), 
            log_dict['Trade_Signal'], 
            json.dumps(log_dict['Order_Sent']), 
            json.dumps(log_dict['Order_Confirmation_Rejection_msg'])
            ]
        
        self.connector.cursor.execute(log_sql,log_set)
        self.connector.connection.commit()

from Message_Que.Q_PUB_SUB_class import Q

class Subscribe_Config_Rows:
    def __init__(self):
        self.que = Q()
      
    def fetch_stop_trading_messages(self):
        fetched_messages = self.que.subscribe()
        
        for message in fetched_messages:
            if message['Message_Group'] != 'Stop_Trading':
                fetched_messages.remove(message)

        if len(fetched_messages) > 0:
            return fetched_messages
        else:
            return []

    def fetch_deploy_trading_messages(self):
        fetched_messages = self.que.subscribe()
        
        for message in fetched_messages:
            if message['Message_Group'] != 'Deploy':
                fetched_messages.remove(message)

        if len(fetched_messages) > 0:
            return fetched_messages
        else:
            return []

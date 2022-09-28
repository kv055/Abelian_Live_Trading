import os
from dotenv import load_dotenv
import boto3
import json
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

class Q:
    def __init__(self):
        load_dotenv()
        self.client = boto3.client(
            'sqs',
            region_name= os.getenv('AWS_REGION'),
            aws_access_key_id= os.getenv('AWS_KEY_ID'),
            aws_secret_access_key= os.getenv('AWS_PRIVATE_KEY')
        )
        # self.q_instance = self.client.get_queue_by_name(QueueName='Test_Q')
        # self.FIFO_q_instance = self.client.get_queue_by_name(QueueName='Test_FIFO_Q.fifo')
        self.queue_url = 'https://sqs.ap-southeast-2.amazonaws.com/254538634148/Test_Q'
        self.fifo_q_url = 'https://sqs.ap-southeast-2.amazonaws.com/254538634148/Test_FIFO_Q.fifo'
    
    def publish(self, msg_body):
        # response = self.q_instance.
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=msg_body
        )
        return response

    def publish_many(self, list_of_msg_bodies):
        response = self.q_instance.send_messages(
            Entries=list_of_msg_bodies
        )
        return response

    def publish_FIFO(self, msg_body):
        # response = self.FIFO_q_instance.
        response = self.client.send_message(
            MessageDeduplicationId=msg_body,
            MessageBody=msg_body,
            MessageGroupId='Testen'
        )
        return response

    def publish_many_FIFO(self, list_of_msg_bodies):
        response = self.FIFO_q_instance.send_messages(
            Entries=list_of_msg_bodies
        )
        return response

    def subscribe_FIFO(self):
        response = self.FIFO_q_instance.receive_messages()
        return response

    def subscribe(self):
        # response = self.q_instance.receive_messages(
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            AttributeNames=[
                'ApproximateFirstReceiveTimestamp',
                'ApproximateReceiveCount'
            ],
            VisibilityTimeout=60
        )

        if 'Messages' in response:
            formated_message_bodies = self.formate_SUB_response_message(response)
            return formated_message_bodies
        else:
            return []
        
    def delete_message(self, message_id):
        pass

    def formate_SUB_response_message(self, q_response):
        formated_message_bodies = []
                    
        for message in q_response['Messages']:
            body_as_string = message['Body']
            body_as_dict = json.loads(body_as_string)
            body_as_dict['Message_ID'] = message['MessageId']
            formated_message_bodies.append(body_as_dict)

        return formated_message_bodies
    
    def list_queues(sqs_resource):
        """
        Creates an iterable of all Queue resources in the collection.
        """
        try:
            sqs_queues = []
            for queue in sqs_resource.queues.all():
                sqs_queues.append(queue)
        except ClientError:
            logger.exception('Could not list queues.')
            raise
        else:
            return sqs_queues 
     
    def delete_message(self, MessageID):
        pass
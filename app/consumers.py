from channels.generic.websocket import WebsocketConsumer
import json
from app import chatbot

class ChatRoomUser(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type':'successful_connection',
            'message':'Welcome! I am Covid-Chatbot, please ask me any covid related questions.',
            'username':'Covid-Chatbot'
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response = str(coronabot.get_response(message))

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'response':response,
            'username': 'Me'
        }))

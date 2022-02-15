from channels.generic.websocket import WebsocketConsumer
import json

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

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username': 'Me'
        }))

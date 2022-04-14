from channels.generic.websocket import WebsocketConsumer
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

covidChatbot = ChatBot("Covid-Chatbot", tagger_language=ENGSM,
    logic_adapters = [  
            "chatterbot.logic.BestMatch",
        {
            'import_path': 'app.chatbot.USLogic.MyLogicAdapter',
            'default_response': "I'm sorry I could not find that information",
        },
        {
            'import_path': 'app.chatbot.stateLogic.MyLogicAdapter',
            'default_response': "I'm sorry I could not find that information",
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)
training_data_static = open('app/covidStaticResponses.txt').read().splitlines()
trainer = ListTrainer(covidChatbot)
trainer.train(training_data_static)
trainer_corpus = ChatterBotCorpusTrainer(covidChatbot)
trainer_corpus.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
    )

class ChatRoomUser(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.receive(text_data=json.dumps({
            'type':'successful_connection',
            'message':'Welcome! I am Covid-Chatbot, please ask me any covid related questions.',
            'username':'Covid-Chatbot'
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response = str(covidChatbot.get_response(message))

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'response':response,
            'username': 'Me'
            }))




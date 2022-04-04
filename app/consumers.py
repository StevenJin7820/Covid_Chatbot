from channels.generic.websocket import WebsocketConsumer
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")
coronabot = ChatBot("Coronabot",
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)
training_data_static = open('app\covidStaticResponses.txt').read().splitlines()
trainer = ListTrainer(coronabot)
trainer.train(training_data_static)
trainer_corpus = ChatterBotCorpusTrainer(coronabot)
trainer_corpus.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
    )

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

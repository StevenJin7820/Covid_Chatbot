from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")

coronabot = ChatBot("Bill")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(coronabot)
trainer.train(conversation)

trainer_corpus = ChatterBotCorpusTrainer(coronabot)
trainer.train("chatterbot.corpus.english")

def index(request):
    return render(request, 'index.html', {})

def chat(request):
    return render(request, 'chat.html')
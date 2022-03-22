from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")

coronabot = ChatBot("Coronabot")

trainer_corpus = ChatterBotCorpusTrainer(coronabot)
trainer_corpus.train("chatterbot.corpus.english")
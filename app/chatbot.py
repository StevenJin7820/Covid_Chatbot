from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")

coronabot = ChatBot("Coronabot")

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
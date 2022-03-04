from codecs import ignore_errors
import random
import json
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout


lemmatizer = WordNetLemmatizer

intents = json.loads(open("app\intents.json").read())

words = []
classes = []
documents = []
ignore_punctuation = ["?", "!", ".", ","]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        #Tokenize breaks a line down to its individual words and returns it as a list
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        #We append to documents a tuple of word_list and the intent tag, this way we know what words match to which tag
        documents.append((word_list, intent["tag"]))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)
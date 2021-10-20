# -*- coding: utf-8 -*-
"""
jedi chatbot
"""

pip install nltk

pip install newspaper3k

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

article = Article('https://openstax.org/books/entrepreneurship/pages/1-1-entrepreneurship-today#0') 
article.download()
article.parse()
article.nlp()
corpus = article.text

print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)

print(sentence_list)

#Response to greetings
def greeting_response(text):
  text = text.lower()

  bot_greetings = ['hello sir', 'hi', 'namaste sir', 'what can i do for you?', 'Hi sir']
  user_greeting = ['hi', 'hi_jedi', 'hey','jedi']

  for word in text.split():
    if word in user_greetings:
      return random.choice(bob_greetings)

def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0, length))

  x = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]] > x[list_index[j]]:
        #swap
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp
  return list_index

#create the bot response
def bot_response(user_input):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_response = ''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1], cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort(similarity_scores_list)

  j = 0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      bot_response = bot_response + ' ' + sentence_list[index[i]]
      response_flag = 1
      j = j + 1
      if j > 2:
        break

  if response_flag == 0:
    bot_response = bot_response+ " " + "I apolagise i dont understand."

  sentence_list.remove(user_input)
  return bot_response

print('jedi: i am jedi i can answer your queries about entrprenourship, or say exit to end the chat, Thank you')
exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']
while(True):
  user_input = input()
  if user_input.lower in exit_list:
    print('jedi: chat with you later')
    break

  else:
    if greetin_response(user_input) != None:
      print('jedi: ' + greeting_response(user_input))  
    else:
      print('jedi: '+bot_response(user_inpu))



